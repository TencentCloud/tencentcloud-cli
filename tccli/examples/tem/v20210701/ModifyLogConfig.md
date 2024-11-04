**Example 1: 编辑日志收集配置**

编辑日志收集配置

Input: 

```
tccli tem ModifyLogConfig --cli-unfold-argument  \
    --EnvironmentId en-xxxxxx \
    --Name abc \
    --Data.Name abc \
    --Data.InputType abc \
    --Data.LogsetId abc \
    --Data.TopicId abc \
    --Data.LogType abc \
    --Data.BeginningRegex abc \
    --Data.LogPath abc \
    --Data.FilePattern abc \
    --Data.CreateDate abc \
    --Data.ModifyDate abc \
    --Data.ApplicationId abc \
    --Data.ApplicationName abc \
    --Data.ExtractRule.BeginningRegex abc \
    --Data.ExtractRule.Keys abc \
    --Data.ExtractRule.FilterKeys abc \
    --Data.ExtractRule.FilterRegex abc \
    --Data.ExtractRule.LogRegex abc \
    --Data.ExtractRule.TimeKey abc \
    --Data.ExtractRule.TimeFormat abc \
    --Data.ExtractRule.UnMatchUpload abc \
    --Data.ExtractRule.UnMatchedKey abc \
    --Data.ExtractRule.Backtracking abc \
    --Data.ExtractRule.Delimiter abc \
    --ApplicationId app-xxxxxx
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

