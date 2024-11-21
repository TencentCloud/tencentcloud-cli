**Example 1: 删除应用弹性策略组合**

删除应用弹性策略组合

Input: 

```
tccli tem DeleteApplicationAutoscaler --cli-unfold-argument  \
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
        "RequestId": "ab-xx"
    }
}
```

