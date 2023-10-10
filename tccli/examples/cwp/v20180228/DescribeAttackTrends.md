**Example 1: 网络攻击趋势数据**

网络攻击趋势数据

Input: 

```
tccli cwp DescribeAttackTrends --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "NetAttackTrend": [
            {
                "AttackCount": 2,
                "DateTime": "2023-05-22",
                "SuccAttackCount": 0,
                "TryAttackCount": 2
            }
        ],
        "RequestId": "8a9ca170-ea5d-4bcf-b8f6-5d9d68cb15c1"
    }
}
```

