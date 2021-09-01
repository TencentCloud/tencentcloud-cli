**Example 1: 查询任务列表**

指定任务ID，查询任务详情

Input: 

```
tccli tcaplusdb DescribeTasks --cli-unfold-argument  \
    --ClusterIds 5674209986 \
    --Offset 3 \
    --Limit 3
```

Output: 
```
{
    "Response": {
        "RequestId": "72fc70ce-2396-4b8e-ac54-9bce72058da1",
        "TaskInfos": [
            {
                "ClusterName": "gz测试PROTO",
                "ClusterId": "5674209986",
                "Content": "20548499 modify quotas table(tb_example) of Cluster(5674209986) TableGroup(101), InstanceId tcaplus-1f224454, Storage Layer Expand: volume[1 -> 2], owner 20548499",
                "Operator": "20548499",
                "Progress": 0,
                "StartTime": "2019-08-30 18:16:50",
                "TaskId": "5674209986-1202",
                "TaskType": "ModifyTableQuotas",
                "TransId": "0",
                "UpdateTime": "2019-08-30 18:16:50"
            },
            {
                "ClusterName": "gz测试PROTO",
                "ClusterId": "5674209986",
                "Content": "20548499 modify table(tb_example)'s structure of Cluster(5674209986) TableGroup(101), InstanceId tcaplus-1f224454, owner 20548499",
                "Operator": "20548499",
                "Progress": 100,
                "StartTime": "2019-08-30 18:02:50",
                "TaskId": "5674209986-1200",
                "TaskType": "ModifyTables",
                "TransId": "558",
                "UpdateTime": "2019-08-30 18:02:51"
            },
            {
                "ClusterName": "gz测试PROTO",
                "ClusterId": "5674209986",
                "Content": "20548499 clear table(tb_example) of Cluster(5674209986) TableGroup(101), InstanceId tcaplus-1f224454, owner 20548499",
                "Operator": "20548499",
                "Progress": 0,
                "StartTime": "2019-08-30 17:34:07",
                "TaskId": "5674209986-1199",
                "TaskType": "ClearTables",
                "TransId": "557",
                "UpdateTime": "2019-08-30 17:34:07"
            }
        ],
        "TotalCount": 19
    }
}
```

