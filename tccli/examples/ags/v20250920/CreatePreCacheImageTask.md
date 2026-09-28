**Example 1: 预热**



Input: 

```
tccli ags CreatePreCacheImageTask --cli-unfold-argument  \
    --Image tcr-cq.tencentcloudcr.com/test/alpine:latest \
    --ImageRegistryType enterprise
```

Output: 
```
{
    "Response": {
        "Image": "******.tencentcloudcr.com/***********:******",
        "ImageDigest": "sha256:*************************************************************",
        "ImageRegistryType": "enterprise",
        "PreCacheImageId": "pcimg-f8c*****",
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

**Example 2: 预热用户 VPC 可达第三方镜像**



Input: 

```
tccli ags CreatePreCacheImageTask --cli-unfold-argument  \
    --Image harbor.internal.example.com/team/app:1.0 \
    --ImageRegistryType custom
```

Output: 
```
{
    "Response": {
        "Image": "harbor.internal.example.com/team/app:1.0",
        "ImageDigest": "sha256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "ImageRegistryType": "custom",
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

