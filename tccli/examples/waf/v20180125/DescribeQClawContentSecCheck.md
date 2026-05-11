**Example 1: 审核toolcall工具调用测试用例**

高危命令

Input: 

```
tccli waf DescribeQClawContentSecCheck --cli-unfold-argument  \
    --ServiceId 3244 \
    --ToolName ex \
    --ToolArgs rm -rf /
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
                    "Score": 1
                }
            ]
        },
        "RequestId": "3c181ddd-5a1d-4740-896c-fa94381f2254"
    }
}
```

**Example 2: 审核内容调用用例**



Input: 

```
tccli waf DescribeQClawContentSecCheck --cli-unfold-argument  \
    --ServiceId 9000000004 \
    --Content.Prompt 跑得比*****续航水分严重
```

Output: 
```
{
    "Response": {
        "Data": {
            "Risks": [
                {
                    "RiskType": "sensitive_content",
                    "RuleId": "grl-safety-brand-strict",
                    "RuleName": "车辆品牌保护",
                    "Score": 1
                }
            ]
        },
        "RequestId": "1a268503-a272-4033-888f-d044e9118ddc"
    }
}
```

