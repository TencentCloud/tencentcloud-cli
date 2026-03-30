**Example 1: 审核测试用例**

高危命令

Input: 

```
tccli waf DescribeQClawContentSecCheck --cli-unfold-argument  \
    --ServiceId sdfsfs \
    --Content.Prompt rm -rf / *** \
    --UserId sd \
    --SessionId sdf
```

Output: 
```
{
    "Response": {
        "Data": {
            "Risks": [
                {
                    "RiskType": "tool_call",
                    "RuleId": "gtc-baseline-001",
                    "RuleName": "高危系统命令工具阻断",
                    "Score": 0.99
                }
            ]
        },
        "RequestId": "f4a85fb0-28a8-43f0-a5ac-e0a1232346cb"
    }
}
```

