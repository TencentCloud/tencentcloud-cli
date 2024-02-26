**Example 1: 示例**

示例

Input: 

```
tccli lcic GetRooms --cli-unfold-argument  \
    --SdkAppId 1 \
    --StartTime 1 \
    --EndTime 1 \
    --Page 1 \
    --Limit 1 \
    --Status 0 1 2 3
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Rooms": [
            {
                "Name": "abc",
                "RoomId": 1,
                "Status": 1,
                "StartTime": 1,
                "EndTime": 1,
                "RealStartTime": 1,
                "RealEndTime": 1,
                "Resolution": 1,
                "MaxRTCMember": 1,
                "ReplayUrl": "abc",
                "RecordUrl": "abc",
                "MaxMicNumber": 1,
                "EnableDirectControl": 1,
                "InteractionMode": 0,
                "VideoOrientation": 0,
                "IsGradingRequiredPostClass": 0,
                "RoomType": 0,
                "EndDelayTime": 0,
                "LiveType": 1,
                "RecordLiveUrl": "abc",
                "EnableAutoStart": 1,
                "RecordBackground": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

