**Example 1: success**



Input: 

```
tccli tcbr DescribeCloudRunServerDetail --cli-unfold-argument  \
    --ServerName 字符串 \
    --EnvId 字符串
```

Output: 
```
{
    "Response": {
        "BaseInfo": null,
        "RequestId": "34143393-ede8-43ac-ad78-12a5bfea9663",
        "ServerConfig": null,
        "OnlineVersionInfos": null
    }
}
```

**Example 2: DescribeCloudRunServerDetail**



Input: 

```
tccli tcbr DescribeCloudRunServerDetail --cli-unfold-argument  \
    --ServerName xx \
    --EnvId xx
```

Output: 
```
{
    "Response": {
        "BaseInfo": {
            "Status": "xx",
            "ServerName": "xx",
            "CustomDomainName": "xx",
            "UpdateTime": "xx",
            "DefaultDomainName": "xx"
        },
        "ServerConfig": {
            "EnvId": "xx",
            "MaxNum": 1,
            "BuildDir": "xx",
            "Mem": 0.0,
            "ServerName": "xx",
            "InitialDelaySeconds": 1,
            "CustomLogs": "xx",
            "CreateTime": "xx",
            "MinNum": 1,
            "HasDockerfile": true,
            "EnvParams": "xx",
            "Dockerfile": "xx",
            "Port": "xx",
            "Cpu": 0.0
        },
        "OnlineVersionInfos": [
            {
                "VersionName": "test-001",
                "ImageUrl": "test:01"
            }
        ],
        "RequestId": "xx"
    }
}
```

