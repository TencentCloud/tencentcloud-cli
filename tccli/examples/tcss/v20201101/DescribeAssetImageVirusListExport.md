**Example 1: 查询镜像病毒列表导出**

查询镜像病毒列表导出

Input: 

```
tccli tcss DescribeAssetImageVirusListExport --cli-unfold-argument  \
    --ImageID sha256:80beff5ff34259ceb7fbe9cd10b2d94912618f5b5595f23434***** \
    --ExportField Path RiskLevel FileType VirusName Tags
```

Output: 
```
{
    "Response": {
        "DownloadUrl": "www.***.com/***",
        "JobId": "JobId",
        "RequestId": "7c07629e-58ff-4e8a-b63d-679698cf295a"
    }
}
```

