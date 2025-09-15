**Example 1: 导出基于软件分类的软件列表**



Input: 

```
tccli ioa ExportSoftListBySoftCategory --cli-unfold-argument  \
    --OsType 0 \
    --GroupId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "3b916d06-c775-417f-a393-af61a08eff5f",
        "Data": {
            "DownloadURL": "https://xxx"
        }
    }
}
```

