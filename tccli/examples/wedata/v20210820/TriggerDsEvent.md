**Example 1: 触发事件**

触发事件

Input: 

```
tccli wedata TriggerDsEvent --cli-unfold-argument  \
    --ProjectId abc \
    --EventCaseList.0.CaseId abc \
    --EventCaseList.0.Name abc \
    --EventCaseList.0.Dimension abc \
    --EventCaseList.0.CreationTs abc \
    --EventCaseList.0.ConsumerId abc \
    --EventCaseList.0.Description abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 0,
            "SuccessCount": 0,
            "FailCount": 0,
            "FailMessageList": [
                {
                    "Key": "abc",
                    "ErrorMessage": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

