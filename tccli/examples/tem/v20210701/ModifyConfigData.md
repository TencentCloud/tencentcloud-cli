**Example 1: 编辑配置**

编辑配置

Input: 

```
tccli tem ModifyConfigData --cli-unfold-argument  \
    --EnvironmentId en-xxxxxx \
    --Name config-test \
    --SourceChannel 0 \
    --Data.0.Key key-xxx \
    --Data.0.Value val-xxx \
    --Data.0.Type  \
    --Data.0.Config  \
    --Data.0.Secret 
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

