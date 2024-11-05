**Example 1: SubmitTaskEvent**

提交任务事件

Input: 

```
tccli smop SubmitTaskEvent --cli-unfold-argument  \
    --AccountId 5Gsl****VfPd \
    --DeviceId oPD5****G0zr \
    --OrderId xFUDBDgn4lv403u5 \
    --Code addType \
    --Async 1 \
    --NotifyURL https://gmall.m.qq.com/api/ReceiveTaskNotify \
    --ProductId 7999
```

Output: 
```
{
    "Response": {
        "OrderId": "xFUDBDgn4lv403u5",
        "Code": 0,
        "Message": "success",
        "Data": [
            {
                "Code": 0,
                "Message": "success",
                "TaskId": 11100,
                "TaskOrderId": "3772179646188093549",
                "TaskCode": 1,
                "TaskCoinNumber": 10,
                "TaskType": 1151,
                "TotalCoin": 100,
                "Attach": "自定义数据说明",
                "DoneTimes": 1,
                "TotalTimes": 3,
                "TaskName": "自定义任务",
                "GrowScore": 100
            }
        ],
        "RequestId": "afc7e79d-b282-154e-5389-f5a6592d2408"
    }
}
```

