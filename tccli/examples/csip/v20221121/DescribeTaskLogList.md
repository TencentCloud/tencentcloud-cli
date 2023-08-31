**Example 1: 获取任务扫描报告列表**

获取任务扫描报告列表

Input: 

```
tccli csip DescribeTaskLogList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Data": [
            {
                "TaskLogName": "xx",
                "TaskLogId": "xx",
                "AssetsNumber": 0,
                "RiskNumber": 0,
                "Time": "xx",
                "Status": 0,
                "TaskName": "xx",
                "StartTime": "xx",
                "TaskCenterTaskId": "xx",
                "AppId": "xx",
                "UIN": "xx",
                "UserName": "xx"
            }
        ],
        "NotViewNumber": 0,
        "RequestId": "xx"
    }
}
```

