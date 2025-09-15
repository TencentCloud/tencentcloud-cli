**Example 1: 导出基于设备分组的软件分类列表**



Input: 

```
tccli ioa ExportSoftCategoryListByDevice --cli-unfold-argument  \
    --OsType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "0d8287c1-8c27-439a-a4b7-df6a03d7e75c",
        "Data": {
            "DownloadURL": "https://xxx"
        }
    }
}
```

