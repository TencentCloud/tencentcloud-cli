**Example 1: 查询指定应用任务流并按创建时间降序**



Input: 

```
tccli vod DescribeProcedureTemplates --cli-unfold-argument  \
    --SubAppId 221094 \
    --SortBy.0.Field create_time \
    --SortBy.0.Order desc
```

Output: 
```
{
    "Response": {
        "ProcedureTemplateSet": [
            {
                "AiAnalysisTask": null,
                "AiContentReviewTask": null,
                "AiRecognitionTask": null,
                "AiRecognitionTaskSet": [],
                "Comment": "",
                "CreateTime": "2026-05-12T14:58:40+08:00",
                "MediaProcessTask": {
                    "AdaptiveDynamicStreamingTaskSet": [],
                    "AnimatedGraphicTaskSet": [],
                    "CoverBySnapshotTaskSet": [],
                    "ImageSpriteTaskSet": [],
                    "SampleSnapshotTaskSet": [],
                    "SnapshotByTimeOffsetTaskSet": [],
                    "TranscodeTaskSet": [
                        {
                            "BlindWatermark": null,
                            "CopyRightWatermark": {
                                "Text": ""
                            },
                            "Definition": 1140,
                            "EndTimeOffset": 0,
                            "HeadTailSet": [],
                            "MosaicSet": [],
                            "OverrideParameter": null,
                            "StartTimeOffset": 0,
                            "SubtitleInfoSet": [],
                            "TraceWatermark": {
                                "Definition": 0,
                                "Switch": ""
                            },
                            "WatermarkSet": []
                        }
                    ]
                },
                "MiniProgramPublishTask": null,
                "Name": "hy-test2",
                "ReviewAudioVideoTask": null,
                "Type": "Custom",
                "UpdateTime": "2026-05-12T14:58:40+08:00"
            }
        ],
        "TotalCount": 5,
        "RequestId": "884b286f-de85-4065-a5d5-64ce54dfe5bf"
    }
}
```

**Example 2: 查询指定应用全部任务流**



Input: 

```
tccli vod DescribeProcedureTemplates --cli-unfold-argument  \
    --SubAppId 221094
```

Output: 
```
{
    "Response": {
        "ProcedureTemplateSet": [
            {
                "AiAnalysisTask": null,
                "AiContentReviewTask": null,
                "AiRecognitionTask": {
                    "Definition": 70
                },
                "AiRecognitionTaskSet": [],
                "Comment": "",
                "CreateTime": "2019-10-23T20:47:15+08:00",
                "MediaProcessTask": {
                    "AdaptiveDynamicStreamingTaskSet": [],
                    "AnimatedGraphicTaskSet": [],
                    "CoverBySnapshotTaskSet": [],
                    "ImageSpriteTaskSet": [],
                    "SampleSnapshotTaskSet": [],
                    "SnapshotByTimeOffsetTaskSet": [],
                    "TranscodeTaskSet": [
                        {
                            "BlindWatermark": null,
                            "CopyRightWatermark": {
                                "Text": ""
                            },
                            "Definition": 1010,
                            "EndTimeOffset": 0,
                            "HeadTailSet": [],
                            "MosaicSet": [],
                            "OverrideParameter": null,
                            "StartTimeOffset": 0,
                            "SubtitleInfoSet": [],
                            "TraceWatermark": {
                                "Definition": 0,
                                "Switch": ""
                            },
                            "WatermarkSet": []
                        }
                    ]
                },
                "MiniProgramPublishTask": null,
                "Name": "default",
                "ReviewAudioVideoTask": null,
                "Type": "Preset",
                "UpdateTime": "2019-10-23T20:47:15+08:00"
            }
        ],
        "TotalCount": 5,
        "RequestId": "84dc6ce1-df4c-4950-88a4-1d9c4cf96e2d"
    }
}
```

