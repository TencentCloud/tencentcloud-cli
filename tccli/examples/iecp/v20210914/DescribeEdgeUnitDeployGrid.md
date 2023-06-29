**Example 1: 查询边缘单元Grid列表**



Input: 

```
tccli iecp DescribeEdgeUnitDeployGrid --cli-unfold-argument  \
    --EdgeUnitId 8367274 \
    --NamePattern  \
    --Limit 30 \
    --Offset 0 \
    --Order DESC
```

Output: 
```
{
    "Response": {
        "RequestId": "03a1b60d-4125-4618-8a52-93a3148be20d",
        "TotalCount": 2,
        "GridSet": [
            {
                "Id": 100166,
                "Name": "deploy-grid",
                "GridUniqKey": "logo-group",
                "Description": "deploy",
                "WorkloadKind": "DeploymentGrid",
                "StartTime": "2021-07-20 11:31:35",
                "Replicas": 0
            },
            {
                "Id": 100165,
                "Name": "sts-grid",
                "GridUniqKey": "logo-group",
                "Description": "",
                "WorkloadKind": "StatefulSetGrid",
                "StartTime": "2021-07-20 11:30:42",
                "Replicas": 0
            }
        ]
    }
}
```

