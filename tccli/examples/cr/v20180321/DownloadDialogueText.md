**Example 1: 对话文本下载**



Input: 

```
tccli cr DownloadDialogueText --cli-unfold-argument  \
    --Module Report \
    --Operation DownloadTextReport \
    --InstId ins-abc123 \
    --ReportDate 2018-07-15
```

Output: 
```
{
    "Response": {
        "TextReportUrl": "http://collection-robot.myqcloud.com/report-text.zip",
        "RequestId": "15d67679-7f71-4077-a7bd-c0ed27ae2461"
    }
}
```

