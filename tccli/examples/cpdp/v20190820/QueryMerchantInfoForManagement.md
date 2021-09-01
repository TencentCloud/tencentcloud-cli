**Example 1: QueryMerchantInfoForManagement**



Input: 

```
tccli cpdp QueryMerchantInfoForManagement --cli-unfold-argument  \
    --InvoicePlatformId 0 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "CPDP-1585143238239",
        "Result": {
            "Total": 1,
            "List": [
                {}
            ]
        }
    }
}
```

