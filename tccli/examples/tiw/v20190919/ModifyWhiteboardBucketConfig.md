**Example 1: 设置应用资源配置**



Input: 

```
tccli tiw ModifyWhiteboardBucketConfig --cli-unfold-argument  \
    --SdkAppId 1400000001 \
    --TaskType recording \
    --BucketLocation ap-guangzhou \
    --BucketName test-120000001 \
    --BucketPrefix doc \
    --ResultDomain https://bucket.com
```

Output: 
```
{
    "Response": {
        "RequestId": "d290f1ee-6c54-4b01-90e6-d701748f0851"
    }
}
```

