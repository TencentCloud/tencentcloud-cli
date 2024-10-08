**Example 1: 替换高优路由表和子网绑定关系**

替换高优路由表和子网绑定关系

Input: 

```
tccli vpc ReplaceHighPriorityRouteTableAssociation --cli-unfold-argument  \
    --HighPriorityRouteTableId hprtb-hd4tl8cg \
    --SubnetId subnet-a9pjzfq0
```

Output: 
```
{
    "Response": {
        "RequestId": "14095a9f-1411-4a0e-966a-32da69f58db7"
    }
}
```

