**Example 1: 成功**



Input: 

```
tccli vdb DescribePriceRenewInstance --cli-unfold-argument  \
    --InstanceId vdb-8x28fw3t \
    --PayPeriod 1
```

Output: 
```
{
    "Response": {
        "Currency": "CNY",
        "OriginalPrice": 111600,
        "Price": 37680,
        "RequestId": "fc0bef64-59b4-4bf6-8211-632204c3cc7f"
    }
}
```

