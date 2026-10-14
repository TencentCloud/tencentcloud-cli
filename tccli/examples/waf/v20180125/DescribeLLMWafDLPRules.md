**Example 1: 查询规则列表**



Input: 

```
tccli waf DescribeLLMWafDLPRules --cli-unfold-argument  \
    --ServiceId 9000002874 \
    --InstanceId waf_2l15d14809yfq9sf
```

Output: 
```
{
    "Response": {
        "Rules": [
            {
                "Action": "deny",
                "Description": "检测银行卡号，覆盖借记卡与信用卡（13-19位数字）",
                "DesensitizeSample": "****1234",
                "Direction": 1,
                "RuleId": "gdl-001",
                "RuleName": "银行卡",
                "Severity": "high",
                "Status": 1
            }
        ],
        "RequestId": "aa87bb50-22c3-4bd8-b734-c583abfdb4a5"
    }
}
```

