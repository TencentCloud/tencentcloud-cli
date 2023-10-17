**Example 1: 获取迁移任务列表**

获取迁移任务列表

Input: 

```
tccli tdmq DescribeRocketMQSmoothMigrationTaskList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Data": [
            {
                "ClusterId": "rocketmq-3jaer4odmx52",
                "ConnectionType": "PUBLIC",
                "SourceClusterName": "222",
                "SourceNameServer": "",
                "TaskId": "700000780519-3jaer4odmx52-7f0df1dc",
                "TaskName": "稳定稳定",
                "TaskStatus": "Configuration"
            },
            {
                "ClusterId": "rocketmq-og9vpdx3vwn3",
                "ConnectionType": "VPC",
                "SourceClusterName": "test111",
                "SourceNameServer": "109.0.15.17:9876",
                "TaskId": "700000780519-og9vpdx3vwn3-2e17057b",
                "TaskName": "test111",
                "TaskStatus": "ServiceMigration"
            },
            {
                "ClusterId": "rocketmq-o4n3m5g97wgr",
                "ConnectionType": "PUBLIC",
                "SourceClusterName": "abcdfe",
                "SourceNameServer": "123.12.53.222:9876",
                "TaskId": "700000780519-o4n3m5g97wgr-3391d15d",
                "TaskName": "mm-demo3",
                "TaskStatus": "ServiceMigration"
            },
            {
                "ClusterId": "rocketmq-q5zm4gwd9x2j",
                "ConnectionType": "VPC",
                "SourceClusterName": "test",
                "SourceNameServer": "",
                "TaskId": "700000780519-q5zm4gwd9x2j-744ea9ec",
                "TaskName": "test11",
                "TaskStatus": "Configuration"
            },
            {
                "ClusterId": "rocketmq-o3dr5om3qn3",
                "ConnectionType": "PUBLIC",
                "SourceClusterName": "aaaa",
                "SourceNameServer": "192.111.13.100:9876",
                "TaskId": "700000780519-o3dr5om3qn3-61be55a8",
                "TaskName": "aaaa",
                "TaskStatus": "ServiceMigration"
            },
            {
                "ClusterId": "rocketmq-q5zm4gwd9x2j",
                "ConnectionType": "PUBLIC",
                "SourceClusterName": "abccdddf",
                "SourceNameServer": "156.129.53.64:9876",
                "TaskId": "700000780519-q5zm4gwd9x2j-107430a9",
                "TaskName": "demo-test-2",
                "TaskStatus": "Completed"
            },
            {
                "ClusterId": "rocketmq-q5zm4gwd9x2j",
                "ConnectionType": "PUBLIC",
                "SourceClusterName": "abcdef",
                "SourceNameServer": "156.222.32.222:9876",
                "TaskId": "700000780519-q5zm4gwd9x2j-2a97516c",
                "TaskName": "demo",
                "TaskStatus": "Completed"
            },
            {
                "ClusterId": "rocketmq-a87e43zd7k72",
                "ConnectionType": "PUBLIC",
                "SourceClusterName": "abcdef",
                "SourceNameServer": "222.222.122.22:9876",
                "TaskId": "700000780519-a87e43zd7k72-09bc951a",
                "TaskName": "test-acl",
                "TaskStatus": "SourceConnectionFailure"
            },
            {
                "ClusterId": "rocketmq-q5zm4gwd9x2j",
                "ConnectionType": "PUBLIC",
                "SourceClusterName": "demo-show",
                "SourceNameServer": "222.122.253.24:9876",
                "TaskId": "700000780519-q5zm4gwd9x2j-5af2d7d1",
                "TaskName": "demo-show",
                "TaskStatus": "Completed"
            },
            {
                "ClusterId": "rocketmq-8j8mg3zqoxwn",
                "ConnectionType": "PUBLIC",
                "SourceClusterName": "test-new",
                "SourceNameServer": "222.222.102.236:9876",
                "TaskId": "700000780519-8j8mg3zqoxwn-ccd6c766",
                "TaskName": "test-new",
                "TaskStatus": "ServiceMigration"
            }
        ],
        "RequestId": "4070a143-3df6-4018-b1a4-838966a0bc01",
        "TotalCount": 11
    }
}
```

