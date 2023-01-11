**Example 1: 查询子渠道的App合规诊断任务报告url**

获取诊断报告

Input: 

```
tccli acp DescribeChannelTaskReportUrl --cli-unfold-argument  \
    --Source 2 \
    --Platform 0 \
    --TaskID 170******340 \
    --TaskType 0 \
    --ReportType 0 \
    --AppMD5 12xxxxxxx03
```

Output: 
```
{
    "Response": {
        "RequestId": "5*********3e6",
        "Result": 0,
        "ReportUrl": "诊断报告下载链接url",
        "ReportTitle": "诊断报告名称"
    }
}
```

