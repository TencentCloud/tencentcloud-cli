**Example 1: 查询绑定任务进度**



Input: 

```
tccli csip DescribeCSIPLicenseBindSchedule --cli-unfold-argument  \
    --TaskId 7505
```

Output: 
```
{
    "Response": {
        "FailedList": [],
        "FailedNum": 0,
        "List": [
            {
                "ErrMsg": "",
                "FixMessage": "",
                "Quuid": "ins-****5j4c",
                "Status": 1
            }
        ],
        "Schedule": 100,
        "Status": "DONE",
        "SuccessNum": 1,
        "TaskId": 7505,
        "Total": 1,
        "RequestId": "7ffffd25-06bb-42f9-98df-5edfddbd5e7b"
    }
}
```

