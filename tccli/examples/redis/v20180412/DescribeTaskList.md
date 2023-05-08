**Example 1: 示例**

查询实例的任务详情

Input: 

```
tccli redis DescribeTaskList --cli-unfold-argument  \
    --InstanceId crs-opcazbrb
```

Output: 
```
{
    "Response": {
        "RequestId": "19a7fb07-8e21-4827-88dd-fee57f38e8cd",
        "Tasks": [
            {
                "EndTime": "2019-11-15 14:25:46",
                "InstanceId": "crs-opcazbrb",
                "InstanceName": "multidbccbugfix11153",
                "Progress": 1,
                "ProjectId": 0,
                "Result": 2,
                "StartTime": "2019-11-15 14:25:37",
                "TaskId": 42372,
                "TaskType": "037"
            },
            {
                "EndTime": "2019-11-15 14:25:25",
                "InstanceId": "crs-opcazbrb",
                "InstanceName": "multidbccbugfix11153",
                "Progress": 1,
                "ProjectId": 0,
                "Result": 2,
                "StartTime": "2019-11-15 14:25:16",
                "TaskId": 42371,
                "TaskType": "037"
            }
        ],
        "TotalCount": 2
    }
}
```

