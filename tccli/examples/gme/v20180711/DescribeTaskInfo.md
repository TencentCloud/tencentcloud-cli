**Example 1: 查询录制taskid**

查询录制taskid

Input: 

```
tccli gme DescribeTaskInfo --cli-unfold-argument  \
    --RoomId 9832 \
    --BizId 3400352518
```

Output: 
```
{
    "Response": {
        "SubscribeRecordUserIds": {
            "SubscribeUserIds": [
                3342
            ],
            "UnSubscribeUserIds": [
                7619
            ]
        },
        "RecordMode": 1,
        "RequestId": "h9167d24-a2c6-1125-a5bd-5c023ba721c2",
        "TaskId": 446192236330927912
    }
}
```

