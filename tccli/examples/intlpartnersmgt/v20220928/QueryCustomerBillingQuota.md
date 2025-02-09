**Example 1: 1**



Input: 

```
tccli intlpartnersmgt QueryCustomerBillingQuota --cli-unfold-argument  \
    --EventId 1 \
    --ComponentName 123
```

Output: 
```
{
    "Response": {
        "Data": {
            "Force": 0,
            "RemainingCredit": 0,
            "RemainingVoucher": 0,
            "TotalCredit": 0
        },
        "RequestId": "xxx"
    }
}
```

**Example 2: QueryCustomerBillingQuota**



Input: 

```
tccli intlpartnersmgt QueryCustomerBillingQuota --cli-unfold-argument  \
    --EventId 123 \
    --ComponentName xx
```

Output: 
```
{
    "Response": {
        "Data": {
            "RemainingCredit": 0.0,
            "RemainingVoucher": 0.0,
            "TotalCredit": 0.0
        },
        "RequestId": "xx"
    }
}
```

**Example 3: QueryCustomerBillingQuota示例**



Input: 

```
tccli intlpartnersmgt QueryCustomerBillingQuota --cli-unfold-argument  \
    --EventId 0 \
    --ComponentName 字符串
```

Output: 
```
{
    "Response": {
        "Data": {
            "RemainingCredit": 0,
            "RemainingVoucher": 0,
            "TotalCredit": 0
        },
        "RequestId": "0117004b-2653-4146-b637-73c05e067172"
    }
}
```

