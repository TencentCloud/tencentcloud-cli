**Example 1: 查询日志收集配置详情**

查询日志收集配置详情

Input: 

```
tccli tem DescribeLogConfig --cli-unfold-argument  \
    --EnvironmentId xx \
    --Name xx
```

Output: 
```
{
    "Response": {
        "Result": {
            "ApplicationName": "xx",
            "TopicId": "xx",
            "BeginningRegex": "xx",
            "Name": "xx",
            "CreateDate": "xx",
            "LogPath": "xx",
            "InputType": "xx",
            "LogType": "xx",
            "FilePattern": "xx",
            "ModifyDate": "xx",
            "ApplicationId": "xx",
            "LogsetId": "xx"
        },
        "RequestId": "xx"
    }
}
```

