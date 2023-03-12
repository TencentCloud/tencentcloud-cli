**Example 1: 全部下载列表**

获取基线下载列表

Input: 

```
tccli cwp DescribeBaselineDownloadList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "TaskId": 1,
                "TaskName": "123",
                "Status": 0,
                "StartTime": "0001-01-01 00:00:00",
                "EndTime": "0001-01-01 00:00:00",
                "DownloadUrl": "http://www.a.b.c"
            }
        ],
        "RequestId": "b0596030-57ec-42aa-8e0f-738a6a07e2d0",
        "Total": 1
    }
}
```

