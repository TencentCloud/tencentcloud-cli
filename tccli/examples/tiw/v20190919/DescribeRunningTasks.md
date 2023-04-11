**Example 1: 获取当前正在执行的白板推流任务列表**

通过接口获取当前应用白板推流任务类型的正在执行中的任务列表

Input: 

```
tccli tiw DescribeRunningTasks --cli-unfold-argument  \
    --SdkAppID 1400000001 \
    --TaskType WhiteboardPush
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Tasks": [
            {
                "TaskID": "bj0mt2l23osdj300hl31",
                "TaskType": "WhiteboardPush",
                "CreateTime": "2023-03-14 15:00:00",
                "CancelTime": "",
                "Status": "PROCESSING",
                "Progress": 11,
                "RoomID": 12345,
                "FileURL": "",
                "SdkAppID": 1400000001
            }
        ],
        "RequestId": "d290f1ee-6c54-4b01-90e6-d701748f0851"
    }
}
```

