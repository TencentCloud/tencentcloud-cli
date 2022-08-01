**Example 1: 获取小程序的诊断报告链接**



Input: 

```
tccli mmps DescribeFlySecMiniAppReportUrl --cli-unfold-argument  \
    --ReportType 0 \
    --MiniAppID wx66e50f1e*******6f \
    --Mode 1 \
    --TaskID 1701438134******0
```

Output: 
```
{
    "Response": {
        "RequestId": "5e93a212-ca01-0fdc-eedd-5a1fce5e83e6",
        "Ret": 0,
        "Url": "诊断报告下载链接"
    }
}
```

