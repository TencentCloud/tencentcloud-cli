**Example 1: 获取容器应用防护内存马扫描事件详情**



Input: 

```
tccli cwp DescribeRaspMemShellDetailTCSS --cli-unfold-argument  \
    --Id 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Alias": "v_llzlu微隔离测试(millionlan)",
            "Annotations": "",
            "Args": "org.apache.catalina.startup.Bootstrap start",
            "ClassContent": "yv66vgAAADIAHAoABgAOCQAPABAIABEKABIAEwcAFAcAFQEABjxpbml0PgEAAygpVgEABENvZGUBAA9MaW5lTnVtYmVyVGFibGUBAAg8Y2xpbml0PgEAClNvdXJjZUZpbGUBAAxQYXlsb2FkLmphdmEMAAcACAcAFgwAFwAYAQALUGF5bG9hZEluaXQHABkMABoAGwEADG1haW4vUGF5bG9hZAEAEGphdmEvbGFuZy9PYmplY3QBABBqYXZhL2xhbmcvU3lzdGVtAQADb3V0AQAVTGphdmEvaW8vUHJpbnRTdHJlYW07AQATamF2YS9pby9QcmludFN0cmVhbQEAB3ByaW50bG4BABUoTGphdmEvbGFuZy9TdHJpbmc7KVYAIQAFAAYAAAAAAAIAAQAHAAgAAQAJAAAAHQABAAEAAAAFKrcAAbEAAAABAAoAAAAGAAEAAAAEAAgACwAIAAEACQAAACUAAgAAAAAACbIAAhIDtgAEsQAAAAEACgAAAAoAAgAAAAYACAAHAAEADAAAAAIADQ==",
            "ClassContentPretty": "/*\n * Decompiled with CFR 0.152.\n */\npackage main;\n\npublic class Payload {\n    static {\n        System.out.println(\"PayloadInit\");\n    }\n}",
            "ClassLoaderName": "org.apache.jsp.bebinder_005fshell_jsp$U",
            "ClassName": "main.Payload",
            "ClusterId": "",
            "ClusterName": "",
            "ContainerId": "",
            "ContainerName": "",
            "ContainerNetStatus": "",
            "ContainerStatus": "",
            "CreateTime": "2025-04-18 17:33:33",
            "EventDescription": "检测到Java服务进程中存在Java内存木马。Java内存马能长期驻留在内存中，接收攻击者输入，从而达到长期远程控制服务器的目的",
            "Exe": "/usr/lib/jvm/java-7-openjdk-amd64/jre/bin/java",
            "HostTags": [],
            "Id": 1,
            "ImageId": "",
            "ImageName": "",
            "InstanceID": "ins-j7vumfb6",
            "Interfaces": "",
            "Md5": "4f5f5774ace8d6ad95eec034def6f610",
            "NodeName": "v_llzlu微隔离测试(millionlan)",
            "Pid": 206840,
            "PodIp": "",
            "PodName": "",
            "PrivateIp": "10.0.1.233",
            "PublicIp": "43.138.142.208",
            "Quuid": "acdd5474-6360-4fd4-bfc7-843162cb8116",
            "RecentFoundTime": "2025-04-18 17:40:26",
            "SecurityAdvice": "检查Java服务访问日志，评估内存马是否被访问; 检查主机高危漏洞，修复高危漏洞并重启java服务",
            "Status": 1,
            "SuperClassName": "",
            "Type": 5
        },
        "RequestId": "f1d582d9-bca8-4f9a-8e65-4b5ebef83719"
    }
}
```

