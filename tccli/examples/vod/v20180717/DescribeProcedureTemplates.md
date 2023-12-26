**Example 1: 查询指定任务流模板**

查询名为“我的任务流A”的任务流模板的详情

Input: 

```
tccli vod DescribeProcedureTemplates --cli-unfold-argument  \
    --Names 我的任务流A
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ProcedureTemplateSet": [
            {
                "Name": "我的任务流A",
                "Type": "Custom",
                "Comment": "我的任务流A",
                "UpdateTime": "2018-10-01T18:00:00",
                "CreateTime": "2018-10-01T18:00:00",
                "MediaProcessTask": {
                    "TranscodeTaskSet": [
                        {
                            "Definition": 20,
                            "WatermarkSet": [],
                            "MosaicSet": [],
                            "TraceWatermark": {
                                "Switch": "OFF",
                                "Definition": 0
                            },
                            "StartTimeOffset": 0,
                            "CopyRightWatermark": {
                                "Text": ""
                            },
                            "HeadTailSet": [],
                            "EndTimeOffset": 0
                        },
                        {
                            "Definition": 30,
                            "WatermarkSet": [],
                            "MosaicSet": [],
                            "TraceWatermark": {
                                "Switch": "OFF",
                                "Definition": 0
                            },
                            "StartTimeOffset": 0,
                            "CopyRightWatermark": {
                                "Text": ""
                            },
                            "HeadTailSet": [],
                            "EndTimeOffset": 0
                        },
                        {
                            "Definition": 40,
                            "WatermarkSet": [],
                            "MosaicSet": [],
                            "TraceWatermark": {
                                "Switch": "OFF",
                                "Definition": 0
                            },
                            "StartTimeOffset": 0,
                            "CopyRightWatermark": {
                                "Text": ""
                            },
                            "HeadTailSet": [],
                            "EndTimeOffset": 0
                        }
                    ],
                    "AnimatedGraphicTaskSet": [],
                    "SnapshotByTimeOffsetTaskSet": [],
                    "SampleSnapshotTaskSet": [],
                    "ImageSpriteTaskSet": [],
                    "CoverBySnapshotTaskSet": []
                },
                "AiContentReviewTask": null,
                "AiAnalysisTask": null,
                "AiRecognitionTask": null,
                "MiniProgramPublishTask": null,
                "ReviewAudioVideoTask": null
            }
        ],
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3"
    }
}
```

**Example 2: 查询所有的任务流模板**

查询所有的任务流模板的详情，共查到3个任务流模板

Input: 

```
tccli vod DescribeProcedureTemplates --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 3,
        "ProcedureTemplateSet": [
            {
                "Name": "我的任务流A",
                "Type": "Custom",
                "Comment": "我的任务流A",
                "UpdateTime": "2018-10-01T18:00:00",
                "CreateTime": "2018-10-01T18:00:00",
                "MediaProcessTask": {
                    "TranscodeTaskSet": [
                        {
                            "Definition": 20,
                            "WatermarkSet": [],
                            "MosaicSet": [],
                            "TraceWatermark": {
                                "Switch": "OFF",
                                "Definition": 0
                            },
                            "StartTimeOffset": 0,
                            "CopyRightWatermark": {
                                "Text": ""
                            },
                            "HeadTailSet": [],
                            "EndTimeOffset": 0
                        },
                        {
                            "Definition": 30,
                            "WatermarkSet": [],
                            "MosaicSet": [],
                            "TraceWatermark": {
                                "Switch": "OFF",
                                "Definition": 0
                            },
                            "StartTimeOffset": 0,
                            "CopyRightWatermark": {
                                "Text": ""
                            },
                            "HeadTailSet": [],
                            "EndTimeOffset": 0
                        },
                        {
                            "Definition": 40,
                            "WatermarkSet": [],
                            "MosaicSet": [],
                            "TraceWatermark": {
                                "Switch": "OFF",
                                "Definition": 0
                            },
                            "StartTimeOffset": 0,
                            "CopyRightWatermark": {
                                "Text": ""
                            },
                            "HeadTailSet": [],
                            "EndTimeOffset": 0
                        }
                    ],
                    "AnimatedGraphicTaskSet": [],
                    "SnapshotByTimeOffsetTaskSet": [],
                    "SampleSnapshotTaskSet": [],
                    "ImageSpriteTaskSet": [],
                    "CoverBySnapshotTaskSet": []
                },
                "AiContentReviewTask": null,
                "AiAnalysisTask": null,
                "AiRecognitionTask": null,
                "MiniProgramPublishTask": null,
                "ReviewAudioVideoTask": null
            },
            {
                "Name": "我的任务流B",
                "Type": "Custom",
                "Comment": "我的任务流B",
                "UpdateTime": "2018-10-01T18:00:00",
                "CreateTime": "2018-10-01T18:00:00",
                "MediaProcessTask": {
                    "TranscodeTaskSet": [
                        {
                            "Definition": 20,
                            "WatermarkSet": [],
                            "MosaicSet": [],
                            "TraceWatermark": {
                                "Switch": "OFF",
                                "Definition": 0
                            },
                            "StartTimeOffset": 0,
                            "CopyRightWatermark": {
                                "Text": ""
                            },
                            "HeadTailSet": [],
                            "EndTimeOffset": 0
                        },
                        {
                            "Definition": 30,
                            "WatermarkSet": [],
                            "MosaicSet": [],
                            "TraceWatermark": {
                                "Switch": "OFF",
                                "Definition": 0
                            },
                            "StartTimeOffset": 0,
                            "CopyRightWatermark": {
                                "Text": ""
                            },
                            "HeadTailSet": [],
                            "EndTimeOffset": 0
                        },
                        {
                            "Definition": 40,
                            "WatermarkSet": [],
                            "MosaicSet": [],
                            "TraceWatermark": {
                                "Switch": "OFF",
                                "Definition": 0
                            },
                            "StartTimeOffset": 0,
                            "CopyRightWatermark": {
                                "Text": ""
                            },
                            "HeadTailSet": [],
                            "EndTimeOffset": 0
                        }
                    ],
                    "AnimatedGraphicTaskSet": [],
                    "SnapshotByTimeOffsetTaskSet": [],
                    "SampleSnapshotTaskSet": [],
                    "ImageSpriteTaskSet": [],
                    "CoverBySnapshotTaskSet": []
                },
                "AiContentReviewTask": null,
                "AiAnalysisTask": null,
                "AiRecognitionTask": null,
                "MiniProgramPublishTask": null,
                "ReviewAudioVideoTask": null
            },
            {
                "Name": "我的任务流C",
                "Type": "Custom",
                "Comment": "我的任务流C",
                "UpdateTime": "2018-10-01T18:00:00",
                "CreateTime": "2018-10-01T18:00:00",
                "MediaProcessTask": null,
                "AiContentReviewTask": {
                    "Definition": 10
                },
                "AiAnalysisTask": null,
                "AiRecognitionTask": null,
                "MiniProgramPublishTask": null,
                "ReviewAudioVideoTask": null
            }
        ],
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3"
    }
}
```

