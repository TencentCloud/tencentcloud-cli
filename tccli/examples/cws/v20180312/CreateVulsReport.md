**Example 1: 生成漏洞报告**

本接口 (CreateVulsReport) 用于生成漏洞报告并返回下载链接。

Input: 

```
tccli cws CreateVulsReport --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ReportFileUrl": "https://cws-test-1256046992.cos.ap-guangzhou.myqcloud.com/report/1251001047/report_monitor_2.pdf",
        "RequestId": "905d87e7-e756-473e-b035-7ad74390850f"
    }
}
```

