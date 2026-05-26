**Example 1: 修改云存储外部数据源**

修改云存储外部数据源，更换 COS桶 和 BasePath

Input: 

```
tccli tcb ModifyStorageSource --cli-unfold-argument  \
    --EnvId cloudbase-0gx36sm8ddc58be0 \
    --StorageConfig.BucketName tencent-cos-v2-1257619089 \
    --StorageConfig.Region ap-shanghai \
    --StorageConfig.BasePath cloudbase-0gx36sm8ddc58be0
```

Output: 
```
{
    "Response": {
        "RequestId": "1c13cdb3-a99b-49fb-a42a-f106527ec577"
    }
}
```

