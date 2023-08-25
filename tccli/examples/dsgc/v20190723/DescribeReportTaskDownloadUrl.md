**Example 1: 获取资产报告下载链接**

获取资产报告下载链接

Input: 

```
tccli dsgc DescribeReportTaskDownloadUrl --cli-unfold-argument  \
    --ReportTaskId 1 \
    --IsWithSensitiveDetailReport True \
    --DspaId abc
```

Output: 
```
{
    "Response": {
        "DownloadUrlSet": [
            "abc"
        ],
        "RequestId": "abc"
    }
}
```

