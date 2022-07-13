**Example 1: 查询App隐私合规诊断任务状态**

任务完成

Input: 

```
tccli acp DescribeScanTaskReportUrl --cli-unfold-argument  \
    --Source 2 \
    --TaskType 0 \
    --ReportType 0 \
    --TaskID 1701438134******0 \
    --Platform 0
```

Output: 
```
{
    "Response": {
        "RequestId": "5e93a212-***-0fdc-****-5a1fce5e83e6",
        "Result": 0,
        "ReportUrl": "诊断报告下载链接url",
        "ReportTitle": "诊断报告名称"
    }
}
```

