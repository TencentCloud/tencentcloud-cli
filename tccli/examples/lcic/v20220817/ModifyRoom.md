**Example 1: 修改房间**

修改房间参数示例

Input: 

```
tccli lcic ModifyRoom --cli-unfold-argument  \
    --RoomId 1 \
    --StartTime 1 \
    --EndTime 1 \
    --TeacherId abc \
    --Name abc \
    --Resolution 1 \
    --MaxMicNumber 1 \
    --AutoMic 1 \
    --AudioQuality 1 \
    --SubType abc \
    --DisableRecord 1 \
    --Assistants abc \
    --SdkAppId 1 \
    --GroupId abc \
    --EnableDirectControl 1
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

