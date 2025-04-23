**Example 1: 启用应用弹性策略组合**

启用应用弹性策略组合

Input: 

```
tccli tem EnableApplicationAutoscaler --cli-unfold-argument  \
    --ApplicationId app-xxxxxx \
    --SourceChannel 0 \
    --EnvironmentId en-xxx \
    --AutoscalerId scaler-xxxxxx
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "abc-xxx-xxx-xxx"
    }
}
```

