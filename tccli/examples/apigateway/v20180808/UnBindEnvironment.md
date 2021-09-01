**Example 1: 用于解绑使用计划**



Input: 

```
tccli apigateway UnBindEnvironment --cli-unfold-argument  \
    --BindType SERVICE \
    --Environment test \
    --ServiceId service-ody35h5e \
    --UsagePlanIds usagePlan-quqxvett
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "a6c567f9-7a55-43b9-81d2-f721da5e271a"
    }
}
```

