**Example 1: 查询Top5的攻击域名**



Input: 

```
tccli waf DescribeTopAttackDomain --cli-unfold-argument  \
    --FromTime 2024-11-03 00:00:00 \
    --ToTime 2024-11-03 15:17:00
```

Output: 
```
{
    "Response": {
        "CC": [],
        "Web": [],
        "RequestId": "a4010dd1-d24b-43f5-bab4-8a6b204835b7"
    }
}
```

