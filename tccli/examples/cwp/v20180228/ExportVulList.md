**Example 1: 导出漏洞列表数据，获取下载url**

导出漏洞列表数据，获取下载url

Input: 

```
tccli cwp ExportVulList --cli-unfold-argument  \
    --IfDetail 1
```

Output: 
```
{
    "Response": {
        "DownloadUrl": "xx",
        "RequestId": "xx",
        "TaskId": "xx"
    }
}
```

