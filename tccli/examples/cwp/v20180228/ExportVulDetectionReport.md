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
        "RequestId": "935e27b1-d675-4509-80bf-96fbf0764237",
        "DownloadUrl": "https://xxx.cos.ap-guangzhou.myqcloud.com/%E6%BC%8F%E6%B4%9E%E6%A3%80%E6%B5%8B%E6%8A%A5%E5%91%8A_20210312.pdf?q-sign-algorithm=sha1&q-ak=xxx&q-sign-time=1615549630%3B1615553230&q-key-time=1615549630%3B1615553230&q-header-list=host&q-url-param-list=&q-signature=xxx",
        "TaskId": "15674"
    }
}
```

