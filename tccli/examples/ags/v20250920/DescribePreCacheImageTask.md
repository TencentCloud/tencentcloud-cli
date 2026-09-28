**Example 1: 按PreCacheImageId查询预热镜像**



Input: 

```
tccli ags DescribePreCacheImageTask --cli-unfold-argument  \
    --PreCacheImageId pcimg-qi3p****
```

Output: 
```
{
    "Response": {
        "CachedImageSizeBytes": 3523604480,
        "CreateTime": "2026-09-11T16:41:57+08:00",
        "Image": "***.ccs.tencentyun.com/*********/************************:*****",
        "ImageDigest": "sha256:*************",
        "ImageRegistryType": "personal",
        "LastUsedTime": "2026-09-11T18:04:36+08:00",
        "Message": "Image precache completed successfully",
        "PreCacheImageId": "pcimg-qi3p****",
        "SourceType": "EXPLICIT",
        "Status": "Success",
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

**Example 2: 查询用户 VPC 可达第三方镜像预热状态**



Input: 

```
tccli ags DescribePreCacheImageTask --cli-unfold-argument  \
    --Image harbor.internal.example.com/team/app:1.0 \
    --ImageDigest sha256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \
    --ImageRegistryType custom
```

Output: 
```
{
    "Response": {
        "Image": "harbor.internal.example.com/team/app:1.0",
        "ImageDigest": "sha256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "ImageRegistryType": "custom",
        "Status": "Success",
        "Message": "conversion-backed precache completed",
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

