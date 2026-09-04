**Example 1: 查询队列的弹性伸缩历史记录**

按照队列名称进行过滤

Input: 

```
tccli thpc DescribeClusterActivities --cli-unfold-argument  \
    --ClusterId hpc-k2uwxvhn \
    --Offset 0 \
    --Limit 20 \
    --Filters.0.Name queue-name \
    --Filters.0.Values compute
```

Output: 
```
{
    "Response": {
        "ClusterActivitySet": [
            {
                "ActivityId": "cha-m9uxy80u",
                "ActivityStatus": "SUCCESSFUL",
                "ActivityStatusCode": "ActivitySuccess",
                "ActivityType": "CreateAndAddNodes",
                "Cause": "AutoScaleOut",
                "ClusterId": "hpc-k2uwxvhn",
                "Description": "弹性扩容，创建实例并添加进集群，队列：compute 增加 2个节点，总共扩容2个节点。",
                "EndTime": "2026-08-31T03:51:51Z",
                "QueueName": "compute",
                "RelatedNodeActivitySet": [
                    {
                        "NodeActivityStatus": "SUCCESSFUL",
                        "NodeActivityStatusCode": "ActivitySuccess",
                        "NodeActivityStatusReason": "Activity success.",
                        "NodeInstanceId": "ins-7236kgtn"
                    }
                ],
                "ResultDetail": "Activity success.",
                "StartTime": "2026-08-31T03:49:33Z"
            }
        ],
        "TotalCount": 1,
        "RequestId": "4e4ec467-cfa6-4212-9c1f-0c548278a43e"
    }
}
```

**Example 2: 查询集群活动历史记录**

根据集群ID查询集群活动历史记录。

Input: 

```
tccli thpc DescribeClusterActivities --cli-unfold-argument  \
    --ClusterId hpc-0yd8fqsc \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "ClusterActivitySet": [
            {
                "ClusterId": "hpc-myd8fgsc",
                "ActivityId": "cha-gvzj0zbd",
                "ActivityType": "TerminateNodes",
                "ActivityStatus": "SUCCESSFUL",
                "ActivityStatusCode": "ActivitySuccess",
                "ResultDetail": "Activity success.",
                "Cause": "DeleteCluster",
                "QueueName": "compute",
                "Description": "删除指定集群，销毁实例，销毁所有节点。",
                "RelatedNodeActivitySet": [
                    {
                        "NodeInstanceId": "ins-1zll2of0",
                        "NodeActivityStatus": "SUCCESSFUL",
                        "NodeActivityStatusCode": "ActivitySuccess",
                        "NodeActivityStatusReason": "Activity success."
                    },
                    {
                        "NodeInstanceId": "ins-ig2bew40",
                        "NodeActivityStatus": "SUCCESSFUL",
                        "NodeActivityStatusCode": "ActivitySuccess",
                        "NodeActivityStatusReason": "Activity success."
                    }
                ],
                "StartTime": "2021-11-01T02:17:20Z",
                "EndTime": "2021-11-01T02:17:38Z"
            }
        ],
        "TotalCount": 1,
        "RequestId": "7fa864e6-cf1a-4962-8aa9-f68abfa31a00"
    }
}
```

