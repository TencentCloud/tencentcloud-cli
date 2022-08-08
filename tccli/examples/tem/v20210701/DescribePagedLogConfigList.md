**Example 1: 查询分页的日志收集配置列表**

查询分页的日志收集配置列表

Input: 

```
tccli tem DescribePagedLogConfigList --cli-unfold-argument  \
    --EnvironmentId xx
```

Output: 
```
{
    "Response": {
        "Result": {
            "Records": [
                {
                    "ApplicationId": "xx",
                    "ApplicationName": "xx",
                    "TopicId": "xx",
                    "BeginningRegex": "xx",
                    "Name": "xx",
                    "CreateDate": "xx",
                    "LogPath": "xx",
                    "InputType": "container_stdout",
                    "LogType": "xx",
                    "FilePattern": "xx",
                    "ModifyDate": "xx",
                    "LogsetId": "xx"
                }
            ],
            "ContinueToken": "xx"
        },
        "RequestId": "xx"
    }
}
```

