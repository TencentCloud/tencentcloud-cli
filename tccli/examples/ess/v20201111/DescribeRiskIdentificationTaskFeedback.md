**Example 1: 查询合同审查任务反馈信息**



Input: 

```
tccli ess DescribeRiskIdentificationTaskFeedback --cli-unfold-argument  \
    --TaskId yDtzlUUckpfqqv89Ux7RXxxx \
    --Operator.UserId yDwqbUUckp3o2rzmUxHsV0xxx
```

Output: 
```
{
    "Response": {
        "FeedbackList": [
            {
                "FeedbackResult": 0,
                "Reason": "",
                "RiskId": "yDtzlUUckpfqqvn7Ux7RX5xxx"
            },
            {
                "FeedbackResult": 2,
                "Reason": "审查不准确",
                "RiskId": "yDtzlUUckpfqqvp9Uxxx"
            }
        ],
        "RequestId": "676edecf-3176-4c29-a235-a58f233a6265"
    }
}
```

