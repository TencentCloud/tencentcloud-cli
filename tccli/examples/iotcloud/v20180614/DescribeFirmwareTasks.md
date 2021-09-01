**Example 1: 查询固件升级任务列表**



Input: 

```
tccli iotcloud DescribeFirmwareTasks --cli-unfold-argument  \
    --ProductID ABCDE12345 \
    --FirmwareVersion 1.0.0 \
    --Offset 1 \
    --Limit 5
```

Output: 
```
{
    "Response": {
        "Total": 53,
        "TaskInfos": [
            {
                "TaskId": 1000175,
                "Status": 3,
                "CreateTime": 1589466879,
                "Type": 1
            },
            {
                "TaskId": 1000176,
                "Status": 3,
                "CreateTime": 1589467049,
                "Type": 1
            },
            {
                "Status": 3,
                "CreateTime": 1589467138,
                "Type": 1,
                "TaskId": 1000179
            },
            {
                "TaskId": 1000180,
                "Status": 3,
                "CreateTime": 1589467139,
                "Type": 1
            },
            {
                "Type": 1,
                "TaskId": 1000182,
                "Status": 3,
                "CreateTime": 1589467141
            }
        ],
        "RequestId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
}
```

