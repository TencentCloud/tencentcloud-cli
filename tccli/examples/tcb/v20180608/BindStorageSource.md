**Example 1: 绑定腾讯云COS作为外部数据源**



Input: 

```
tccli tcb BindStorageSource --cli-unfold-argument  \
    --EnvId cloudbase-0gx36sm8ddc58be0 \
    --StorageConfig.Enabled True \
    --StorageConfig.BucketName tencent-cos-bucket-1257619089 \
    --StorageConfig.Region ap-shanghai \
    --StorageConfig.BasePath cloudbase-env-v1
```

Output: 
```
{
    "Response": {
        "RequestId": "fd56e5d7-8b26-4ac2-ad17-82f9a3265337"
    }
}
```

