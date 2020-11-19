**Example 1: 重设转码规则**

重设工作流 ID 为2573的转码规则，转码输出加上水印。

Input: 

```
tccli mps ResetWorkflow --cli-unfold-argument  \
    --WorkflowId 2573 \
    --WorkflowName trans-100020-100030-100040 \
    --Trigger.Type CosFileUpload \
    --Trigger.CosFileUploadTrigger.Bucket TopRankVideo-125xxx88 \
    --Trigger.CosFileUploadTrigger.Region ap-chongqing \
    --Trigger.CosFileUploadTrigger.Dir /movie/201907/ \
    --MediaProcessTask.TranscodeTaskSet.0.Definition 100020 \
    --MediaProcessTask.TranscodeTaskSet.0.WatermarkSet.0.Definition 12580 \
    --MediaProcessTask.TranscodeTaskSet.1.Definition 100030 \
    --MediaProcessTask.TranscodeTaskSet.1.WatermarkSet.0.Definition 12580 \
    --MediaProcessTask.TranscodeTaskSet.2.Definition 100040 \
    --MediaProcessTask.TranscodeTaskSet.2.WatermarkSet.0.Definition 12580
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3"
    }
}
```

