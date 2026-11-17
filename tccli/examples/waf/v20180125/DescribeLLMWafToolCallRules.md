**Example 1: 测试用例**



Input: 

```
tccli waf DescribeLLMWafToolCallRules --cli-unfold-argument  \
    --ServiceId 9000002874 \
    --InstanceId waf_2l15d14809yfq9sf
```

Output: 
```
{
    "Response": {
        "Categories": [
            {
                "Category": "dangerous_ops",
                "Count": 9,
                "Rules": [
                    {
                        "Action": "log",
                        "Description": "拦截 rm -rf、mkfs、dd、shutdown、reboot 等破坏性系统命令",
                        "DesensitizeSample": "",
                        "RuleId": "gtc-baseline-001",
                        "RuleName": "高危系统命令工具阻断",
                        "Severity": "critical",
                        "Status": 1
                    }
                ]
            }
        ],
        "RequestId": "e757752d-8e32-4521-b701-d9204aadd6de"
    }
}
```

