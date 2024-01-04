**Example 1: 查询应用**

查询应用

Input: 

```
tccli hai DescribeApplications --cli-unfold-argument  \
    --ApplicationIds app-jxnaqazx \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "ApplicationSet": [
            {
                "ApplicationId": "app-jxnaqazx",
                "ApplicationName": "应用名称",
                "Description": "应用描述",
                "ConfigEnvironment": "",
                "MinSystemDiskSize": 80,
                "ApplicationState": "ONLINE",
                "ApplicationSize": 50,
                "ApplicationType": "PRIVATE_APPLICATION",
                "CreateTime": "2023-09-18 16:48:47"
            }
        ],
        "RequestId": "2b1fae52-8004-4a13-a20a-26ea1149f9df",
        "TotalCount": 1
    }
}
```

