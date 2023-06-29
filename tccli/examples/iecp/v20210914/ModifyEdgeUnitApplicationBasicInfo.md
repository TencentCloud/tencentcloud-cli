**Example 1: ModifyEdgeUnitApplicationBasicInfo**



Input: 

```
tccli iecp ModifyEdgeUnitApplicationBasicInfo --cli-unfold-argument  \
    --BasicInfo.Name app \
    --BasicInfo.Description test \
    --ApplicationId 1 \
    --EdgeUnitId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "5ebf13a2-f925-4ba7-adff-ddbc21d355e3"
    }
}
```

