**Example 1: 创建边缘单元NodeUnit模板**



Input: 

```
tccli iecp CreateEdgeNodeUnitTemplate --cli-unfold-argument  \
    --EdgeUnitId 8367274 \
    --Name auto-code1 \
    --Namespace default \
    --Nodes logofox node2 dev00311 \
    --Description Description
```

Output: 
```
{
    "Response": {
        "RequestId": "5ebf13a2-f925-4ba7-adff-ddbc21d355e3"
    }
}
```

