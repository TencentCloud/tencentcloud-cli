**Example 1: 查看任务列表**

查看任务执行列表

Input: 

```
tccli ioa DescribeTaskList --cli-unfold-argument  \
    --OsType 0 \
    --Condition.PageSize 20 \
    --Condition.PageNum 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Page": {
                "PageSize": 1,
                "PageNum": 1,
                "PageCount": 1,
                "Total": 1
            },
            "Items": [
                {
                    "Seq": 0,
                    "TaskId": 0,
                    "BusinessId": 0,
                    "Owner": "abc",
                    "Status": 0,
                    "Result": "abc",
                    "Data": "abc",
                    "BeginTime": "abc",
                    "DeviceTotal": 0,
                    "DeviceCount": 0,
                    "Itime": "abc",
                    "Utime": "abc",
                    "TaskResultStatus": 0,
                    "OsType": 0
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

