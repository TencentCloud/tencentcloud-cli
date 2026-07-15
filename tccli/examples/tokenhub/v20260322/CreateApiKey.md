**Example 1: CreateApiKey**



Input: 

```
tccli tokenhub CreateApiKey --cli-unfold-argument  \
    --ApiKeyName my-api-key \
    --Platform maas \
    --BindType all \
    --Quotas.0.CycleUnit d \
    --Quotas.0.CycleCredits 1000
```

Output: 
```
{
    "Response": {
        "ApiKeyId": "ak-20260609-f294a4aa4e2a7412780914226ad3ffd8",
        "RequestId": "c7fdc4d0-04d5-4c76-a55e-b8528047a782"
    }
}
```

