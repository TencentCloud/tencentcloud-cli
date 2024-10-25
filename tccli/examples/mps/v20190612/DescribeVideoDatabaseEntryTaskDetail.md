**Example 1: 查询任务状态**

根据任务ID查询视频入库任务的状态

Input: 

```
tccli mps DescribeVideoDatabaseEntryTaskDetail --cli-unfold-argument  \
    --TaskId 251xxx279-VideoDBEntryTask-60e4ae3b23ff4fd3936eb6b7e8af25ec
```

Output: 
```
{
    "Response": {
        "TaskId": "251xxx279-VideoDBEntryTask-60e4ae3b23ff4fd3936eb6b7e8af25ec",
        "Status": "SUCCESS",
        "VideoDBEntryTaskResults": [
            {
                "VideoId": "c92846202b9fca7813dfc92846fc3e408"
            }
        ],
        "RequestId": "c92846202b9fca7813df05aa2b9fe408"
    }
}
```

