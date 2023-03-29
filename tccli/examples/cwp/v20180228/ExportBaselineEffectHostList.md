**Example 1: 漏洞影响主机列表导出**

导出漏洞影响主机列表数据

Input: 

```
tccli cwp ExportBaselineEffectHostList --cli-unfold-argument  \
    --BaselineId 1
```

Output: 
```
{
    "Response": {
        "DownloadUrl": "",
        "RequestId": "requestId",
        "TaskId": "123456"
    }
}
```

