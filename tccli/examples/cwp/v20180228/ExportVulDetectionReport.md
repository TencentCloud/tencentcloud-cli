**Example 1: 导出漏洞检测报告**



Input: 

```
tccli cwp ExportVulDetectionReport --cli-unfold-argument  \
    --TaskId 1596595610
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "DownloadUrl": "https://yunjing-dev-1256299843.cos.ap-guangzhou.myqcloud.com/%E6%BC%8F%E6%B4%9E%E6%A3%80%E6%B5%8B%E6%8A%A5%E5%91%8A_20210312.pdf?q-sign-algorithm=sha1&q-ak=AKIDhKl043NTODrNqE5dghYgnmdIqEPSgDug&q-sign-time=1615549630%3B1615553230&q-key-time=1615549630%3B1615553230&q-header-list=host&q-url-param-list=&q-signature=b6bcb7404ad9338e34fce4766c32ba6c47b7e5ec",
        "TaskId": 1615549629
    }
}
```

