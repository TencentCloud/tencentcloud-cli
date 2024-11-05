**Example 1: 批量授权镜像扫描V2.0**



Input: 

```
tccli tcss ModifyImageAuthorized --cli-unfold-argument  \
    --AllLocalImages False \
    --AllRegistryImages False \
    --ImageSourceType ASSETIMAGE \
    --LocalImageIds sha256:aaad346fbeab5768b61c75f016128c9189b7d0135053d308ef02958a8c80e6cd \
    --OnlyShowLatest True \
    --UpdatedLocalImageCnt 100 \
    --UpdatedRegistryImageCnt 0
```

Output: 
```
{
    "Response": {
        "RequestId": "e55bf3cb-f38f-4697-8638-a1e22efe8bb1"
    }
}
```

