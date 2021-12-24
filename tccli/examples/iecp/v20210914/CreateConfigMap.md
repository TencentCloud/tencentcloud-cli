**Example 1: CreateConfigMap**



Input: 

```
tccli iecp CreateConfigMap --cli-unfold-argument  \
    --EdgeUnitID 1 \
    --ConfigMapName test \
    --ConfigMapNamespace default \
    --ConfigMapData.0.Key username \
    --ConfigMapData.0.Value iecp
```

Output: 
```
{
    "Response": {
        "RequestId": "72d540a0-ed11-4370-b977-96c6c224a1d8"
    }
}
```

