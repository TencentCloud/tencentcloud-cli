**Example 1: 导出本次漏洞检测Excel**

导出本次漏洞检测Excel

Input: 

```
tccli cwp ExportVulDetectionExcel --cli-unfold-argument  \
    --TaskId 1596595610
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "DownloadUrl": "https://cwp-1258344***.cos.ap-guangzhou.myqcloud.com/file.txt",
        "TaskId": "1615549629"
    }
}
```

