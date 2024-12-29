**Example 1: 创建日志收集配置**

创建日志收集配置

Input: 

```
tccli tem CreateLogConfig --cli-unfold-argument  \
    --EnvironmentId en-dpxydze5 \
    --ApplicationId app-5vaz8x85 \
    --LogsetId 7a126551-62d1-4e12-b426-84bd5b2fdbca \
    --TopicId 6c69fdb7-5e4c-4e52-8437-32c2c729b85a \
    --InputType container_stdout \
    --LogType json_log \
    --Name log-cfg-xxx \
    --ExtractRule.UnMatchUpload true \
    --ExtractRule.UnMatchedKey LogParseFailure
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

