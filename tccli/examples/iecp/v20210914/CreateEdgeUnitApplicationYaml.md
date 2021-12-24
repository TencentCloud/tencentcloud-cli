**Example 1: CreateEdgeUnitApplicationYaml**



Input: 

```
tccli iecp CreateEdgeUnitApplicationYaml --cli-unfold-argument  \
    --BasicInfo.Name app \
    --BasicInfo.Description test \
    --EdgeUnitId 1 \
    --Yaml 
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

