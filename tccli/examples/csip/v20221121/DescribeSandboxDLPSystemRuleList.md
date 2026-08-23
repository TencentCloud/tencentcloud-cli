**Example 1: 查询 DLP 系统规则列表示例**



Input: 

```
tccli csip DescribeSandboxDLPSystemRuleList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "ID": 3001,
                "RuleName": "身份证号识别",
                "RuleContent": "[1-9]\\d{5}(19|20)\\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\\d|3[01])\\d{3}[0-9Xx]"
            }
        ],
        "TotalCount": 28,
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    }
}
```

