**Example 1: 获取特殊采集配置**



Input: 

```
tccli cls DescribeConfigExtras --cli-unfold-argument  \
    --Filters.0.Key configExtraId \
    --Filters.0.Values xxxx-xxx-xxxx \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Configs": [
            {
                "ConfigExtraId": "xxxx-xx-xx-xx-yyyyyyy1",
                "Name": "testname",
                "TopicId": "xxxxxx-xxx-xxxxxx",
                "Type": "host_file",
                "HostFile": {
                    "LogPath": "/var/log/tmep",
                    "FilePattern": "*.log",
                    "CustomLabels": [
                        "key1=value1",
                        "key=value2"
                    ]
                },
                "LogType": "minimalist_log",
                "ExtractRule": {
                    "TimeKey": "date",
                    "TimeFormat": "%Y-%m-%d %H:%M:%S",
                    "Delimiter": "|",
                    "LogRegex": ".*",
                    "BeginRegex": "^",
                    "Keys": [
                        "date",
                        "",
                        "content"
                    ],
                    "FilterKeyRegex": [
                        {
                            "Key": "xxx",
                            "Regex": "ssss"
                        }
                    ],
                    "UnMatchLogKey": "testlog",
                    "UnMatchUpLoadSwitch": true,
                    "Backtracking": -1
                },
                "ExcludePaths": [
                    {
                        "Type": "xx",
                        "Value": "xx"
                    }
                ],
                "UserDefineRule": "xxxxxx",
                "UpdateTime": "2017-08-08 12:12:12",
                "CreateTime": "2017-08-08 12:12:12"
            }
        ],
        "TotalCount": 1,
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

