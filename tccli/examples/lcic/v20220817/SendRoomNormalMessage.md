**Example 1: 指定用户给房间中发送消息**



Input: 

```
tccli lcic SendRoomNormalMessage --cli-unfold-argument  \
    --SdkAppId 3520371 \
    --RoomId 352320437 \
    --FromAccount 2WqeRoOMJKQqnnL1lILRFHpdFla \
    --MsgBody.0.MsgType TIMTextElem \
    --MsgBody.0.TextMsgContent.Text abc \
    --MsgBody.0.FaceMsgContent.Index 1 \
    --MsgBody.0.FaceMsgContent.Data abc \
    --MsgBody.0.ImageMsgContent.UUID 494d1feab \
    --MsgBody.0.ImageMsgContent.ImageFormat 1 \
    --MsgBody.0.ImageMsgContent.ImageInfoList.0.Type 1 \
    --MsgBody.0.ImageMsgContent.ImageInfoList.0.Size 12033 \
    --MsgBody.0.ImageMsgContent.ImageInfoList.0.Width 2048 \
    --MsgBody.0.ImageMsgContent.ImageInfoList.0.Height 800 \
    --MsgBody.0.ImageMsgContent.ImageInfoList.0.URL https://grg-1258699.cos.ap-shanghai.myqcloud.com/room_messages.png \
    --CloudCustomData abcsd
```

Output: 
```
{
    "Response": {
        "RequestId": "abee5f"
    }
}
```

