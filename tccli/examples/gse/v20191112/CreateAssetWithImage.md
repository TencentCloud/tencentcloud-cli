**Example 1: 创建生成包镜像信息**



Input: 

```
tccli gse CreateAssetWithImage --cli-unfold-argument  \
    --AssetName asset-demo \
    --AssetVersion 1.0 \
    --AssetRegion ap-shanghai \
    --ImageId img-pj8r89ch \
    --ImageSize 40GB \
    --ImageOs 'CentOS 6.5 64bit' \
    --OsType CentOS \
    --ImageType SHARED_IMAGE \
    --OsBit 64
```

Output: 
```
{
    "Response": {
        "AssetArn": "qcs::gse:ap-shanghai:uin/838831829:asset/asset-mds6425j",
        "AssetId": "asset-mds6425j",
        "RequestId": "s1604054956874940891"
    }
}
```

