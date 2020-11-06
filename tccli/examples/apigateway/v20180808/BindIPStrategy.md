**Example 1: BindIPStrategy**



Input: 

```
tccli apigateway BindIPStrategy --cli-unfold-argument  \
    --StrategyId IPStrategy-0ez0c8to \
    --EnvironmentName test \
    --ServiceId service-ody35h5e \
    --BindApiIds api-e92i2jds
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "bb85842c-c0d2-4543-8f4d-396a193babe8"
    }
}
```

