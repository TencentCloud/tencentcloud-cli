**Example 1: 预热镜像**



Input: 

```
tccli ags CreatePreCacheImageTask --cli-unfold-argument  \
    --Image test.tencentcloudcr.com/example/app:0.2.2 \
    --ImageRegistryType enterprise \
    --TimeoutMinutes 60
```

Output: 
```
{
    "Response": {
        "Image": "test.tencentcloudcr.com/example/app:0.2.2",
        "ImageDigest": "sha256:axxxxxxxxxb98e195ae1d8c85d59fe1fb8c282bcccf1071f877db20f",
        "ImageRegistryType": "enterprise",
        "RequestId": "b538f3f1-da59-49e5-ac4b-41a440396ec6"
    }
}
```

