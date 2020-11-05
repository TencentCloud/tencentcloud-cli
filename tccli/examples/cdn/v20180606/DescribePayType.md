**Example 1: Querying your billing method**



Input: 

```
tccli cdn DescribePayType --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "1732a0dd-48d8-4ff1-8dcb-7f04ca139825",
        "PayType": "flux",
        "StatType": "sum",
        "BillingCycle": "day",
        "RegionType": "all",
        "CurrentPayType": "flux",
        "IsVip": 0
    }
}
```

