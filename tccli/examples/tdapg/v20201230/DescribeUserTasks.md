**Example 1: 查询任务列表和详情**



Input: 

```
tccli tdapg DescribeUserTasks --cli-unfold-argument  \
    --Limit 0 \
    --Filters.0.Values tdapg-lhoplocc \
    --Filters.0.Name InstanceIds \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "a8b8cc55-a0b8-46c6-b265-85f7ad71a43c",
        "TaskList": [
            {
                "AppId": 1251966477,
                "CreateTime": "2021-03-29 11:06:13",
                "EndTime": "2021-03-29 11:06:15",
                "ErrMsg": "",
                "Id": 1533,
                "InstanceId": "tdapg-lhoplocc",
                "InstanceName": "tdapg-lhoplocc",
                "Progress": 100,
                "Status": "success",
                "TaskType": "modifyParams"
            },
            {
                "AppId": 1251966477,
                "CreateTime": "2021-03-26 14:17:02",
                "EndTime": "2021-03-26 14:21:06",
                "ErrMsg": "",
                "Id": 1531,
                "InstanceId": "tdapg-lhoploccc",
                "InstanceName": "tdapg-lhoplocc",
                "Progress": 100,
                "Status": "success",
                "TaskType": "create"
            }
        ],
        "TotalCount": 5
    }
}
```

