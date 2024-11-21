**Example 1: 查询分页的日志收集配置列表**

查询分页的日志收集配置列表

Input: 

```
tccli tem DescribePagedLogConfigList --cli-unfold-argument  \
    --EnvironmentId en-xxxxxx \
    --ApplicationId app-xxxxxx \
    --ApplicationName abc \
    --Name abc \
    --Limit 0 \
    --ContinueToken some-token-value
```

Output: 
```
{
    "Response": {
        "RequestId": "0793bb3c-6de8-4816-9ab0-5f006cf7656c",
        "Result": {
            "ContinueToken": "",
            "Records": [
                {
                    "ApplicationId": "app-5vaz8x85",
                    "ApplicationName": "app0925",
                    "BeginningRegex": "",
                    "CreateDate": "2024-10-31T15:25:07.000+08:00",
                    "ExtractRule": {
                        "Backtracking": "",
                        "BeginningRegex": "",
                        "Delimiter": "",
                        "FilterKeys": [],
                        "FilterRegex": [],
                        "Keys": [],
                        "LogRegex": "",
                        "TimeFormat": "",
                        "TimeKey": "",
                        "UnMatchUpload": "true",
                        "UnMatchedKey": "LogParseFailure"
                    },
                    "FilePattern": "",
                    "InputType": "container_stdout",
                    "LogPath": "",
                    "LogType": "",
                    "LogsetId": "7a126551-62d1-4e12-b426-84bd5b2fdbca",
                    "ModifyDate": "2024-10-31T15:25:08.000+08:00",
                    "Name": "test",
                    "TopicId": "6c69fdb7-5e4c-4e52-8437-32c2c729b85a"
                }
            ]
        }
    }
}
```

