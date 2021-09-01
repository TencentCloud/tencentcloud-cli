**Example 1: 基线列表导出接口**

导出列表信息或者详情信息

Input: 

```
tccli cwp ExportBaselineList --cli-unfold-argument  \
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

