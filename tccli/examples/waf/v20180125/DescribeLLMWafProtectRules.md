**Example 1: 查询提示词注入**



Input: 

```
tccli waf DescribeLLMWafProtectRules --cli-unfold-argument  \
    --ServiceId 9000002874 \
    --InstanceId waf_2l15d14809yfq9sf \
    --RuleType prompt_injection
```

Output: 
```
{
    "Response": {
        "Categories": [
            {
                "Category": "prompt_injection",
                "Count": 4,
                "Rules": [
                    {
                        "Action": "log",
                        "Description": "检测用户输入中试图覆盖或篡改系统指令的攻击行为",
                        "DesensitizeSample": "",
                        "RuleId": "grl-safety-prompt-001",
                        "RuleName": "指令覆盖检测",
                        "Severity": "critical",
                        "Status": 1
                    }
                ]
            }
        ],
        "RequestId": "9f0960eb-a57f-43bf-8ac0-69cbc49ac924"
    }
}
```

