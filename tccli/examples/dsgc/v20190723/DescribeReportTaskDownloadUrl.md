**Example 1: 获取资产报告下载链接**

获取资产报告下载链接

Input: 

```
tccli dsgc DescribeReportTaskDownloadUrl --cli-unfold-argument  \
    --ReportTaskId 1 \
    --IsWithSensitiveDetailReport True \
    --DspaId dspa-12ac32db
```

Output: 
```
{
    "Response": {
        "DownloadUrlSet": [
            "https://dsgc-report-test-13254732833.cos.ap-guangzhou.myqcloud.com/report%2F232457112%2F%E8%B5%8……"
        ],
        "RequestId": "91c7a73v-e540-4780-8b8e-74e0b65b4f1a"
    }
}
```

