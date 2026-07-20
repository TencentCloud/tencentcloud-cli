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
                "LogFormat": "xx",
                "LogType": "xx",
                "ExtractRule": {
                    "LogRegex": "xx",
                    "Keys": [
                        "content"
                    ],
                    "FilterKeyRegex": [
                        {
                            "Regex": "xx",
                            "Key": "xx"
                        }
                    ],
                    "TimeKey": "xx",
                    "BeginRegex": "xx",
                    "Delimiter": "xx",
                    "TimeFormat": "xx",
                    "UnMatchUpLoadSwitch": true,
                    "UnMatchLogKey": "testlog",
                    "Backtracking": 1048576
                },
                "ExcludePaths": [
                    {
                        "Type": "xx",
                        "Value": "xxxxxxx"
                    }
                ],
                "TopicId": "xx",
                "UserDefineRule": "xxxx"
            },
            {
                "TopicId": "xx",
                "LogFormat": "xx",
                "ExtractRule": {
                    "TimeKey": "xx",
                    "Keys": [
                        "content"
                    ],
                    "FilterKeyRegex": [
                        {
                            "Key": "xx",
                            "Regex": "xx"
                        }
                    ],
                    "LogRegex": "xx",
                    "BeginRegex": "xx",
                    "Delimiter": "xx",
                    "TimeFormat": "xx"
                },
                "ExcludePaths": [
                    {
                        "Type": "xx",
                        "Value": "xxxxxxx"
                    }
                ],
                "LogType": "xx",
                "UserDefineRule": "xxxx"
            }
        ],
        "ServiceLogConfigs": [
            {},
            {}
        ],
        "URL": "xx",
        "NeedUpdate": true,
        "FileMd5": "xx",
        "LastVersion": "xx",
        "RequestId": "xx"
    }
}
```

