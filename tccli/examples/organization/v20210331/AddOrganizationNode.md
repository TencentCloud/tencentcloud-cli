**Example 1: 添加企业组织节点**



Input: 

```
tccli organization AddOrganizationNode --cli-unfold-argument  \
    --Name node_name \
    --ParentNodeId 101
```

Output: 
```
{
    "Response": {
        "NodeId": 1001,
        "RequestId": "b46d2afe-6893-4529-bc96-2c82d9214957"
    }
}
```

