**Example 1: 查询TOP攻击信息示例**



Input: 

```
tccli csip DescribeTopAttackInfo --cli-unfold-argument  \
    --MemberId mem-tencent-1f94db8d0x231e0
```

Output: 
```
{
    "Response": {
        "TopAttackInfo": [
            {
                "Name": "漏洞攻击",
                "Count": 13
            }
        ],
        "RequestId": "ab168264-2afb-4c51-bfb5-d8e24e0a03ac"
    }
}
```

