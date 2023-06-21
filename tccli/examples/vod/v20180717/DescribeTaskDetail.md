**Example 1: 获取任务详情-Procedure**

获取任务详情-任务流

Input: 

```
tccli vod DescribeTaskDetail --cli-unfold-argument  \
    --TaskId 12567683xx-Procedure-633031cd8293ef29d39251ea751b69f2t0
```

Output: 
```
{
    "Response": {
        "TaskType": "Procedure",
        "Status": "FINISH",
        "CreateTime": "2019-02-21T08:27:42Z",
        "BeginProcessTime": "2019-02-21T08:27:43Z",
        "FinishTime": "2019-02-21T08:27:44Z",
        "ProcedureTask": {
            "TaskId": "12567683xx-Procedure-2e1af2456351812be963e309cc133403t0",
            "Status": "FINISH",
            "ErrCode": 0,
            "Message": "",
            "SessionContext": "",
            "SessionId": "",
            "Operator": "",
            "OperationType": "",
            "FileId": "5285890784246869930",
            "FileName": "small",
            "FileUrl": "http://12567683xx.vod2.myqcloud.com/1c1ae5d2vodgzp12567683xx/c643347c5285890784246869930/AtUCmy6gmIYA.mp4",
            "MetaData": {
                "AudioDuration": 59.9900016784668,
                "Md5": "",
                "AudioStreamSet": [
                    {
                        "Bitrate": 383854,
                        "Codec": "aac",
                        "SamplingRate": 48000
                    }
                ],
                "Bitrate": 1021028,
                "Container": "mov,mp4,m4a,3gp,3g2,mj2",
                "Duration": 60,
                "Height": 480,
                "Rotate": 0,
                "Size": 7700180,
                "VideoDuration": 60,
                "VideoStreamSet": [
                    {
                        "Bitrate": 637174,
                        "Codec": "h264",
                        "Fps": 23,
                        "Height": 480,
                        "Width": 640,
                        "DynamicRangeInfo": {}
                    }
                ],
                "Width": 640
            },
            "MediaProcessResultSet": [],
            "AiContentReviewResultSet": [],
            "AiRecognitionResultSet": [],
            "AiAnalysisResultSet": [],
            "TasksPriority": 0,
            "TasksNotifyMode": ""
        },
        "ComposeMediaTask": null,
        "SplitMediaTask": null,
        "WechatMiniProgramPublishTask": null,
        "EditMediaTask": null,
        "WechatPublishTask": null,
        "TranscodeTask": null,
        "SnapshotByTimeOffsetTask": null,
        "ConcatTask": null,
        "ClipTask": null,
        "CreateImageSpriteTask": null,
        "PullUploadTask": null,
        "RemoveWatermarkTask": null,
        "ReviewAudioVideoTask": null,
        "ReduceMediaBitrateTask": null,
        "ExtractTraceWatermarkTask": null,
        "ExtractCopyRightWatermarkTask": null,
        "DescribeFileAttributesTask": null,
        "RebuildMediaTask": null,
        "QualityInspectTask": null,
        "RequestId": "sdfadf"
    }
}
```

**Example 2: 获取任务详情-Transcode**

获取任务详情-转码

Input: 

```
tccli vod DescribeTaskDetail --cli-unfold-argument  \
    --TaskId 12567683xx-transcode-58a1bc57b1c23ed1079597ec17a47666t0
```

Output: 
```
{
    "Response": {
        "TaskType": "Transcode",
        "Status": "FINISH",
        "CreateTime": "2019-01-22T06:50:31Z",
        "BeginProcessTime": "2019-01-22T06:50:32Z",
        "FinishTime": "2019-01-22T06:50:45Z",
        "ProcedureTask": null,
        "EditMediaTask": null,
        "TranscodeTask": {
            "TaskId": "12567683xx-transcode-58a1bc57b1c23ed1079597ec17a47666t0",
            "ErrCode": 0,
            "Message": "",
            "FileId": "5285890784246869930",
            "FileName": "small",
            "Duration": 60,
            "CoverUrl": "http://12567683xx.vod2.myqcloud.com/d042887avodtransgzp12567683xx/c643347c5285890784246869930/1546950643_4191274987.100_0.jpg",
            "PlayInfoSet": [
                {
                    "Url": "http://12567683xx.vod2.myqcloud.com/1c1ae5d2vodgzp12567683xx/c643347c5285890784246869930/AtUCmy6gmIYA.mp4",
                    "Definition": 0,
                    "Bitrate": 1021028,
                    "Height": 480,
                    "Width": 640
                },
                {
                    "Url": "http://12567683xx.vod2.myqcloud.com/d042887avodtransgzp12567683xx/c643347c5285890784246869930/v.f10.mp4",
                    "Definition": 10,
                    "Bitrate": 304695,
                    "Height": 240,
                    "Width": 320
                }
            ]
        },
        "ComposeMediaTask": null,
        "WechatMiniProgramPublishTask": null,
        "SplitMediaTask": null,
        "SnapshotByTimeOffsetTask": null,
        "WechatPublishTask": null,
        "ConcatTask": null,
        "ClipTask": null,
        "CreateImageSpriteTask": null,
        "PullUploadTask": null,
        "RemoveWatermarkTask": null,
        "ReviewAudioVideoTask": null,
        "ReduceMediaBitrateTask": null,
        "ExtractTraceWatermarkTask": null,
        "ExtractCopyRightWatermarkTask": null,
        "DescribeFileAttributesTask": null,
        "RebuildMediaTask": null,
        "QualityInspectTask": null,
        "RequestId": "62597d15-3fad-4234-af1a-ed33602a6118"
    }
}
```

**Example 3: 获取任务详情-EditMedia**

获取任务详情-编辑视频

Input: 

```
tccli vod DescribeTaskDetail --cli-unfold-argument  \
    --TaskId 12530394xx-procedurev2-61c975da05662fd9d3bf9d89a63361c0t0
```

Output: 
```
{
    "Response": {
        "TaskType": "EditMedia",
        "Status": "FINISH",
        "CreateTime": "2019-02-25T10:56:02Z",
        "BeginProcessTime": "2019-02-25T10:56:02Z",
        "FinishTime": "2019-02-25T10:56:13Z",
        "ProcedureTask": null,
        "EditMediaTask": {
            "TaskId": "12530394xx-procedurev2-61c975da05662fd9d3bf9d89a63361c0t0",
            "Status": "FINISH",
            "ErrCode": 0,
            "Message": "",
            "Input": {
                "InputType": "Stream",
                "FileInfoSet": [
                    {
                        "FileId": "4565514956192708397",
                        "StartTimeOffset": 0,
                        "EndTimeOffset": 30
                    },
                    {
                        "FileId": "4565514956192708396",
                        "StartTimeOffset": 0,
                        "EndTimeOffset": 30
                    }
                ],
                "StreamInfoSet": [
                    {
                        "StreamId": "29920_stream",
                        "StartTime": "2019-02-20T06:21:00Z",
                        "EndTime": "2019-02-20T06:21:30Z"
                    }
                ]
            },
            "Output": {
                "FileType": "mp4",
                "FileId": "4565514956222184986",
                "FileUrl": "http://12530394xx.vod2.myqcloud.com/9395476dvodcq1253039488/f0e1f8314565514956222184986/playlist.f9.mp4"
            },
            "ProcedureTaskId": ""
        },
        "ComposeMediaTask": null,
        "SplitMediaTask": null,
        "WechatMiniProgramPublishTask": null,
        "WechatPublishTask": null,
        "TranscodeTask": null,
        "SnapshotByTimeOffsetTask": null,
        "ConcatTask": null,
        "ClipTask": null,
        "CreateImageSpriteTask": null,
        "PullUploadTask": null,
        "RemoveWatermarkTask": null,
        "ReviewAudioVideoTask": null,
        "ReduceMediaBitrateTask": null,
        "ExtractTraceWatermarkTask": null,
        "ExtractCopyRightWatermarkTask": null,
        "DescribeFileAttributesTask": null,
        "RebuildMediaTask": null,
        "QualityInspectTask": null,
        "RequestId": "sdfadf"
    }
}
```

**Example 4: 获取任务详情-WechatMiniProgramPublish**

获取任务详情-微信小程序发布

Input: 

```
tccli vod DescribeTaskDetail --cli-unfold-argument  \
    --TaskId 1253339xxx-wechat-mini-program-publish-e576984516ec3b3c8e49753adf6b0688t0
```

Output: 
```
{
    "Response": {
        "TaskType": "WechatMiniProgramPublish",
        "Status": "FINISH",
        "CreateTime": "2019-06-23T13:04:42Z",
        "BeginProcessTime": "2019-06-23T13:04:42Z",
        "FinishTime": "2019-06-23T13:04:53Z",
        "ProcedureTask": null,
        "EditMediaTask": null,
        "ComposeMediaTask": null,
        "WechatPublishTask": null,
        "PullUploadTask": null,
        "WechatMiniProgramPublishTask": {
            "TaskId": "1253339xxx-wechat-mini-program-publish-e576984516ec3b3c8e49753adf6b0688t0",
            "Status": "FINISH",
            "ErrCode": 0,
            "Message": "",
            "FileId": "5285890789444337543",
            "SourceDefinition": 0,
            "PublishResult": "Pass"
        },
        "SplitMediaTask": null,
        "TranscodeTask": null,
        "SnapshotByTimeOffsetTask": null,
        "ConcatTask": null,
        "ClipTask": null,
        "CreateImageSpriteTask": null,
        "RemoveWatermarkTask": null,
        "ReviewAudioVideoTask": null,
        "ReduceMediaBitrateTask": null,
        "ExtractTraceWatermarkTask": null,
        "ExtractCopyRightWatermarkTask": null,
        "DescribeFileAttributesTask": null,
        "RebuildMediaTask": null,
        "QualityInspectTask": null,
        "RequestId": "04db7d25-f590-414a-a341-8f1584f15f84"
    }
}
```

