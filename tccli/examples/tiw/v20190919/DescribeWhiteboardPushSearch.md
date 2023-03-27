**Example 1: 成功**



Input: 

```
tccli tiw DescribeWhiteboardPushSearch --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1 \
    --RoomId 101069223
```

Output: 
```
{
    "Response": {
        "WhiteboardPushTaskSet": [
            {
                "CreateTime": "2021-01-15T12:43:57+08:00",
                "RoomId": 101069223,
                "TaskId": "01bjgeeigsh31f3rh00c",
                "Status": "STOPPED",
                "SdkAppId": 1400313729,
                "PushUserId": "tic_push_user_101069223_107991",
                "Result": {
                    "RoomId": 101069223,
                    "GroupId": "101069223",
                    "FinishReason": "USER_CALL",
                    "ExceptionCnt": 0,
                    "PushStartTime": 1610685839,
                    "PushStopTime": 1610685852,
                    "IMSyncTime": 0,
                    "ErrorCode": 0,
                    "ErrorMsg": ""
                }
            }
        ],
        "TotalCount": 1,
        "RequestId": "d290f1ee-6c54-4b01-90e6-d701748f0851"
    }
}
```

