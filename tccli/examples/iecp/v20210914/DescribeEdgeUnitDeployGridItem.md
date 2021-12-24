**Example 1: 查询边缘单元指定Grid下的部署列表**



Input: 

```
tccli iecp DescribeEdgeUnitDeployGridItem --cli-unfold-argument  \
    --EdgeUnitId 8367274 \
    --GridName logo-dg-privileged1111 \
    --Namespace default \
    --WorkloadKind DeploymentGrid \
    --Order ASC
```

Output: 
```
{
    "Response": {
        "RequestId": "5ebf13a2-f925-4ba7-adff-ddbc21d355e3",
        "TotalCount": 2,
        "DeploySet": [
            {
                "Name": "logo-dg-privileged1111-logofox",
                "Replicas": 1,
                "AvailableReplicas": 1,
                "StartTime": "2021-07-06 10:43:00",
                "WorkloadKind": "Deployment"
            },
            {
                "Name": "logo-dg-privileged1111-dev005",
                "Replicas": 1,
                "AvailableReplicas": 1,
                "StartTime": "2021-07-06 14:03:46",
                "WorkloadKind": "Deployment"
            }
        ]
    }
}
```

