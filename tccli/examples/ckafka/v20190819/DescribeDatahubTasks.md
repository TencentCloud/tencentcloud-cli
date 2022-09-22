**Example 1: 查询Datahub任务列表**



Input: 

```
tccli ckafka DescribeDatahubTasks --cli-unfold-argument  \
    --TaskType SINK \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 0,
            "TaskList": [
                {
                    "Status": 0,
                    "TaskId": "xx",
                    "TaskName": "MyTaskName",
                    "TaskType": "SINK",
                    "SourceResource": {
                        "Type": "KAFKA",
                        "KafkaParam": {
                            "SelfBuilt": false,
                            "Resource": "ckafka-7kd5rzza",
                            "Topic": "topic-test",
                            "OffsetType": "timestamp",
                            "StartTime": 1635339533,
                            "ResourceName": "MyCkafkaName",
                            "ZoneId": 200005
                        }
                    },
                    "TargetResource": {
                        "Type": "EB",
                        "EventBusParam": {
                            "Type": "COS",
                            "SelfBuilt": false,
                            "Resource": "target-resource",
                            "Namespace": "default",
                            "FunctionName": "ckafka-7kd5rzza_topic-0cus2p9z_task_1633501781881_schedule",
                            "Qualifier": "$LATEST"
                        }
                    }
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

