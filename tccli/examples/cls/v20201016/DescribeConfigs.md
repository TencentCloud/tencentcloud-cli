**Example 1: 获取采集配置**



Input: 

```
tccli cls DescribeConfigs --cli-unfold-argument  \
    --Filters.0.Key configId \
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
                "ConfigId": "xxxx-xx-xx-xx-yyyyyyyy",
                "Path": "/abc/log/test.log",
                "LogType": "delimiter_log",
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
                            "Key": "xx",
                            "Regex": "xxxx"
                        }
                    ],
                    "UnMatchLogKey": "testlog",
                    "UnMatchUpLoadSwitch": true,
                    "Backtracking": -1
                },
                "UserDefineRule": "xxxx",
                "UpdateTime": "2017-08-08 12:12:12",
                "CreateTime": "2017-08-08 12:12:12"
            }
        ],
        "TotalCount": 1,
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

