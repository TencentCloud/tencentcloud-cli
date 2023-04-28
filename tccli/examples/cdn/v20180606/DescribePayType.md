**Example 1: 计费方式查询**

计费方式查询

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
        "CurrentPayType": "flux"
    }
}
```

