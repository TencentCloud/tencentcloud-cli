**Example 1: 查询workload类型的影响范围示例**



Input: 

```
tccli tcss DescribeAffectedWorkloadList --cli-unfold-argument  \
    --CheckItemId 10071 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "AffectedWorkloadList": [
            {
                "ClusterId": "test-clusterid",
                "ClusterName": "benben-tcss",
                "Region": "ap-guangzhou",
                "VerifyInfo": "yunjing-agent set image tag \"latest\"",
                "WorkloadName": "tcss/yunjing-agent",
                "WorkloadType": "DaemonSet"
            }
        ],
        "RequestId": "299deeb1-48aa-449d-980c-1f46e2375cec",
        "TotalCount": 111
    }
}
```

