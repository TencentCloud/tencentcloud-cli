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

