**Example 1: 获取漏洞扫描诊断报告url**



Input: 

```
tccli acp DescribeScanTaskReportUrl --cli-unfold-argument  \
    --Platform 0 \
    --Source 3 \
    --ReportType 0 \
    --TaskID 347***496 \
    --TaskType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "d9357*********a512b39ee",
        "Result": 0,
        "ReportUrl": "http://apk***f3x_00yY",
        "ReportTitle": "",
        "ReportResult": ""
    }
}
```

**Example 2: 查询App隐私合规诊断任务状态**

任务完成

Input: 

```
tccli acp DescribeScanTaskReportUrl --cli-unfold-argument  \
    --Source 2 \
    --TaskType 0 \
    --ReportType 0 \
    --TaskID 170******340 \
    --Platform 0
```

Output: 
```
{
    "Response": {
        "RequestId": "5*********3e6",
        "Result": 0,
        "ReportUrl": "诊断报告下载链接url",
        "ReportTitle": "诊断报告名称",
        "ReportResult": "诊断报告内容"
    }
}
```

