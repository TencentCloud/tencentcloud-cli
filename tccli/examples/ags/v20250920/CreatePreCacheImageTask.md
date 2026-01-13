**Example 1: 创建预热镜像任务**



Input: 

```
tccli ags CreatePreCacheImageTask --cli-unfold-argument  \
    --Image test.tencentcloudcr.com/example/app:0.2.2 \
    --ImageRegistryType enterprise
```

Output: 
```
{
    "Response": {
        "Image": "test.tencentcloudcr.com/example/app:0.2.2",
        "ImageDigest": "sha256:39e2c18395c3105ace919d1d285cd775d380e83581b132d8d742761123a1e675",
        "ImageRegistryType": "enterprise",
        "RequestId": "57872da7-8d1e-4035-819f-92c26eaf9557"
    }
}
```

