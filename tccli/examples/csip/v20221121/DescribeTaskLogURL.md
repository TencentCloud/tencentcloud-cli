**Example 1: 获取报告下载的临时链接**

获取报告下载的临时链接

Input: 

```
tccli csip DescribeTaskLogURL --cli-unfold-argument  \
    --ReportItemKeyList.0.TaskLogList rpt-**** \
    --Type 0 \
    --ReportTaskIdList.0.AppId 1302**** \
    --ReportTaskIdList.0.TaskIdList rmis-****
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "URL": "https://yuzhi-tasklog-pdf-1300616671.cos.ap-guangzhou.myqcloud.com/****.pdf",
                "LogId": "rpt-****",
                "TaskLogName": "标准体检_*****",
                "AppId": "1302****"
            }
        ],
        "RequestId": "7429061e-dabd-e1ee-e135-43364c7bb15d"
    }
}
```

