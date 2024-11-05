**Example 1: 查询日志收集配置详情**

查询日志收集配置详情

Input: 

```
tccli tem DescribeLogConfig --cli-unfold-argument  \
    --EnvironmentId en-xxxxxx \
    --Name abc \
    --ApplicationId app-xxxxxx
```

Output: 
```
{
    "Response": {
        "Result": {
            "Name": "abc",
            "InputType": "abc",
            "LogsetId": "abc",
            "TopicId": "abc",
            "LogType": "abc",
            "BeginningRegex": "abc",
            "LogPath": "abc",
            "FilePattern": "abc",
            "CreateDate": "abc",
            "ModifyDate": "abc",
            "ApplicationId": "abc",
            "ApplicationName": "abc",
            "ExtractRule": {
                "BeginningRegex": "abc",
                "Keys": [
                    "abc"
                ],
                "FilterKeys": [
                    "abc"
                ],
                "FilterRegex": [
                    "abc"
                ],
                "LogRegex": "abc",
                "TimeKey": "abc",
                "TimeFormat": "abc",
                "UnMatchUpload": "abc",
                "UnMatchedKey": "abc",
                "Backtracking": "abc",
                "Delimiter": "abc"
            }
        },
        "RequestId": "abc"
    }
}
```

