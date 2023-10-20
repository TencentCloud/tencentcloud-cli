**Example 1: 查询迁移任务详情**

查询迁移任务详情

Input: 

```
tccli tdmq DescribeRocketMQSmoothMigrationTask --cli-unfold-argument  \
    --TaskId 700000780519-o4n3m5g97wgr-3391d15d
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "AccessKey": "",
        "ClusterId": "rocketmq-o4n3m5g97wgr",
        "ConnectionType": "PUBLIC",
        "EnableACL": false,
        "RequestId": "62a5410a-3d9b-486a-98fb-8cb23eb89072",
        "SecretKey": "",
        "SourceClusterName": "abcdfe",
        "SourceClusterNameServer": "222.212.253.122:9876",
        "SubnetId": "",
        "TaskError": null,
        "TaskId": "700000780519-o4n3m5g97wgr-3391d15d",
        "TaskName": "mm-demo3",
        "TaskStatus": "ServiceMigration",
        "TopicStageDistribution": [
            {
                "Count": 1,
                "Stage": "S_RW_D_NA"
            },
            {
                "Count": 1,
                "Stage": "S_RW_D_R"
            },
            {
                "Count": 0,
                "Stage": "S_RW_D_RW"
            },
            {
                "Count": 1,
                "Stage": "S_R_D_RW"
            },
            {
                "Count": 0,
                "Stage": "S_NA_D_RW"
            }
        ],
        "TopicTypeDistribution": [
            {
                "Count": 3,
                "TopicType": "Normal"
            },
            {
                "Count": 0,
                "TopicType": "PartitionedOrder"
            },
            {
                "Count": 0,
                "TopicType": "Transaction"
            },
            {
                "Count": 0,
                "TopicType": "DelayScheduled"
            },
            {
                "Count": 0,
                "TopicType": "Retry"
            },
            {
                "Count": 0,
                "TopicType": "DeadLetter"
            }
        ],
        "VpcId": ""
    }
}
```

