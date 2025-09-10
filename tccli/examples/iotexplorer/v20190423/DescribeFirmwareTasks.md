**Example 1: 查询固件升级任务列表**



Input: 

```
tccli iotexplorer DescribeFirmwareTasks --cli-unfold-argument  \
    --ProductID I6KTCZ170U \
    --FirmwareVersion t.1 \
    --Offset 0 \
    --Limit 3
```

Output: 
```
{
    "Response": {
        "RequestId": "baffed26-d55b-41bd-a8b3-5c0377cd45d2",
        "TaskInfos": [
            {
                "CreateTime": 1599293298,
                "Status": 5,
                "TaskId": 1000698,
                "Type": 1
            },
            {
                "CreateTime": 1599293285,
                "Status": 5,
                "TaskId": 1000697,
                "Type": 1
            },
            {
                "CreateTime": 1599293158,
                "Status": 5,
                "TaskId": 1000696,
                "Type": 1
            }
        ],
        "Total": 6
    }
}
```

