**Example 1: 查询安全审计日志导出文件下载链接**

查询安全审计日志导出文件下载链接。

Input: 

```
tccli dbbrain DescribeSecurityAuditLogDownloadUrls --cli-unfold-argument  \
    --SecAuditGroupId sag-01z37k3f \
    --Product mysql \
    --AsyncRequestId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "6ad536b0-5ee2-11eb-bc9a-9357e9eb1000",
        "Urls": [
            "https://xxx"
        ]
    }
}
```

