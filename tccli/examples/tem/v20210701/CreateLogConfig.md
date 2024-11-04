**Example 1: 创建日志收集配置**

创建日志收集配置

Input: 

```
tccli tem CreateLogConfig --cli-unfold-argument  \
    --EnvironmentId en-xxxxxx \
    --ApplicationId app-xxxxxx \
    --Name abc \
    --LogsetId abc-xxx \
    --TopicId abc-xxxxx \
    --InputType container_stdout \
    --LogType json_log \
    --BeginningRegex abc \
    --LogPath /abc \
    --FilePattern abc \
    --ExtractRule.BeginningRegex abc \
    --ExtractRule.Keys abc \
    --ExtractRule.FilterKeys abc \
    --ExtractRule.FilterRegex abc \
    --ExtractRule.LogRegex abc \
    --ExtractRule.TimeKey abc \
    --ExtractRule.TimeFormat abc \
    --ExtractRule.UnMatchUpload abc \
    --ExtractRule.UnMatchedKey abc \
    --ExtractRule.Backtracking abc \
    --ExtractRule.Delimiter abc
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

