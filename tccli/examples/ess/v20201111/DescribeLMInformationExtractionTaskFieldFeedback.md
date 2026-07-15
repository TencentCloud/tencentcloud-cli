**Example 1: 查询合同智能提取任务字段反馈**



Input: 

```
tccli ess DescribeLMInformationExtractionTaskFieldFeedback --cli-unfold-argument  \
    --TaskId yDtzNUUckpf2nfh6UEcTcQVvNxxx \
    --Operator.UserId yDwqbUUckp3o2rzmUxHsV0xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "s1763690910938836088",
        "SubTaskFeedbackList": [
            {
                "FeedbackList": [
                    {
                        "Id": "yDtzNUUckpf2nfh7UEcTcQVCcnmxgiuu",
                        "Info": {
                            "Reason": {
                                "ReasonContent": "",
                                "ReasonType": 0
                            },
                            "Result": 0
                        }
                    }
                ],
                "SubTaskId": "yDtzNUUckpf2nfheUEcTcQVydamvsAeY"
            }
        ],
        "TaskId": "yDtzNUUckpf2nfh6UEcTcQVvNViPazOG"
    }
}
```

