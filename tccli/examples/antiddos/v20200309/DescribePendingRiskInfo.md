**Example 1: 查询账号维度待处理风险信息**

查询账号维度待处理风险信息

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
        "RequestId": "0506d138-ef0f-4ff4-83b0-f1d85e740afd",
        "Total": 146,
        "BlockingCount": 2
    }
}
```

