**Example 1: 查询边缘单元Grid的Pod列表**



Input: 

```
tccli iecp DescribeEdgeUnitGridPods --cli-unfold-argument  \
    --EdgeUnitId 100020 \
    --GridName sasas-grid \
    --Namespace default \
    --WorkloadKind DeploymentGrid \
    --NodeUnit sasas-grid-ddd-zone
```

Output: 
```
{
    "Response": {
        "RequestId": "5ebf13a2-f925-4ba7-adff-ddbc21d355e3",
        "PodSet": [
            {
                "Name": "test2-grid-test1-zone-cb5b845f7-sk8qw",
                "NameSpace": "default",
                "Status": "Pending",
                "NodeName": "node3",
                "NodeIP": "172.21.7.3",
                "PodIP": "",
                "StartTime": "2021-08-23 16:49:18",
                "RunSec": 2004,
                "RestartCount": 0
            }
        ]
    }
}
```

