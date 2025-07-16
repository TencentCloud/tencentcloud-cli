**Example 1: 发起评测任务**



Input: 

```
tccli mps CreateMediaEvaluation --cli-unfold-argument  \
    --InputInfo.Type URL \
    --InputInfo.UrlInputInfo.Url http://abc/reference.mp4 \
    --OutputStorage.Type COS \
    --OutputStorage.CosOutputStorage.Bucket mybucket \
    --OutputStorage.CosOutputStorage.Region ap-guangzhou \
    --OutputDir /output/ \
    --EvaluationTask.TaskType NORMAL \
    --EvaluationTask.EvaluationTypeSet PSNR VMAF \
    --EvaluationTask.EvaluationRangeType FRAME \
    --EvaluationTask.ContrastMediaSet.0.InputInfo.Type URL \
    --EvaluationTask.ContrastMediaSet.0.InputInfo.UrlInputInfo.Url http://abc/reference_transcode.mp4 \
    --EvaluationTask.StartFrameIndex 1 \
    --EvaluationTask.EndFrameIndex 100
```

Output: 
```
{
    "Response": {
        "TaskId": "24000006-EvaluationTask-366dd19ff7159ba06e24467b4212c41ett12",
        "RequestId": "df1b9015-1f90-4ed1-820a-380cd78cbe5e"
    }
}
```

