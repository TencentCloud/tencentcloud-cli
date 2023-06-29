**Example 1: 修改边缘单元Grid部署项副本数**



Input: 

```
tccli iecp ModifyEdgeUnitDeployGridItem --cli-unfold-argument  \
    --EdgeUnitId 8367274 \
    --GridItemName logo-dg-privileged1111-logofox \
    --WorkloadKind DeploymentGrid \
    --Namespace default \
    --Replicas 0
```

Output: 
```
{
    "Response": {
        "RequestId": "5ebf13a2-f925-4ba7-adff-ddbc21d355e3"
    }
}
```

