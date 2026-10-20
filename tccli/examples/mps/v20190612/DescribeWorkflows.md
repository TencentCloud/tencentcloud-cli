**Example 1: 查询特定工作流**

查询 ID 为10001的工作流。

Input: 

```
tccli mps DescribeWorkflows --cli-unfold-argument  \
    --WorkflowIds 10001
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "WorkflowInfoSet": [
            {
                "AiAnalysisTask": null,
                "AiContentReviewTask": {
                    "Definition": 10
                },
                "AiRecognitionTask": null,
                "CreateTime": "2024-04-03T08:29:26Z",
                "MediaProcessTask": {
                    "AdaptiveDynamicStreamingTaskSet": [],
                    "AnimatedGraphicTaskSet": [],
                    "ImageSpriteTaskSet": [],
                    "SampleSnapshotTaskSet": [],
                    "SnapshotByTimeOffsetTaskSet": [],
                    "TranscodeTaskSet": []
                },
                "OutputDir": "",
                "OutputStorage": {
                    "CosOutputStorage": {
                        "Bucket": "mpstest-12345567",
                        "Region": "ap-nanjing"
                    },
                    "S3OutputStorage": null,
                    "Type": "COS"
                },
                "Status": "Enabled",
                "TaskNotifyConfig": null,
                "TaskPriority": -10,
                "Trigger": {
                    "AwsS3FileUploadTrigger": null,
                    "CosFileUploadTrigger": {
                        "Bucket": "mpstest-12345567",
                        "Dir": "/mps/",
                        "Formats": [
                            ""
                        ],
                        "Region": "ap-nanjing"
                    },
                    "Type": "CosFileUpload"
                },
                "UpdateTime": "2024-08-05T07:04:30Z",
                "WorkflowId": 10001,
                "WorkflowName": "工作流test"
            }
        ],
        "RequestId": "73054d13-abcdef1-8c28-7ce8698ef8b9"
    }
}
```

