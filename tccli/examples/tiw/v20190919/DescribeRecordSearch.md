**Example 1: 成功**



Input: 

```
tccli tiw DescribeRecordSearch --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1 \
    --RoomId 880528
```

Output: 
```
{
    "Response": {
        "RecordTaskSet": [
            {
                "CreateTime": "2020-08-24T21:53:56+08:00",
                "RoomId": 880528,
                "TaskId": "gvft1qbrvs2331tcs1tb",
                "Status": "FINISHED",
                "SdkAppId": 1400127140,
                "Result": {
                    "FinishReason": "USER_CALL",
                    "ExceptionCnt": 0,
                    "RoomId": 880528,
                    "GroupId": "880528",
                    "RecordStartTime": 1598277240,
                    "RecordStopTime": 1598277614,
                    "TotalTime": 368433,
                    "VideoInfos": [
                        {
                            "VideoDuration": 368332,
                            "UserId": "",
                            "VideoSize": 10731806,
                            "VideoUrl": "http://whiteboard-cam-test-1257307760.cos.ap-nanjing.myqcloud.com/video/gvft1qbrvs2331tcs1tb/0cf156ea197a8012073e6b690f44e530.mp4",
                            "VideoType": 2,
                            "VideoPlayTime": 0,
                            "VideoFormat": "mp4",
                            "VideoId": "0cf156ea197a8012073e6b690f44e530",
                            "Width": 1280,
                            "Height": 960
                        },
                        {
                            "VideoDuration": 368325,
                            "UserId": "tic_mixstream_880528_custom",
                            "VideoSize": 12276476,
                            "VideoUrl": "http://whiteboard-cam-test-1257307760.cos.ap-nanjing.myqcloud.com/video/gvft1qbrvs2331tcs1tb/ae62799da16a83ab9eb3da0bb37ef89f.mp4",
                            "VideoType": 3,
                            "VideoPlayTime": 108,
                            "VideoFormat": "mp4",
                            "VideoId": "ae62799da16a83ab9eb3da0bb37ef89f",
                            "Width": 1624,
                            "Height": 1000
                        },
                        {
                            "VideoDuration": 181102,
                            "UserId": "tic_mixstream_880528_101",
                            "VideoSize": 3743450,
                            "VideoUrl": "http://whiteboard-cam-test-1257307760.cos.ap-nanjing.myqcloud.com/video/gvft1qbrvs2331tcs1tb/54797f6b83940a708c7b7aecc2f1d1a9.mp4",
                            "VideoType": 3,
                            "VideoPlayTime": 28918,
                            "VideoFormat": "mp4",
                            "VideoId": "54797f6b83940a708c7b7aecc2f1d1a9",
                            "Width": 496,
                            "Height": 368
                        },
                        {
                            "VideoDuration": 35405,
                            "UserId": "tiw_web_736",
                            "VideoSize": 3001045,
                            "VideoUrl": "http://whiteboard-cam-test-1257307760.cos.ap-nanjing.myqcloud.com/video/gvft1qbrvs2331tcs1tb/7e562e9d513d12a2e03bea1514cc40fc.mp4",
                            "VideoType": 0,
                            "VideoPlayTime": 29475,
                            "VideoFormat": "mp4",
                            "VideoId": "7e562e9d513d12a2e03bea1514cc40fc",
                            "Width": 1280,
                            "Height": 720
                        },
                        {
                            "VideoDuration": 161885,
                            "UserId": "tiw_web_310",
                            "VideoSize": 9974368,
                            "VideoUrl": "http://whiteboard-cam-test-1257307760.cos.ap-nanjing.myqcloud.com/video/gvft1qbrvs2331tcs1tb/9ba564cba92925a02a88ef3ee874b586.mp4",
                            "VideoType": 0,
                            "VideoPlayTime": 47535,
                            "VideoFormat": "mp4",
                            "VideoId": "9ba564cba92925a02a88ef3ee874b586",
                            "Width": 1280,
                            "Height": 720
                        },
                        {
                            "VideoDuration": 6085,
                            "UserId": "tiw_web_736",
                            "VideoSize": 283329,
                            "VideoUrl": "http://whiteboard-cam-test-1257307760.cos.ap-nanjing.myqcloud.com/video/gvft1qbrvs2331tcs1tb/9517ed0696f910865ecaf22a07be4c0f.mp4",
                            "VideoType": 0,
                            "VideoPlayTime": 64903,
                            "VideoFormat": "mp4",
                            "VideoId": "9517ed0696f910865ecaf22a07be4c0f",
                            "Width": 960,
                            "Height": 540
                        },
                        {
                            "VideoDuration": 96787,
                            "UserId": "tiw_web_736",
                            "VideoSize": 5604352,
                            "VideoUrl": "http://whiteboard-cam-test-1257307760.cos.ap-nanjing.myqcloud.com/video/gvft1qbrvs2331tcs1tb/cdda0043fb734600d14324c4364213e2.mp4",
                            "VideoType": 0,
                            "VideoPlayTime": 115401,
                            "VideoFormat": "mp4",
                            "VideoId": "cdda0043fb734600d14324c4364213e2",
                            "Width": 1280,
                            "Height": 720
                        }
                    ],
                    "OmittedDurations": [],
                    "Details": "",
                    "ErrorCode": 0,
                    "ErrorMsg": ""
                }
            }
        ],
        "TotalCount": 151,
        "RequestId": "bc309eaa-6d64-11e8-a7fe-5254000b4175"
    }
}
```

