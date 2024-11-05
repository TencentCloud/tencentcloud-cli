**Example 1: 关闭应用弹性策略组合**

关闭应用弹性策略组合

Input: 

```
tccli tem DisableApplicationAutoscaler --cli-unfold-argument  \
    --ApplicationId app-xxxxxx \
    --SourceChannel 0 \
    --EnvironmentId en-xxxxxx \
    --AutoscalerId scaler-xxxxxx
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "ab-xxxxx"
    }
}
```

