**Example 1: Querying the specified workflow**

This example shows you how to query the workflow whose ID is 78459.

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
                "MediaOutputInfo": null,
                "MediaProcessTask": {
                    "TranscodeTaskSet": [
                        {
                            "Definition": 10,
                            "WatermarkSet": [],
                            "MediaOutputInfo": null
                        }
                    ]
                },
                "AiContentReviewTask": null,
                "AiRecognitionTask": null,
                "TaskNotifyConfig": null,
                "TaskPriority": 0,
                "CreateTime": "2019-07-18T10:00:00Z",
                "UpdateTime": "2019-07-18T11:00:03Z"
            }
        ]
    }
}
```

