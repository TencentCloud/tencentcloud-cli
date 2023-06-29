**Example 1: 批量预添加节点**



Input: 

```
tccli iecp CreateEdgeNodeBatch --cli-unfold-argument  \
    --Nodes.0.Remark 20220911 \
    --Nodes.0.SN SN2232323 \
    --Nodes.0.Name snnode \
    --EdgeUnitId 100026
```

Output: 
```
{
    "Response": {
        "RequestId": "82b8436a-1d51-4e33-8036-6a6c5b854056"
    }
}
```

