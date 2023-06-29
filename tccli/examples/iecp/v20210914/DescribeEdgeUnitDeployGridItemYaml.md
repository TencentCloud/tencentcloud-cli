**Example 1: 查询指定Grid部署项的Yaml**



Input: 

```
tccli iecp DescribeEdgeUnitDeployGridItemYaml --cli-unfold-argument  \
    --EdgeUnitId 8367274 \
    --GridItemName logo-dg-privileged1111-logofox \
    --WorkloadKind DeploymentGrid \
    --Namespace default
```

Output: 
```
{
    "Response": {
        "RequestId": "5ebf13a2-f925-4ba7-adff-ddbc21d355e3",
        "Yaml": "XXXX",
        "Replicas": 7
    }
}
```

