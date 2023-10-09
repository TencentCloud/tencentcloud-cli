**Example 1: 查询java内存马事件详细信息**



Input: 

```
tccli cwp DescribeJavaMemShellInfo --cli-unfold-argument  \
    --Id 1
```

Output: 
```
{
    "Response": {
        "RequestId": "d92d723e-4aac-4f4a-bbf9-e5430e29d289",
        "Info": {
            "InstanceName": "v_llzlu-PC0",
            "InstanceState": "RUNNING",
            "PrivateIp": "192.168.255.10",
            "PublicIp": "110.40.207.98",
            "Type": 1,
            "Description": "Java (2845)中加载的net...",
            "CreateTime": "2021-01-20 16:17:11",
            "RecentFoundTime": "2021-01-20 16:17:11",
            "Status": 0,
            "ClassLoaderName": "org.apache.jasper.servlet.JasperLoader",
            "SuperClassName": "java.lang.Object",
            "Md5": "37e54fce63f1ca6c82927caf7aa1c412",
            "Interfaces": "java.IO.Writer,java.IO.Reader",
            "Annotations": "注释",
            "Pid": 123,
            "Exe": "/usr/lib/jvm/java-6-openjdk-amd64/jre/bin/java",
            "Args": "org.apache.catalina.startup.Bootstrap start",
            "ClassName": "main.class",
            "ClassContent": "avewsa==...",
            "ClassContentPretty": "package com.company;public class Main public static void main(String[] args) ...",
            "EventDescription": "腾讯御见...",
            "SecurityAdvice": "安全建议.."
        }
    }
}
```

