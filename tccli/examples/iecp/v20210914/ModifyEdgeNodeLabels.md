**Example 1: 编辑边缘节点标签**



Input: 

```
tccli iecp ModifyEdgeNodeLabels --cli-unfold-argument  \
    --EdgeUnitId 8367274 \
    --NodeId 2 \
    --Labels.0.Key nvidia-device-enable \
    --Labels.0.Value true \
    --Labels.1.Key superedge.io/edge-node \
    --Labels.1.Value enable
```

Output: 
```
{
    "Response": {
        "RequestId": "7c59b432-1f22-4442-8f18-85d2a4bd4a90"
    }
}
```

