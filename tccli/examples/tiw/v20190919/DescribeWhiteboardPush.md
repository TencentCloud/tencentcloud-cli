**Example 1: 查询白板推流任务**



Input: 

```
tccli tiw DescribeWhiteboardPush --cli-unfold-argument  \
    --SdkAppId 1400000001 \
    --TaskId ghucnligqtgtvk2624mb
```

Output: 
```
{
    "Response": {
        "ExceptionCnt": 0,
        "FinishReason": "USER_CALL",
        "GroupId": "880528",
        "IMSyncTime": 0,
        "PushStartTime": 1610591726,
        "PushStopTime": 1610591759,
        "PushUserId": "tic_push_user_880528_test1",
        "RequestId": "d290f1ee-6c54-4b01-90e6-d701748f0851",
        "RoomId": 880528,
        "Status": "STOPPED",
        "Backup": "",
        "TaskId": "g42lfmu5uc3lpoqrqvvb"
    }
}
```

**Example 2: 查询推流失败的白板推流任务**



Input: 

```
tccli tiw DescribeWhiteboardPush --cli-unfold-argument  \
    --SdkAppId 1400000001 \
    --TaskId ghucnligqtgtvk2624mb
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.WhiteboardPush",
            "Message": "code: 40006, msg: 2021-01-13 22:34:42, TRTC onError, code: -70003, msg: The UserSig in use is illegal. Please regenerate UserSig through official API. (FYI: https://cloud.tencent.com/document/product/269/32688 )\n"
        },
        "RequestId": "d290f1ee-6c54-4b01-90e6-d701748f0851"
    }
}
```

