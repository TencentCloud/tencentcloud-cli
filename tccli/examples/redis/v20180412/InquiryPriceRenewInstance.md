**Example 1: 查询示例**

查询续费价格

Input: 

```
tccli redis InquiryPriceRenewInstance --cli-unfold-argument  \
    --Period 1 \
    --InstanceId crs-qkdj****
```

Output: 
```
{
    "Response": {
        "Price": 100800,
        "HighPrecisionPrice": 100800.98,
        "Currency": "CNY",
        "AmountUnit": "pent",
        "RequestId": "4bd77cc7-ece7-4660-bbdd-6892d96f35a1"
    }
}
```

