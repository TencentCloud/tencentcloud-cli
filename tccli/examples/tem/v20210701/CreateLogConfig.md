**Example 1: 创建日志收集配置**

创建日志收集配置

Input: 

```
tccli tem CreateLogConfig --cli-unfold-argument  \
    --TopicId xx \
    --Name xx \
    --EnvironmentId xx \
    --LogPath xx \
    --InputType xx \
    --LogType xx \
    --FilePattern xx \
    --ApplicationId xx \
    --LogsetId xx \
    --ExtractRule.BeginningRegex xxx \
    --ExtractRule.Keys xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "81f74023-563c-437d-abf7-8139449ef178",
        "Result": true
    }
}
```

