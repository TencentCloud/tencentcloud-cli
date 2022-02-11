**Example 1: 创建媒体库**



Input: 

```
tccli smh CreateLibrary --cli-unfold-argument  \
    --BucketRegion ap-guangzhou \
    --Name 名称 \
    --Remark 备注 \
    --LibraryExtension.IsFileLibrary true \
    --BucketName examplebucket-1250000000
```

Output: 
```
{
    "Response": {
        "LibraryId": "smh0q8nrvsg7t6y6",
        "RequestId": "1586674e-e04c-4315-943a-c282b5f8ed6b"
    }
}
```

