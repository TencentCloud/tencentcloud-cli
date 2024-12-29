**Example 1: 创建配置**

创建配置

Input: 

```
tccli tem CreateConfigData --cli-unfold-argument  \
    --EnvironmentId en-xxxxxx \
    --Name config-name-xxx \
    --SourceChannel 0 \
    --Data.0.Key key-xxx \
    --Data.0.Value val-xxx
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

