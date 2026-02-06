**Example 1: 导出软件信息列表**



Input: 

```
tccli ioa ExportSoftwareInformationList --cli-unfold-argument  \
    --Mid 1
```

Output: 
```
{
    "Response": {
        "RequestId": "0c1f66e2-90aa-4253-8e32-4abddb044170",
        "Data": {
            "DownloadURL": "https://xxxx"
        }
    }
}
```

**Example 2: 测试下载**

测试下载

Input: 

```
tccli ioa ExportSoftwareInformationList --cli-unfold-argument  \
    --Mid 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "DownloadURL": "http://xxx",
            "TaskId": 0
        },
        "RequestId": "e36ff231-6bbc-475d-9e26-dd0d59260b55"
    }
}
```

