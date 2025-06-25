**Example 1: 查询java内存马事件列表**

查询java内存马事件列表

Input: 

```
tccli cwp DescribeJavaMemShellList --cli-unfold-argument  \
    --Offset 1 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Id": 184113,
                "Quuid": "d4cc302e-09e5-436f-b99b-5ab9c9070323",
                "Uuid": "d4cc302e-09e5-436f-b99b-5ab9c9070323",
                "Alias": "machine",
                "HostIp": "1.1.1.1",
                "Type": 0,
                "Description": "检测到java进程921852/org.apache.catalina.startup.Bootstrap start中加载的webshell_filter类中存在木马",
                "CreateTime": "2024-09-20 15:32:08",
                "RecentFoundTime": "2024-09-20 15:32:08",
                "Status": 1,
                "MachineExtraInfo": {
                    "WanIP": "1.1.1.1",
                    "PrivateIP": "1.1.1.1",
                    "NetworkType": 0,
                    "NetworkName": "vpc-id",
                    "InstanceID": "ins-id",
                    "HostName": "hn"
                },
                "ClassName": "webshell_filter",
                "SuperClassName": "java.my.******",
                "Interfaces": "javax\\.servlet\\.Filter",
                "Annotations": "anno",
                "LoaderClassName": "org\\.apache\\.jsp\\.bebinder_005fshell_jsp\\$U"
            }
        ],
        "RequestId": "bf4896f8-84ba-405d-bbc9-b4d951f52161",
        "TotalCount": 1
    }
}
```

**Example 2: 查看内存马注入事件列表**

查看内存马注入事件列表

Input: 

```
tccli cwp DescribeJavaMemShellList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Alias": "内存马注入",
                "Annotations": "",
                "ClassName": "org\\.apache\\.jsp\\.test_jsp",
                "CreateTime": "2025-06-22 14:36:54",
                "Description": "检测到java进程1229492/org.apache.catalina.startup.Bootstrap start中加载的org.apache.jsp.test_jsp类中存在木马",
                "HostIp": "129.226.165.240",
                "Id": 163073,
                "Interfaces": "org\\.apache\\.jasper\\.runtime\\.JspSourceImports\\|javax\\.servlet\\.ServletConfig\\|javax\\.servlet\\.Servlet\\|org\\.apache\\.jasper\\.runtime\\.JspSourceDependent\\|javax\\.servlet\\.jsp\\.HttpJspPage\\|java\\.io\\.Serializable",
                "LoaderClassName": "",
                "MachineExtraInfo": {
                    "HostName": "",
                    "InstanceID": "ins-7hg2g94e",
                    "NetworkName": "",
                    "NetworkType": 0,
                    "PrivateIP": "172.19.0.14",
                    "WanIP": "129.226.165.240"
                },
                "Quuid": "421c0ff7-84ce-4f41-b015-9329748e90d9",
                "RecentFoundTime": "2025-06-22 14:36:54",
                "Status": 1,
                "SuperClassName": "org\\.apache\\.jasper\\.runtime\\.HttpJspBase\\|javax\\.servlet\\.http\\.HttpServlet\\|javax\\.servlet\\.GenericServlet",
                "Type": 2,
                "Uuid": "421c0ff7-84ce-4f41-b015-9329748e90d9"
            },
            {
                "Alias": "内存马注入",
                "Annotations": "",
                "ClassName": "org\\.apache\\.jsp\\.test_jsp",
                "CreateTime": "2025-06-22 12:17:02",
                "Description": "检测到java进程1185744/org.apache.catalina.startup.Bootstrap start中加载的org.apache.jsp.test_jsp类中存在木马",
                "HostIp": "129.226.165.240",
                "Id": 163072,
                "Interfaces": "org\\.apache\\.jasper\\.runtime\\.JspSourceImports\\|javax\\.servlet\\.ServletConfig\\|javax\\.servlet\\.Servlet\\|org\\.apache\\.jasper\\.runtime\\.JspSourceDependent\\|javax\\.servlet\\.jsp\\.HttpJspPage\\|java\\.io\\.Serializable",
                "LoaderClassName": "",
                "MachineExtraInfo": {
                    "HostName": "",
                    "InstanceID": "ins-7hg2g94e",
                    "NetworkName": "",
                    "NetworkType": 0,
                    "PrivateIP": "172.19.0.14",
                    "WanIP": "129.226.165.240"
                },
                "Quuid": "421c0ff7-84ce-4f41-b015-9329748e90d9",
                "RecentFoundTime": "2025-06-22 12:17:02",
                "Status": 1,
                "SuperClassName": "org\\.apache\\.jasper\\.runtime\\.HttpJspBase\\|javax\\.servlet\\.http\\.HttpServlet\\|javax\\.servlet\\.GenericServlet",
                "Type": 2,
                "Uuid": "421c0ff7-84ce-4f41-b015-9329748e90d9"
            },
            {
                "Alias": "内存马注入",
                "Annotations": "",
                "ClassName": "org\\.apache\\.jsp\\.test_jsp",
                "CreateTime": "2025-06-21 17:40:02",
                "Description": "检测到java进程843518/org.apache.catalina.startup.Bootstrap start中加载的org.apache.jsp.test_jsp类中存在木马",
                "HostIp": "129.226.165.240",
                "Id": 163071,
                "Interfaces": "org\\.apache\\.jasper\\.runtime\\.JspSourceImports\\|javax\\.servlet\\.ServletConfig\\|javax\\.servlet\\.Servlet\\|org\\.apache\\.jasper\\.runtime\\.JspSourceDependent\\|javax\\.servlet\\.jsp\\.HttpJspPage\\|java\\.io\\.Serializable",
                "LoaderClassName": "",
                "MachineExtraInfo": {
                    "HostName": "",
                    "InstanceID": "ins-7hg2g94e",
                    "NetworkName": "",
                    "NetworkType": 0,
                    "PrivateIP": "172.19.0.14",
                    "WanIP": "129.226.165.240"
                },
                "Quuid": "421c0ff7-84ce-4f41-b015-9329748e90d9",
                "RecentFoundTime": "2025-06-21 17:40:02",
                "Status": 1,
                "SuperClassName": "org\\.apache\\.jasper\\.runtime\\.HttpJspBase\\|javax\\.servlet\\.http\\.HttpServlet\\|javax\\.servlet\\.GenericServlet",
                "Type": 2,
                "Uuid": "421c0ff7-84ce-4f41-b015-9329748e90d9"
            },
            {
                "Alias": "内存马注入",
                "Annotations": "",
                "ClassName": "org\\.apache\\.jsp\\.test_jsp",
                "CreateTime": "2025-06-21 16:16:00",
                "Description": "检测到java进程816313/org.apache.catalina.startup.Bootstrap start中加载的org.apache.jsp.test_jsp类中存在木马",
                "HostIp": "129.226.165.240",
                "Id": 163070,
                "Interfaces": "org\\.apache\\.jasper\\.runtime\\.JspSourceImports\\|javax\\.servlet\\.ServletConfig\\|javax\\.servlet\\.Servlet\\|org\\.apache\\.jasper\\.runtime\\.JspSourceDependent\\|javax\\.servlet\\.jsp\\.HttpJspPage\\|java\\.io\\.Serializable",
                "LoaderClassName": "",
                "MachineExtraInfo": {
                    "HostName": "",
                    "InstanceID": "ins-7hg2g94e",
                    "NetworkName": "",
                    "NetworkType": 0,
                    "PrivateIP": "172.19.0.14",
                    "WanIP": "129.226.165.240"
                },
                "Quuid": "421c0ff7-84ce-4f41-b015-9329748e90d9",
                "RecentFoundTime": "2025-06-21 16:16:00",
                "Status": 1,
                "SuperClassName": "org\\.apache\\.jasper\\.runtime\\.HttpJspBase\\|javax\\.servlet\\.http\\.HttpServlet\\|javax\\.servlet\\.GenericServlet",
                "Type": 2,
                "Uuid": "421c0ff7-84ce-4f41-b015-9329748e90d9"
            },
            {
                "Alias": "内存马注入",
                "Annotations": "",
                "ClassName": "org\\.apache\\.jsp\\.test_jsp",
                "CreateTime": "2025-06-21 16:11:43",
                "Description": "检测到java进程814511/org.apache.catalina.startup.Bootstrap start中加载的org.apache.jsp.test_jsp类中存在木马",
                "HostIp": "129.226.165.240",
                "Id": 163069,
                "Interfaces": "org\\.apache\\.jasper\\.runtime\\.JspSourceImports\\|javax\\.servlet\\.ServletConfig\\|javax\\.servlet\\.Servlet\\|org\\.apache\\.jasper\\.runtime\\.JspSourceDependent\\|javax\\.servlet\\.jsp\\.HttpJspPage\\|java\\.io\\.Serializable",
                "LoaderClassName": "",
                "MachineExtraInfo": {
                    "HostName": "",
                    "InstanceID": "ins-7hg2g94e",
                    "NetworkName": "",
                    "NetworkType": 0,
                    "PrivateIP": "172.19.0.14",
                    "WanIP": "129.226.165.240"
                },
                "Quuid": "421c0ff7-84ce-4f41-b015-9329748e90d9",
                "RecentFoundTime": "2025-06-21 16:11:43",
                "Status": 1,
                "SuperClassName": "org\\.apache\\.jasper\\.runtime\\.HttpJspBase\\|javax\\.servlet\\.http\\.HttpServlet\\|javax\\.servlet\\.GenericServlet",
                "Type": 2,
                "Uuid": "421c0ff7-84ce-4f41-b015-9329748e90d9"
            },
            {
                "Alias": "内存马注入",
                "Annotations": "",
                "ClassName": "org\\.apache\\.jsp\\.test_jsp",
                "CreateTime": "2025-06-21 16:07:50",
                "Description": "检测到java进程813379/org.apache.catalina.startup.Bootstrap start中加载的org.apache.jsp.test_jsp类中存在木马",
                "HostIp": "129.226.165.240",
                "Id": 163068,
                "Interfaces": "org\\.apache\\.jasper\\.runtime\\.JspSourceImports\\|javax\\.servlet\\.ServletConfig\\|javax\\.servlet\\.Servlet\\|org\\.apache\\.jasper\\.runtime\\.JspSourceDependent\\|javax\\.servlet\\.jsp\\.HttpJspPage\\|java\\.io\\.Serializable",
                "LoaderClassName": "",
                "MachineExtraInfo": {
                    "HostName": "",
                    "InstanceID": "ins-7hg2g94e",
                    "NetworkName": "",
                    "NetworkType": 0,
                    "PrivateIP": "172.19.0.14",
                    "WanIP": "129.226.165.240"
                },
                "Quuid": "421c0ff7-84ce-4f41-b015-9329748e90d9",
                "RecentFoundTime": "2025-06-21 16:07:50",
                "Status": 1,
                "SuperClassName": "org\\.apache\\.jasper\\.runtime\\.HttpJspBase\\|javax\\.servlet\\.http\\.HttpServlet\\|javax\\.servlet\\.GenericServlet",
                "Type": 2,
                "Uuid": "421c0ff7-84ce-4f41-b015-9329748e90d9"
            },
            {
                "Alias": "内存马注入",
                "Annotations": "",
                "ClassName": "org\\.apache\\.jsp\\.test_jsp",
                "CreateTime": "2025-06-21 16:02:50",
                "Description": "检测到java进程812553/org.apache.catalina.startup.Bootstrap start中加载的org.apache.jsp.test_jsp类中存在木马",
                "HostIp": "129.226.165.240",
                "Id": 163067,
                "Interfaces": "org\\.apache\\.jasper\\.runtime\\.JspSourceImports\\|javax\\.servlet\\.ServletConfig\\|javax\\.servlet\\.Servlet\\|org\\.apache\\.jasper\\.runtime\\.JspSourceDependent\\|javax\\.servlet\\.jsp\\.HttpJspPage\\|java\\.io\\.Serializable",
                "LoaderClassName": "",
                "MachineExtraInfo": {
                    "HostName": "",
                    "InstanceID": "ins-7hg2g94e",
                    "NetworkName": "",
                    "NetworkType": 0,
                    "PrivateIP": "172.19.0.14",
                    "WanIP": "129.226.165.240"
                },
                "Quuid": "421c0ff7-84ce-4f41-b015-9329748e90d9",
                "RecentFoundTime": "2025-06-21 16:02:50",
                "Status": 1,
                "SuperClassName": "org\\.apache\\.jasper\\.runtime\\.HttpJspBase\\|javax\\.servlet\\.http\\.HttpServlet\\|javax\\.servlet\\.GenericServlet",
                "Type": 2,
                "Uuid": "421c0ff7-84ce-4f41-b015-9329748e90d9"
            },
            {
                "Alias": "内存马注入",
                "Annotations": "",
                "ClassName": "org\\.apache\\.jsp\\.shell_005finject_jsp",
                "CreateTime": "2025-06-21 11:23:10",
                "Description": "检测到java进程499548/org.apache.catalina.startup.Bootstrap start中加载的org.apache.jsp.shell_005finject_jsp类中存在木马",
                "HostIp": "129.226.165.240",
                "Id": 163065,
                "Interfaces": "org\\.apache\\.jasper\\.runtime\\.JspSourceImports\\|javax\\.servlet\\.ServletConfig\\|javax\\.servlet\\.Servlet\\|org\\.apache\\.jasper\\.runtime\\.JspSourceDependent\\|javax\\.servlet\\.jsp\\.HttpJspPage\\|java\\.io\\.Serializable",
                "LoaderClassName": "",
                "MachineExtraInfo": {
                    "HostName": "",
                    "InstanceID": "ins-7hg2g94e",
                    "NetworkName": "",
                    "NetworkType": 0,
                    "PrivateIP": "172.19.0.14",
                    "WanIP": "129.226.165.240"
                },
                "Quuid": "421c0ff7-84ce-4f41-b015-9329748e90d9",
                "RecentFoundTime": "2025-06-21 11:23:10",
                "Status": 0,
                "SuperClassName": "org\\.apache\\.jasper\\.runtime\\.HttpJspBase\\|javax\\.servlet\\.http\\.HttpServlet\\|javax\\.servlet\\.GenericServlet",
                "Type": 2,
                "Uuid": "421c0ff7-84ce-4f41-b015-9329748e90d9"
            },
            {
                "Alias": "内存马注入",
                "Annotations": "",
                "ClassName": "org\\.apache\\.jsp\\.shell_005finject_jsp\\$MaliciousFilter",
                "CreateTime": "2025-06-21 11:23:10",
                "Description": "检测到java进程499548/org.apache.catalina.startup.Bootstrap start中加载的org.apache.jsp.shell_005finject_jsp$MaliciousFilter类中存在木马",
                "HostIp": "129.226.165.240",
                "Id": 163064,
                "Interfaces": "javax\\.servlet\\.Filter",
                "LoaderClassName": "",
                "MachineExtraInfo": {
                    "HostName": "",
                    "InstanceID": "ins-7hg2g94e",
                    "NetworkName": "",
                    "NetworkType": 0,
                    "PrivateIP": "172.19.0.14",
                    "WanIP": "129.226.165.240"
                },
                "Quuid": "421c0ff7-84ce-4f41-b015-9329748e90d9",
                "RecentFoundTime": "2025-06-21 11:23:10",
                "Status": 0,
                "SuperClassName": "",
                "Type": 0,
                "Uuid": "421c0ff7-84ce-4f41-b015-9329748e90d9"
            },
            {
                "Alias": "内存马注入",
                "Annotations": "",
                "ClassName": "org\\.apache\\.jsp\\.test_jsp",
                "CreateTime": "2025-06-20 23:15:41",
                "Description": "检测到java进程499548/org.apache.catalina.startup.Bootstrap start中加载的org.apache.jsp.test_jsp类中存在木马",
                "HostIp": "129.226.165.240",
                "Id": 163063,
                "Interfaces": "org\\.apache\\.jasper\\.runtime\\.JspSourceImports\\|javax\\.servlet\\.ServletConfig\\|javax\\.servlet\\.Servlet\\|org\\.apache\\.jasper\\.runtime\\.JspSourceDependent\\|javax\\.servlet\\.jsp\\.HttpJspPage\\|java\\.io\\.Serializable",
                "LoaderClassName": "",
                "MachineExtraInfo": {
                    "HostName": "",
                    "InstanceID": "ins-7hg2g94e",
                    "NetworkName": "",
                    "NetworkType": 0,
                    "PrivateIP": "172.19.0.14",
                    "WanIP": "129.226.165.240"
                },
                "Quuid": "421c0ff7-84ce-4f41-b015-9329748e90d9",
                "RecentFoundTime": "2025-06-20 23:15:41",
                "Status": 1,
                "SuperClassName": "org\\.apache\\.jasper\\.runtime\\.HttpJspBase\\|javax\\.servlet\\.http\\.HttpServlet\\|javax\\.servlet\\.GenericServlet",
                "Type": 2,
                "Uuid": "421c0ff7-84ce-4f41-b015-9329748e90d9"
            }
        ],
        "RequestId": "95a7369c-672f-4737-a52c-1aaea420a920",
        "TotalCount": 62
    }
}
```

