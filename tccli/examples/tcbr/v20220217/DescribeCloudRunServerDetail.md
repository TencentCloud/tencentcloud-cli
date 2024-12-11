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
    --EnvId abc \
    --ServerName abc
```

Output: 
```
{
    "Response": {
        "BaseInfo": {
            "ServerName": "abc",
            "DefaultDomainName": "abc",
            "CustomDomainName": "abc",
            "Status": "abc",
            "UpdateTime": "abc",
            "AccessTypes": [
                "abc"
            ],
            "CustomDomainNames": [
                "abc"
            ]
        },
        "ServerConfig": {
            "EnvId": "abc",
            "ServerName": "abc",
            "OpenAccessTypes": [
                "abc"
            ],
            "Cpu": 0,
            "Mem": 0,
            "MinNum": 1,
            "MaxNum": 1,
            "PolicyDetails": [
                {
                    "PolicyType": "abc",
                    "PolicyThreshold": 1
                }
            ],
            "CustomLogs": "abc",
            "EnvParams": "abc",
            "InitialDelaySeconds": 1,
            "CreateTime": "abc",
            "Port": 0,
            "HasDockerfile": true,
            "Dockerfile": "abc",
            "BuildDir": "abc",
            "LogType": "abc",
            "LogSetId": "abc",
            "LogTopicId": "abc",
            "LogParseType": "abc",
            "Tag": "abc"
        },
        "OnlineVersionInfos": [
            {
                "VersionName": "abc",
                "ImageUrl": "abc",
                "FlowRatio": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

