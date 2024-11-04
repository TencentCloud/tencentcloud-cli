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
        "DownloadUrl": "",
        "RequestId": "be6f6eec-0825-4e67-ab9a-c8568bbf736c",
        "TaskId": "10001"
    }
}
```

