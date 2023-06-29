**Example 1: 重新部署边缘单元指定Grid下应用**



Input: 

```
tccli iecp DeleteEdgeUnitDeployGridItem --cli-unfold-argument  \
    --EdgeUnitId 8367274 \
    --GridItemName logo-dg-privileged1111-logofox \
    --Namespace default \
    --WorkloadKind DeploymentGrid
```

Output: 
```
{
    "Response": {
        "RequestId": "5ebf13a2-f925-4ba7-adff-ddbc21d355e3"
    }
}
```

