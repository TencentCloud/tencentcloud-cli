**Example 1: 获取扫描报告下载链接**



Input: 

```
tccli advisor DescribeDownloadTask --cli-unfold-argument  \
    --ResultId -1#Group#0f7c2fac-20ee-4da9-8e71-944577bf7616
```

Output: 
```
{
    "Response": {
        "CosUrl": "https://advisor-scan-pre-1258344699.cos-internal.ap-guangzhou.tencentcos.cn/AdvisorExcel/腾讯云智能顾问评估结果_2159973417_1251956900(2025-12-17 17_12_33).xlsx",
        "CosUrlPdf": "https://advisor-scan-pre-1258344699.cos-internal.ap-guangzhou.tencentcos.cn/AdvisorExcel/腾讯云智能顾问评估结果_2159973417_1251956900(2025-12-17 17_12_40).pdf",
        "RequestId": "615658e1-6720-43d4-bb2e-4efaadc7f94a",
        "TaskStatus": "success"
    }
}
```

