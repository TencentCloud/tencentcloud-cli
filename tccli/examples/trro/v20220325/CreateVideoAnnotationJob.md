**Example 1: 调用示例1-对象存储源**



Input: 

```
tccli trro CreateVideoAnnotationJob --cli-unfold-argument  \
    --InputType 1 \
    --AnnotationType 3 \
    --S3SourceInfo.Bucket ai-annotation-test-input-1258344699 \
    --S3SourceInfo.Endpoint cos-internal.ap-guangzhou.tencentcos.cn \
    --S3SourceInfo.Region ap-guangzhou \
    --S3SourceInfo.Key batch-test/1qLIfbvfNo_0003.mp4 \
    --S3SourceInfo.Secret.SecretId ************************************ \
    --S3SourceInfo.Secret.SecretKey ******************************** \
    --S3SourceInfo.IsCos 1 \
    --AnnotationContext.TaskGoal 把香蕉从盘子中夹出来 \
    --AnnotationContext.KeyObjects 香蕉 \
    --AnnotationContext.AtomicVerbs 拿取 \
    --OutputInfo.Bucket ai-annotation-test-input-1258344699 \
    --OutputInfo.Endpoint cos-internal.ap-guangzhou.tencentcos.cn \
    --OutputInfo.Region ap-guangzhou \
    --OutputInfo.Key annotation-result/1qLIfbvfNo_0003.json \
    --OutputInfo.Secret.SecretId ************************************ \
    --OutputInfo.Secret.SecretKey ******************************** \
    --CallbackInfo.Url https://callback.example.com/annotation \
    --CallbackInfo.Secret test-callback-secret-0f1e2d3c
```

Output: 
```
{
    "Response": {
        "JobId": "3uixltd7dni3",
        "RequestId": "15df6e34-08b8-42c4-ab24-5b8dbac82a07"
    }
}
```

**Example 2: 调用示例2-HTTP源**



Input: 

```
tccli trro CreateVideoAnnotationJob --cli-unfold-argument  \
    --InputType 2 \
    --AnnotationType 3 \
    --HttpUrl https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4
```

Output: 
```
{
    "Response": {
        "JobId": "3uimnz9razwb",
        "RequestId": "b38bba35-d582-45de-a7ea-e0749145839e"
    }
}
```

