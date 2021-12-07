**Example 1: 镜像漏洞列表导出**



Input: 

```
tccli tcss DescribeAssetImageVulListExport --cli-unfold-argument  \
    --ImageID dskaldjskld \
    --ExportField CVEID Name Component Version Category
```

Output: 
```
{
    "Response": {
        "DownloadUrl": "sfsfsfsfsfs",
        "RequestId": "7c07629e-58ff-4e8a-b63d-679698cf295a"
    }
}
```

