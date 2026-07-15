**Example 1: 常规获取合同审查清单**



Input: 

```
tccli ess DescribeContractReviewChecklist --cli-unfold-argument  \
    --Operator.UserId yDwf3UUckps8dvypUEfH3DjwIpMfa0uw \
    --ChecklistId yD3XCUUckpzdumlzUyb9Q4tyW8MppCjy
```

Output: 
```
{
    "Response": {
        "Categories": [
            {
                "Name": "主体信息审查",
                "Points": [
                    {
                        "AiSuggestion": "AI生成建议",
                        "Explanation": "审查合同中签约方主体信息是否完善，企业签署方需包括企业名称、统一社会信用代码、法定代表人/经办人的姓名和有效身份证件号。个人签署方需要包括个人姓名和有效身份证件号。",
                        "Id": "yD3XCUUckpzdumleUyb9Q4tvHLnQFX0c",
                        "IsConsistentWithReferenceItem": false,
                        "IsIndispensable": false,
                        "ReferenceItem": "可以参考的条款",
                        "RiskLevel": "高风险",
                        "RiskPresentation": [
                            "身份"
                        ],
                        "Suggestion": "固定建议",
                        "Summary": "签约方主体信息完整明确"
                    }
                ]
            }
        ],
        "ChecklistId": "yD3XCUUckpzdumlzUyb9Q4tyW8MppCjy",
        "Enabled": true,
        "Name": "测试API创建审查清单",
        "RequestId": "cdfa675b-509a-4337-82e9-4ed9482f4498"
    }
}
```

