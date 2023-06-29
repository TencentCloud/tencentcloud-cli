**Example 1: 查询集群活动历史记录**

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

