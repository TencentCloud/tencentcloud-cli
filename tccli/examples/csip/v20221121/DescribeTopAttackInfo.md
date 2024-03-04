**Example 1: 查询TOP攻击信息示例**



Input: 

```
tccli csip DescribeTopAttackInfo --cli-unfold-argument  \
    --OperatedMemberId abc
```

Output: 
```
{
    "Response": {
        "TopAttackInfo": [
            {
                "Name": "漏洞攻击",
                "Count": 123
            }
        ],
        "RequestId": "abc"
    }
}
```

