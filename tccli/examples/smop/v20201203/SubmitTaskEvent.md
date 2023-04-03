**Example 1: SubmitTaskEvent**

提交任务事件

Input: 

```
tccli smop SubmitTaskEvent --cli-unfold-argument  \
    --AccountId abc \
    --DeviceId abc \
    --OrderId abc \
    --Code abc \
    --Async 0 \
    --NotifyURL abc \
    --ProductId 0
```

Output: 
```
{
    "Response": {
        "OrderId": "abc",
        "Code": 0,
        "Message": "abc",
        "Data": [
            {
                "Code": 0,
                "Message": "abc",
                "TaskId": 0,
                "TaskOrderId": "abc",
                "TaskCode": 0,
                "TaskCoinNumber": 0,
                "TaskType": 0,
                "TotalCoin": 0,
                "Attach": "abc",
                "DoneTimes": 0,
                "TotalTimes": 0,
                "TaskName": "abc",
                "GrowScore": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

