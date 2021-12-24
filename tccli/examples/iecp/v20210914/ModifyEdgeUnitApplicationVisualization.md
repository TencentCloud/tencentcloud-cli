**Example 1: ModifyEdgeUnitApplicationVisualization**



Input: 

```
tccli iecp ModifyEdgeUnitApplicationVisualization --cli-unfold-argument  \
    --BasicConfig.Name app \
    --BasicConfig.Namespace Default \
    --BasicConfig.WorkflowKind Deployment \
    --EdgeUnitId 1 \
    --ApplicationId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "5ebf13a2-f925-4ba7-adff-ddbc21d355e3"
    }
}
```

