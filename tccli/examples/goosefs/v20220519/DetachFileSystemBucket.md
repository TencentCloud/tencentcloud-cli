**Example 1: 解绑文件系统与Bucket的映射**

解绑文件系统与Bucket的映射

Input: 

```
tccli goosefs DetachFileSystemBucket --cli-unfold-argument  \
    --FileSystemId x_c60_r3c4fa1f \
    --BucketName mybucket-12500000
```

Output: 
```
{
    "Response": {
        "RequestId": "b3caa32f-5e39-4360-91e4-5724369b78a6"
    }
}
```

