**Example 1: Adding an organizational unit**



Input: 

```
tccli organization AddOrganizationNode --cli-unfold-argument  \
    --ParentNodeId 123\
    --Name "test"
```

Output: 
```
{
    "Response": {
        "NodeId": 123,
        "RequestId": "b46d2afe-6893-4529-bc96-2c82d9214957"
    }
}
```

