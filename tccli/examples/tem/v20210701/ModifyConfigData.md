**Example 1: 编辑配置**

编辑配置

Input: 

```
tccli tem ModifyConfigData --cli-unfold-argument  \
    --EnvironmentId xx \
    --Data.0.Value xx \
    --Data.0.Key xx \
    --Name xx \
    --SourceChannel 0
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

