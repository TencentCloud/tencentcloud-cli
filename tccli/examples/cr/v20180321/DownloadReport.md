**Example 1: 报告下载**

报告下载

Input: 

```
tccli cr DownloadReport --cli-unfold-argument  \
    --Module Report \
    --Operation DownloadReport \
    --ReportDate 2018-07-15
```

Output: 
```
{
    "Response": {
        "DailyReportUrl": "http://collection-robot.myqcloud.com/report-type01.zip",
        "ResultReportUrl": "http://collection-robot.myqcloud.com/report-type02.zip",
        "DetailReportUrl": "http://collection-robot.myqcloud.com/report-type03.zip",
        "CallbackDailyReportUrl": "http://collection-robot.myqcloud.com/report-type04.zip",
        "CallbackResultReportUrl": "http://collection-robot.myqcloud.com/report-type05.zip",
        "CallbackDetailReportUrl": "http://collection-robot.myqcloud.com/report-type06.zip",
        "RequestId": "15d67679-7f71-4077-a7bd-c0ed27ae2461"
    }
}
```

