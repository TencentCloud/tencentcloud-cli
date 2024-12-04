**Example 1: 添加企业组织单元**



Input: 

```
tccli organization AddOrganizationNode --cli-unfold-argument  \
    --ParentNodeId 101 \
    --Name "test"
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

