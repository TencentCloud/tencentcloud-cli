**Example 1: Resetting transcoding rule**

This example shows you how to reset the transcoding rule whose workflow ID is 2573 to add a watermark to the transcoding output.

Input: 

```
tccli mps ResetWorkflow --cli-unfold-argument  \
    --WorkflowId 2573\
    --WorkflowName trans-20-30-40\
    --Trigger.Type CosFileUpload\
    --Trigger.CosFileUploadTrigger.Bucket TopRankVideo-125xxx88\
    --Trigger.CosFileUploadTrigger.Region ap-chongqing\
    --Trigger.CosFileUploadTrigger.Dir /movie/201907/\
    --MediaProcessTask.TranscodeTaskSet.0.Definition 20\
    --MediaProcessTask.WatermarkSet.0.Definition 12580\
    --MediaProcessTask.TranscodeTaskSet.1.Definition 30\
    --MediaProcessTask.TranscodeTaskSet.2.Definition 40
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3"
    }
}
```

