**Example 1: 查询AIGC任务详情**



Input: 

```
tccli live DescribeAIGCTaskStatus --cli-unfold-argument  \
    --TaskId ff08e8bb-b378-****-40ee-83ba685f8fdd
```

Output: 
```
{
    "Response": {
        "CreateTime": "2026-03-19 10:59:08",
        "FinishedTime": "2026-03-19 10:59:09",
        "OutputUrl": "https://********************.cos.ap-guangzhou.myqcloud.com/acc08f31-1449-bd0d-fec1-6912c1d2db9a_0.png",
        "ScheduledTime": "2026-03-19 10:59:09",
        "TaskId": "ff08e8bb-b378-****-40ee-83ba685f8fdd",
        "TaskResultCode": -401,
        "TaskResultMsg": "Invalid Para",
        "TaskStatus": "FAILED",
        "RequestId": "4aa73c85-8159-4911-87d7-32852738f9af"
    }
}
```

