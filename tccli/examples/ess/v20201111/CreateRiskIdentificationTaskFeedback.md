**Example 1: 创建合同审查任务反馈**



Input: 

```
tccli ess CreateRiskIdentificationTaskFeedback --cli-unfold-argument  \
    --RiskId yDtzlUUckpfqqvp9Uxx \
    --FeedbackResult 2 \
    --Reason 审查不准确 \
    --Operator.UserId yDwqbUUckp3o2rzmUxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "s1763618858585513085"
    }
}
```

