**Example 1: 获取采集配置**



Input: 

```
tccli cls DescribeAgentConfigs --cli-unfold-argument  \
    --AgentVersion 1.0 \
    --AgentIp 10.10.1.119 \
    --Labels label
```

Output: 
```
{
    "Response": {
        "LogConfigs": [
            {
                "LogsetId": "logset-***",
                "Path": "/var/***",
                "GroupIds": [
                    "group-****"
                ],
                "ConfigId": "config-*****",
                "LogFormat": "**",
                "LogType": "**",
                "ExtractRule": {
                    "LogRegex": "**",
                    "Keys": [
                        "content"
                    ],
                    "FilterKeyRegex": [
                        {
                            "Regex": "**",
                            "Key": "**"
                        }
                    ],
                    "TimeKey": "**",
                    "BeginRegex": "**",
                    "Delimiter": "**",
                    "TimeFormat": "**",
                    "UnMatchUpLoadSwitch": true,
                    "UnMatchLogKey": "testlog",
                    "Backtracking": 1048576,
                    "MetadataType": 1,
                    "Protocol": "***",
                    "JsonStandard": 1,
                    "IsGBK": 1,
                    "Address": "**",
                    "ParseProtocol": "**",
                    "MetaTags": [
                        {
                            "Key": "**",
                            "Value": "**"
                        }
                    ],
                    "PathRegex": "**"
                },
                "ExcludePaths": [
                    {
                        "Type": "**",
                        "Value": "*****"
                    }
                ],
                "TopicId": "x**",
                "UserDefineRule": "x***"
            }
        ],
        "ServiceLogConfigs": [
            {}
        ],
        "URL": "****",
        "NeedUpdate": true,
        "FileMd5": "****",
        "LastVersion": "****",
        "RequestId": "****"
    }
}
```

