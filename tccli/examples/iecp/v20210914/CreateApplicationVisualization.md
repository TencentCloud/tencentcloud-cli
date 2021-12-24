**Example 1: 创建应用模板**



Input: 

```
tccli iecp CreateApplicationVisualization --cli-unfold-argument  \
    --BasicInfo.Name app \
    --BasicInfo.Description test \
    --BasicConfig.Name app \
    --BasicConfig.Namespace Default \
    --BasicConfig.WorkflowKind Deployment
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

