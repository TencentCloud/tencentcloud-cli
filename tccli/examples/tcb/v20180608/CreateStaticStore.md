**Example 1: 创建静态托管资源**



Input: 

```
tccli tcb CreateStaticStore --cli-unfold-argument  \
    --EnvId lotestapi100004
```

Output: 
```
{
    "Response": {
        "Result": "succ",
        "RequestId": "5620b49e-a25a-4007-84ef-03c9035c584d"
    }
}
```

**Example 2: 以腾讯云COS作为外部存储源开通静态托管**



Input: 

```
tccli tcb CreateStaticStore --cli-unfold-argument  \
    --EnvId cloudbase-0gx36sm8ddc58be0 \
    --ExternalStorage.BucketName tencent-cos-v2-1257619089 \
    --ExternalStorage.Region ap-shanghai \
    --ExternalStorage.BasePath cloudbase-0gx36sm8ddc58be-static \
    --ExternalStorage.Enabled True
```

Output: 
```
{
    "Response": {
        "Result": "succ",
        "RequestId": "39ec0c65-d979-4990-90df-facb97c78e73"
    }
}
```

