**Example 1: 查询任务状态**

根据任务ID查询视频检索任务的状态

Input: 

```
tccli mps DescribeVideoSearchTaskDetail --cli-unfold-argument  \
    --TaskId 251xxx279-SearchTask-60e4ae3b23ff4fd3936eb6b7e8af25ec
```

Output: 
```
{
    "Response": {
        "TaskId": "251xxx279-SearchTask-60e4ae3b23ff4fd3936eb6b7e8af25ec",
        "Status": "SUCCESS",
        "SearchTaskResults": [
            {
                "Score": 0.7654,
                "VideoId": "c92846202b9fca7813d2846a6fc3e408"
            }
        ],
        "RequestId": "65ef8b23-677a-429d-83aa-d7eef8bb2aa9"
    }
}
```

