**Example 1: 调用示例1**



Input: 

```
tccli trro CreateBatchVideoAnnotationJob --cli-unfold-argument  \
    --InputStorage.Bucket ai-annotation-test-input-1258344699 \
    --InputStorage.Endpoint cos-internal.ap-guangzhou.tencentcos.cn \
    --InputStorage.Region ap-guangzhou \
    --InputStorage.Prefix batch-test/ \
    --InputStorage.Secret.SecretId ************************************ \
    --InputStorage.Secret.SecretKey ******************************** \
    --InputStorage.Filter ^1qLI.*\.mp4$ \
    --InputStorage.IsCos 1 \
    --AnnotationType 3 \
    --AnnotationContext.TaskGoal 把香蕉从盘子中夹起来 \
    --AnnotationContext.KeyObjects 香蕉 \
    --AnnotationContext.AtomicVerbs 拿取 \
    --OutputStorage.Bucket ai-annotation-test-input-1258344699 \
    --OutputStorage.Endpoint cos-internal.ap-guangzhou.tencentcos.cn \
    --OutputStorage.Region ap-guangzhou \
    --OutputStorage.Secret.SecretId ************************************ \
    --OutputStorage.Secret.SecretKey ******************************** \
    --OutputStorage.Prefix batch-result/ \
    --OutputStorage.NameRule $YYYY$mm$dd_$FileName_$TaskId.json \
    --CallbackInfo.Url https://callback.example.com/annotation \
    --CallbackInfo.Secret test-callback-secret-0f1e2d3c
```

Output: 
```
{
    "Response": {
        "JobId": "3uixqpy6yywr",
        "RequestId": "e2fb02e7-7dad-40bf-a100-69e6eab7af28"
    }
}
```

