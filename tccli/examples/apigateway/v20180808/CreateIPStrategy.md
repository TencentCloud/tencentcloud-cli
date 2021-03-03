**Example 1: CreateIPStrategy**



Input: 

```
tccli apigateway CreateIPStrategy --cli-unfold-argument  \
    --ServiceId service-ody35h5e \
    --StrategyName xx \
    --StrategyType WHITE \
    --StrategyData 1.1.1.1\n2.2.2.2
```

Output: 
```
{
    "Response": {
        "Result": {
            "ServiceId": "service-ody35h5e",
            "StrategyId": "IPStrategy-4xj4r1ou",
            "StrategyName": "xx",
            "StrategyType": "WHITE",
            "StrategyData": "1.1.1.1\n2.2.2.2",
            "CreatedTime": "2020-02-24T19:02:00Z",
            "ModifiedTime": "2020-02-24T19:02:00Z",
            "BindApiTotalCount": null,
            "BindApis": null
        },
        "RequestId": "4336cff4-1d75-433b-8823-bcf8fa8773c6"
    }
}
```

