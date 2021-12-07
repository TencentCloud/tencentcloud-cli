**Example 1: 镜像仓库镜像列表导出**



Input: 

```
tccli tcss DescribeAssetImageRegistryListExport --cli-unfold-argument  \
    --By xx \
    --ExportField xx \
    --Limit 1 \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --Filters.0.ExactMatch True \
    --Offset 1 \
    --Order xx
```

Output: 
```
{
    "Response": {
        "RequestId": "c00f4492-6973-4d8f-872b-c29d22c8eee0",
        "DownloadUrl": "https://image-registory-1302977000.cos.ap-guangzhou.myqcloud.com/251011530-100015468030-ImageListExport.csv?q-sign-algorithm=sha1&q-ak=AKIDSefQCiRPhjYAW4BR9b1B9qqd4E71a63k&q-sign-time=1611991144%3B1611991204&q-key-time=1611991144%3B1611991204&q-header-list=host&q-url-param-list=&q-signature=e3fc796e87165f7401098b83208d973e8e1af6ec"
    }
}
```

