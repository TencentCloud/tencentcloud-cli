**Example 1: 示例**

修改类型

Input: 

```
tccli lcic ModifyRoom --cli-unfold-argument  \
    --RoomId 368760996 \
    --SdkAppId 3520371 \
    --InteractionMode 0 \
    --VideoOrientation 0 \
    --IsGradingRequiredPostClass 1 \
    --RoomType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "50034c8f-cd77-43f2-815e-afe990fb023d"
    }
}
```

**Example 2: 修改房间**

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

