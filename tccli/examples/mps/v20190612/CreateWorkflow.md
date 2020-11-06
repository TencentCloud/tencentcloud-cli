**Example 1: Setting transcoding rule**

This example shows you how to set a transcoding rule named "trans-20-30-40" for the `TopRankVideo-125xxx88` bucket to output in three formats of 20, 30, and 40.

Input: 

```
tccli mps CreateWorkflow --cli-unfold-argument  \
    --WorkflowName trans-20-30-40 \
    --Trigger.Type CosFileUpload \
    --Trigger.CosFileUploadTrigger.Bucket TopRankVideo-125xxx88 \
    --Trigger.CosFileUploadTrigger.Region ap-chongqing \
    --Trigger.CosFileUploadTrigger.Dir /movie/201907/ \
    --MediaProcessTask.TranscodeTaskSet.0.Definition 20 \
    --MediaProcessTask.TranscodeTaskSet.1.Definition 30 \
    --MediaProcessTask.TranscodeTaskSet.2.Definition 40
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "WorkflowId": 157482
    }
}
```

**Example 2: Setting sampled screencapturing rule**

This example shows you how to set a transcoding rule named "snapshot" for the `TopRankVideo-125xxx88` bucket to output in the specification of 10.

Input: 

```
tccli mps CreateWorkflow --cli-unfold-argument  \
    --WorkflowName snapshot \
    --Trigger.Type CosFileUpload \
    --Trigger.CosFileUploadTrigger.Bucket TopRankVideo-125xxx88 \
    --Trigger.CosFileUploadTrigger.Region ap-chongqing \
    --Trigger.CosFileUploadTrigger.Dir /movie/201907/ \
    --MediaProcessTask.SampleSnapshotTaskSet.0.Definition 10
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "WorkflowId": 3457482
    }
}
```

