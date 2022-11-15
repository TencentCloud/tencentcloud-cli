**Example 1: 添加企业组织节点**



Input: 

```
tccli organization AddOrganizationNode --cli-unfold-argument  \
    --Name test \
    --ParentNodeId 123
```

Output: 
```
{
    "Response": {
        "NodeId": 1123,
        "RequestId": "b46d2afe-6893-4529-bc96-2c82d9214957"
    }
}
```

