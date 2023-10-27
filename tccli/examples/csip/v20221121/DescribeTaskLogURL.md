**Example 1: 获取报告下载的临时链接**

获取报告下载的临时链接

Input: 

```
tccli csip DescribeTaskLogURL --cli-unfold-argument  \
    --ReportItemKeyList.0.TaskLogList abc \
    --Type 0 \
    --ReportTaskIdList.0.AppId abc \
    --ReportTaskIdList.0.TaskIdList abc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "URL": "abc",
                "LogId": "abc",
                "TaskLogName": "abc",
                "AppId": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

