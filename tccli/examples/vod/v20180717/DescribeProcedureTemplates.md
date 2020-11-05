**Example 1: Querying all task flow templates**

This example shows you how to query the details of all task flow templates (3 templates are queried).

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
                "Name": "My task flow A",
                "Type": "Custom",
                "MediaPrcoessTask": {
                    "TranscodeTaskSet": [
                        {
                            "Definition": 20,
                            "WatermarkSet": null
                        },
                        {
                            "Definition": 30,
                            "WatermarkSet": null
                        },
                        {
                            "Definition": 40,
                            "WatermarkSet": null
                        }
                    ],
                    "AnimatedGraphicTaskSet": null,
                    "SnapshotByTimeOffsetTaskSet": null,
                    "SampleSnapshotTaskSet": null,
                    "ImageSpriteTaskSet": null,
                    "CoverBySnapshotTaskSet": null
                },
                "AiContentReviewTask": null,
                "AiAnalysisTask": null,
                "AiRecognitionTask": null,
                "MiniProgramPublishTask": null
            },
            {
                "Name": "My task flow B",
                "Type": "Custom",
                "MediaPrcoessTask": {
                    "TranscodeTaskSet": [
                        {
                            "Definition": 20,
                            "WatermarkSet": [
                                {
                                    "Definition": 15780,
                                    "TextContent": null
                                }
                            ]
                        },
                        {
                            "Definition": 30,
                            "WatermarkSet": [
                                {
                                    "Definition": 15780,
                                    "TextContent": null
                                }
                            ]
                        },
                        {
                            "Definition": 40,
                            "WatermarkSet": [
                                {
                                    "Definition": 15780,
                                    "TextContent": null
                                }
                            ]
                        }
                    ],
                    "AnimatedGraphicTaskSet": null,
                    "SnapshotByTimeOffsetTaskSet": null,
                    "SampleSnapshotTaskSet": null,
                    "ImageSpriteTaskSet": null,
                    "CoverBySnapshotTaskSet": null
                },
                "AiContentReviewTask": null,
                "AiAnalysisTask": null,
                "AiRecognitionTask": null,
                "MiniProgramPublishTask": null
            },
            {
                "Name": "My task flow C",
                "Type": "Custom",
                "MediaPrcoessTask": null,
                "AiContentReviewTask": {
                    "Definition": 10
                },
                "AiAnalysisTask": null,
                "AiRecognitionTask": null,
                "MiniProgramPublishTask": null
            }
        ],
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3"
    }
}
```

**Example 2: Querying a specified task flow template**

This example shows you how to query the details of the task flow template named "My task flow A".

Input: 

```
tccli vod DescribeProcedureTemplates --cli-unfold-argument  \
    --Names 'My task flow A'
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ProcedureTemplateSet": [
            {
                "Name": "My task flow A",
                "Type": "Custom",
                "MediaPrcoessTask": {
                    "TranscodeTaskSet": [
                        {
                            "Definition": 20,
                            "WatermarkSet": null
                        },
                        {
                            "Definition": 30,
                            "WatermarkSet": null
                        },
                        {
                            "Definition": 40,
                            "WatermarkSet": null
                        }
                    ],
                    "AnimatedGraphicTaskSet": null,
                    "SnapshotByTimeOffsetTaskSet": null,
                    "SampleSnapshotTaskSet": null,
                    "ImageSpriteTaskSet": null,
                    "CoverBySnapshotTaskSet": null
                },
                "AiContentReviewTask": null,
                "AiAnalysisTask": null,
                "AiRecognitionTask": null,
                "MiniProgramPublishTask": null
            }
        ],
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3"
    }
}
```

