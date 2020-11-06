**Example 1: 查询ES集群实例操作记录**



Input: 

```
tccli es DescribeInstanceOperations --cli-unfold-argument  \
    --InstanceId es-f5mwm28u \
    --StartTime '2019-01-30 20:18:03' \
    --EndTime '2019-03-30 20:18:03' \
    --Offset 0 \
    --Limit 30
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Operations": [
            {
                "Id": 6173,
                "StartTime": "2019-03-07 16:30:39",
                "Type": "CreateInstance",
                "Detail": {
                    "OldInfo": [],
                    "NewInfo": []
                },
                "Result": "completed",
                "Tasks": [
                    {
                        "Name": "prepareResource",
                        "Progress": 1,
                        "FinishTime": "2019-03-07 16:31:11",
                        "SubTasks": []
                    },
                    {
                        "Name": "deployESCluster",
                        "Progress": 1,
                        "FinishTime": "2019-03-07 16:34:32",
                        "SubTasks": []
                    },
                    {
                        "Name": "deployKibana",
                        "Progress": 1,
                        "FinishTime": "2019-03-07 16:35:13",
                        "SubTasks": []
                    },
                    {
                        "Name": "configLB",
                        "Progress": 1,
                        "FinishTime": "2019-03-07 16:35:15",
                        "SubTasks": []
                    }
                ],
                "Progress": 1
            }
        ],
        "RequestId": "870dd618-b1ae-40cc-a5a9-22b867367ed7"
    }
}
```

