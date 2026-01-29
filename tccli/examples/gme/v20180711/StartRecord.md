**Example 1: 开始录制**

开启录制

Input: 

```
tccli gme StartRecord --cli-unfold-argument  \
    --RecordMode 1 \
    --SubscribeRecordUserIds.SubscribeUserIds 10086 \
    --SubscribeRecordUserIds.UnSubscribeUserIds 10087 \
    --RoomId 1987 \
    --BizId 3400352518
```

Output: 
```
{
    "Response": {
        "TaskId": 446192236330927940,
        "RequestId": "h9167d24-a2c6-1125-a5bd-5c023ba721c2"
    }
}
```

