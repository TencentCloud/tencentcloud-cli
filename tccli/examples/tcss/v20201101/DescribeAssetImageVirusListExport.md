**Example 1: 查询镜像病毒列表导出**

查询镜像病毒列表导出

Input: 

```
tccli tcss DescribeAssetImageVirusListExport --cli-unfold-argument  \
    --ImageID dskaldjskld \
    --ExportField Path RiskLevel FileType VirusName Tags
```

Output: 
```
{
    "Response": {
        "DownloadUrl": "sfsfsfsfsfs",
        "JobId": "",
        "RequestId": "7c07629e-58ff-4e8a-b63d-679698cf295a"
    }
}
```

