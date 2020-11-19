**Example 1: 查询特定工作流**

查询 ID 为78459的工作流。

Input: 

```
tccli mps DescribeWorkflows --cli-unfold-argument  \
    --WorkflowIds 78459
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TotalCount": 1,
        "WorkflowInfoSet": [
            {
                "WorkflowId": 78459,
                "WorkflowName": "transcode-10",
                "Status": "Enabled",
                "Trigger": {
                    "Type": "CosFileUpload",
                    "CosFileUploadTrigger": {
                        "Bucket": "TopRankVideo-125xxx88",
                        "Region": "ap-chongqing",
                        "Dir": "/movie/201907/"
                    }
                },
                "OutputStorage": {
                    "Type": "COS",
                    "CosOutputStorage": {
                        "Bucket": "TopRankVideo-125xxx88",
                        "Region": "ap-chongqing"
                    }
                },
                "MediaProcessTask": {
                    "TranscodeTaskSet": [
                        {
                            "Definition": 10,
                            "WatermarkSet": []
                        }
                    ]
                },
                "OutputDir": "/movie/201907/",
                "AiContentReviewTask": null,
                "AiRecognitionTask": null,
                "AiAnalysisTask": null,
                "TaskNotifyConfig": null,
                "TaskPriority": 0,
                "CreateTime": "2019-07-18T10:00:00Z",
                "UpdateTime": "2019-07-18T11:00:03Z"
            }
        ]
    }
}
```

