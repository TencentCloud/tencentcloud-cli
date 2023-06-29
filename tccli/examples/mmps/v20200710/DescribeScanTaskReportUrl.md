**Example 1: 查询小程序隐私合规诊断任务状态**

任务完成

Input: 

```
tccli mmps DescribeScanTaskReportUrl --cli-unfold-argument  \
    --Source 0 \
    --TaskType 0 \
    --ReportType 0 \
    --TaskID 1701438134******0 \
    --Platform 2
```

Output: 
```
{
    "Response": {
        "RequestId": "5e93a212-ca01-0fdc-eedd-5a1fce5e83e6",
        "Result": 0,
        "ReportUrl": "诊断报告下载链接url",
        "ReportTitle": "诊断报告名称",
        "ReportResult": "诊断json结果内容"
    }
}
```

