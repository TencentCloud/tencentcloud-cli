**Example 1: 镜像仓库木马信息列表导出**



Input: 

```
tccli tcss DescribeAssetImageRegistryVirusListExport --cli-unfold-argument  \
    --ImageInfo.Force xx \
    --ImageInfo.ImageTag xx \
    --ImageInfo.InstanceId xx \
    --ImageInfo.RegistryType xx \
    --ImageInfo.Namespace xx \
    --ImageInfo.ImageRepoAddress xx \
    --ImageInfo.ImageName xx \
    --ImageInfo.ImageDigest xx \
    --ImageInfo.InstanceName xx \
    --ExportField xx \
    --Limit 1 \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --Filters.0.ExactMatch True \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "RequestId": "62e5c0e8-2cae-410a-8240-9cefbd419e08",
        "DownloadUrl": "https://image-registory-1302977000.cos.ap-guangzhou.myqcloud.com/251011530-100015468030-ImageVirusListExport.csv?q-sign-algorithm=sha1&q-ak=AKIDSefQCiRPhjYAW4BR9b1B9qqd4E71a63k&q-sign-time=1611991027%3B1611991087&q-key-time=1611991027%3B1611991087&q-header-list=host&q-url-param-list=&q-signature=2fe57c480e4161a967cdbac59e0e2e0271a6d74c"
    }
}
```

