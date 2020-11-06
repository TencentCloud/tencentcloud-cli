**Example 1: Starting real-time recording**



Input: 

```
tccli tiw StartOnlineRecord --cli-unfold-argument  \
    --SdkAppId 1400000001 \
    --RoomId 1203 \
    --RecordUserId tic_record_user_1203_141551 \
    --RecordUserSig usersig_of_<tic_record_user_1203_141551>
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "TaskId": "bj0mt2l23osdj300hl30"
    }
}
```

**Example 2: Starting real-time mixed stream recording**

This example shows you how to use a built-in mixed stream layout for mixed stream recording.

Input: 

```
tccli tiw StartOnlineRecord --cli-unfold-argument  \
    --SdkAppId 1400000001 \
    --RoomId 1203 \
    --RecordUserId tic_record_user_1203_141551 \
    --RecordUserSig usersig_of_<tic_record_user_1203_141551> \
    --Whiteboard.Width 1280 \
    --Whiteboard.Height 960 \
    --Whiteboard.InitParam {"ratio":"16:9"} \
    --Concat.Enabled true \
    --Concat.Image http://background/image.jpg \
    --MixStream.Enabled true \
    --MixStream.DisableAudio false \
    --MixStream.ModelId 2 \
    --MixStream.TeacherId teacher \
    --Extras MIX_STREAM
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "TaskId": "bj0mt2l23osdj300hl30"
    }
}
```

