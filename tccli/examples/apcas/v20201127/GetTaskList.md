**Example 1: 查询任务列表**

查询当前账号AppId下任务列表

Input: 

```
tccli apcas GetTaskList --cli-unfold-argument  \
    --PageNumber 0 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx",
        "TaskListData": {
            "PageNumber": 0,
            "PageSize": 10,
            "TotalCount": 4,
            "TaskList": [
                {
                    "ID": 2,
                    "TaskName": "测试222",
                    "StartTime": 1608799481159,
                    "Status": 2,
                    "Available": 99973,
                    "ErrMsg": ""
                },
                {
                    "ID": 1,
                    "TaskName": "测试111",
                    "StartTime": 1608798649057,
                    "Status": 3,
                    "Available": 0,
                    "ErrMsg": "available people should greater than 1000, now is 5"
                }
            ]
        }
    }
}
```

