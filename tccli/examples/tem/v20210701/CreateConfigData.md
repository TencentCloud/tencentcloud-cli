**Example 1: 创建配置**

创建配置

Input: 

```
tccli tem CreateConfigData --cli-unfold-argument  \
    --EnvironmentId en-xxxxxx \
    --Name abc \
    --SourceChannel 0 \
    --Data.0.Key abc \
    --Data.0.Value abc \
    --Data.0.Type abc \
    --Data.0.Config abc \
    --Data.0.Secret abc
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

