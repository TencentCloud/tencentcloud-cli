**Example 1: 导出漏洞影响主机列表**



Input: 

```
tccli cwp ExportVulEffectHostList --cli-unfold-argument  \
    --VulId 100435
```

Output: 
```
{
    "Response": {
        "DownloadUrl": "https://cwp-1258344***.cos.ap-guangzhou.myqcloud.com/file.txt",
        "RequestId": "be6f6eec-0825-4e67-ab9a-c8568bbf736c",
        "TaskId": "10001"
    }
}
```

