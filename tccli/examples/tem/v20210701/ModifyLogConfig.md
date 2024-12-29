**Example 1: 编辑日志收集配置**

编辑日志收集配置

Input: 

```
tccli tem ModifyLogConfig --cli-unfold-argument  \
    --EnvironmentId en-xxxxxx \
    --Name name-xxx \
    --Data.LogsetId 7a126551-62d1-4e12-b426-84bd5b2fdbca \
    --Data.TopicId 6c69fdb7-5e4c-4e52-8437-32c2c729b85a \
    --Data.InputType container_stdout \
    --Data.LogType json_log \
    --Data.ExtractRule.UnMatchUpload true \
    --Data.ExtractRule.UnMatchedKey LogParseFailure \
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

