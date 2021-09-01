**Example 1: UnBindIPStrategy**



Input: 

```
tccli apigateway UnBindIPStrategy --cli-unfold-argument  \
    --StrategyId IPStrategy-0ez0c8to \
    --EnvironmentName test \
    --ServiceId service-ody35h5e \
    --UnBindApiIds api-e92i2jds
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "6754bb8e-c421-472e-aa27-ce3a6aae0c26"
    }
}
```

