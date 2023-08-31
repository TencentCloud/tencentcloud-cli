**Example 1: 获取报告下载的临时链接**

获取报告下载的临时链接

Input: 

```
tccli csip DescribeTaskLogURL --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "URL": "xx",
                "LogId": "xx",
                "TaskLogName": "xx",
                "AppId": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

