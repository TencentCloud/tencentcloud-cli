**Example 1: 批量授权镜像扫描V2.0**



Input: 

```
tccli tcss ModifyImageAuthorized --cli-unfold-argument  \
    --AllLocalImages false \
    --UpdatedLocalImageCnt 1 \
    --LocalImageIds xx \
    --AllRegistryImages false \
    --UpdatedRegistryImageCnt 1 \
    --RegistryImageIds xx \
    --ImageSourceType ASSETIMAGE
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

