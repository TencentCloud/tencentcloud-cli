**Example 1: 忽略基线检测项导出**

导出已忽略的检测项信息

Input: 

```
tccli cwp ExportIgnoreBaselineRule --cli-unfold-argument  \
    --RuleName "检测项1"
```

Output: 
```
{
    "Response": {
        "DownloadUrl": "",
        "RequestId": "requestId",
        "TaskId": "12123"
    }
}
```

