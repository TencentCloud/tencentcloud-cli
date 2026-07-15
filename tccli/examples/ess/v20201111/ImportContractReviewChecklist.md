**Example 1: 常规导入合同风险审查清单**



Input: 

```
tccli ess ImportContractReviewChecklist --cli-unfold-argument  \
    --Operator.UserId yDwf3UUckps8dvypUEfH3DjwIpMfa0uw \
    --Name 测试API创建审查清单 \
    --Categories.0.Name 主体信息审查 \
    --Categories.0.Points.0.Summary 签约方主体信息完整明确 \
    --Categories.0.Points.0.Explanation 审查合同中签约方主体信息是否完善，企业签署方需包括企业名称、统一社会信用代码、法定代表人/经办人的姓名和有效身份证件号。个人签署方需要包括个人姓名和有效身份证件号。 \
    --Categories.0.Points.0.RiskLevel 高风险 \
    --Categories.0.Points.0.IsIndispensable False \
    --Categories.0.Points.0.IsConsistentWithReferenceItem False \
    --Categories.0.Points.0.ReferenceItem 可以参考的条款 \
    --Categories.0.Points.0.Suggestion 固定建议 \
    --Categories.0.Points.0.AiSuggestion AI生成建议 \
    --Categories.0.Points.0.RiskPresentation 身份 \
    --ChecklistID yD3XCUUckpzdumlzUyb9Q4tyW8MppCjy \
    --Enabled True
```

Output: 
```
{
    "Response": {
        "ChecklistId": "yD3XCUUckpzdumlzUyb9Q4tyW8MppCjy",
        "RequestId": "224836f8-22d1-4255-9077-c38f8e314153"
    }
}
```

