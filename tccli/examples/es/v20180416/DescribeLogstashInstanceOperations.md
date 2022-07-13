**Example 1: 查询Logstash实例操作记录**



Input: 

```
tccli es DescribeLogstashInstanceOperations --cli-unfold-argument  \
    --InstanceId ls-f5mwm28u \
    --StartTime '2021-01-05 20:18:03' \
    --EndTime '2021-01-05 20:28:03' \
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
                "StartTime": "2021-01-05 20:25:39",
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
                        "FinishTime": "2021-01-05 20:27:39",
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

