**Example 1: 查询账号维度待处理风险信息**



Input: 

```
tccli antiddos DescribePendingRiskInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ExpiredCount": 144,
        "IsPaidUsr": true,
        "AttackingCount": 0,
        "RequestId": "xx",
        "Total": 146,
        "BlockingCount": 2
    }
}
```

