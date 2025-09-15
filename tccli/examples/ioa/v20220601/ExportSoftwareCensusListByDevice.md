**Example 1: 导出按终端查看软件统计列表**



Input: 

```
tccli ioa ExportSoftwareCensusListByDevice --cli-unfold-argument  \
    --OsType 0 \
    --GroupId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "b9657bd5-a848-43a9-8849-d278f6cd5207",
        "Data": {
            "DownloadURL": "https://xxx"
        }
    }
}
```

