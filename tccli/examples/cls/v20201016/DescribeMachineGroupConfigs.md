**Example 1: 获取机器组绑定的采集规则配置**



Input: 

```
tccli cls DescribeMachineGroupConfigs --cli-unfold-argument  \
    --GroupId xxxxx-xxx-xxxxx
```

Output: 
```
{
    "Response": {
        "Configs": [
            {
                "ConfigId": "xxxx-xx-xx-xx-yyyyyyyy",
                "Name": "testname",
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
                    "UnMatchUpLoadSwitch": true
                },
                "UpdateTime": "2017-08-08 12:12:12",
                "CreateTime": "2017-08-08 12:12:12"
            }
        ],
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

