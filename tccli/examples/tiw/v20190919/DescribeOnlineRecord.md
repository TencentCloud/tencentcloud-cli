**Example 1: 查询实时录制任务**



Input: 

```
tccli tiw DescribeOnlineRecord --cli-unfold-argument  \
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
        "OmittedDurations": [],
        "RecordStartTime": 1568949369,
        "RecordStopTime": 1568949392,
        "RecordUserId": "tic_record_user_880528_test-01",
        "RequestId": "d290f1ee-6c54-4b01-90e6-d701748f0851",
        "RoomId": 880528,
        "Status": "FINISHED",
        "TaskId": "ghucnligqtgtvk2624mb",
        "TotalTime": 18317,
        "ReplayUrl": "http://replayurl",
        "Interrupts": [],
        "VideoInfos": [
            {
                "UserId": "Mac_trtc_04",
                "VideoDuration": 17969,
                "VideoFormat": "mp4",
                "VideoId": "dace3518e865e76a9e36712c629822ba",
                "VideoPlayTime": 0,
                "VideoSize": 593418,
                "VideoType": 0,
                "Width": 640,
                "Height": 360,
                "VideoUrl": "http://online-recording-1259648581.file.myqcloud.com/00sp43mantgtv4r842mb/d124f518e865e76a9e36712c629822ba.mp4"
            },
            {
                "UserId": "tic_mixstream_880528_101",
                "VideoDuration": 18205,
                "VideoFormat": "mp4",
                "VideoId": "763d1f6b8679c3f17fb118bd37d05c85",
                "VideoPlayTime": 3,
                "VideoSize": 765545,
                "VideoType": 3,
                "Width": 640,
                "Height": 360,
                "VideoUrl": "http://online-recording-1259648581.file.myqcloud.com/00sp43mantgtv4r842mb/763d1f6b86724f51fb118bd37d05c85.mp4"
            },
            {
                "UserId": "tic_mixstream_880528_3",
                "VideoDuration": 18222,
                "VideoFormat": "mp4",
                "VideoId": "1b9623df0516dc7318df89f6e7fffc1e",
                "VideoPlayTime": 95,
                "VideoSize": 402038,
                "VideoType": 3,
                "Width": 640,
                "Height": 360,
                "VideoUrl": "http://online-recording-1259648581.file.myqcloud.com/00sp43mantgtv4r842mb/1b9623df05124f51318df89f6e7fffc1e.mp4"
            },
            {
                "UserId": "",
                "VideoDuration": 17605,
                "VideoFormat": "mp4",
                "VideoId": "a8152f8faa2cfe621dc965a066a5813c",
                "VideoPlayTime": 623,
                "VideoSize": 226337,
                "VideoType": 2,
                "Width": 640,
                "Height": 360,
                "VideoUrl": "http://online-recording-1259648581.file.myqcloud.com/00sp43mantgtv4r842mb/a815224f512cfe621dc965a066a5813c.mp4"
            }
        ]
    }
}
```

**Example 2: 查询录制失败的实时录制任务**



Input: 

```
tccli tiw DescribeOnlineRecord --cli-unfold-argument  \
    --SdkAppId 1400000001 \
    --TaskId ghucnligqtgtvk2624mb
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.Record",
            "Message": "code: 40004, msg: 2019-09-23 10:31:47, im login failed with code 6206, desc serSig expired\n"
        },
        "RequestId": "d290f1ee-6c54-4b01-90e6-d701748f0851"
    }
}
```

