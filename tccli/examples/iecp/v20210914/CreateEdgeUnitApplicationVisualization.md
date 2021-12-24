**Example 1: CreateEdgeUnitApplicationVisualization**



Input: 

```
tccli iecp CreateEdgeUnitApplicationVisualization --cli-unfold-argument  \
    --BasicInfo.Name app \
    --BasicInfo.Description test \
    --BasicConfig.Name app \
    --BasicConfig.Namespace Default \
    --BasicConfig.WorkflowKind Deployment \
    --EdgeUnitId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "5ebf13a2-f925-4ba7-adff-ddbc21d355e3",
        "ApplicationId": 1
    }
}
```

