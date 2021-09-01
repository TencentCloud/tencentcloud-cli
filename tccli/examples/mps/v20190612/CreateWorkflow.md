**Example 1: 设置转码规则**

对名为 TopRankVideo-125xxx88 的 Bucket 设置名称为"trans-100020-100030-100040"转码规则，转出100020，100030，100040三种格式。

Input: 

```
tccli mps CreateWorkflow --cli-unfold-argument  \
    --WorkflowName trans-100020-100030-100040 \
    --Trigger.Type CosFileUpload \
    --Trigger.CosFileUploadTrigger.Bucket TopRankVideo-125xxx88 \
    --Trigger.CosFileUploadTrigger.Region ap-chongqing \
    --Trigger.CosFileUploadTrigger.Dir /movie/201907/ \
    --MediaProcessTask.TranscodeTaskSet.0.Definition 100020 \
    --MediaProcessTask.TranscodeTaskSet.1.Definition 100030 \
    --MediaProcessTask.TranscodeTaskSet.2.Definition 100040
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

**Example 2: 设置采样截图规则**

对名为 TopRankVideo-125xxx88 的 Bucket 设置名称为"snapshot"转码规则，转出100010规格。

Input: 

```
tccli mps CreateWorkflow --cli-unfold-argument  \
    --WorkflowName snapshot \
    --Trigger.Type CosFileUpload \
    --Trigger.CosFileUploadTrigger.Bucket TopRankVideo-125xxx88 \
    --Trigger.CosFileUploadTrigger.Region ap-chongqing \
    --Trigger.CosFileUploadTrigger.Dir /movie/201907/ \
    --MediaProcessTask.SampleSnapshotTaskSet.0.Definition 100010
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

