**Example 1: 查询日志收集配置详情**

查询日志收集配置详情

Input: 

```
tccli tem DescribeLogConfig --cli-unfold-argument  \
    --EnvironmentId en-xxxxxx \
    --Name log-name-xxx \
    --ApplicationId app-xxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "e6fedfb8-1bc9-414d-b69b-5e24fdda6416",
        "Result": {
            "Name": "log-name-xxx",
            "ApplicationName": "app-name-xxx",
            "ApplicationId": "",
            "InputType": "container_stdout",
            "TopicId": "3ae33b64-d3d1-4a2c-96ff-a2e044dcexxx",
            "LogsetId": "5bf3beeb-1f64-40f9-9672-b596248d7xxx",
            "LogType": "minimalist_log",
            "BeginningRegex": "",
            "ExtractRule": {
                "Backtracking": "-1",
                "BeginningRegex": "",
                "Delimiter": "",
                "FilterKeys": [],
                "FilterRegex": [],
                "Keys": [],
                "LogRegex": "",
                "TimeFormat": "",
                "TimeKey": "",
                "UnMatchUpload": "false",
                "UnMatchedKey": ""
            },
            "LogPath": "",
            "FilePattern": "",
            "CreateDate": "2022-05-28T18:02:55.000+08:00",
            "ModifyDate": "2022-05-28T18:02:56.000+08:00"
        }
    }
}
```

