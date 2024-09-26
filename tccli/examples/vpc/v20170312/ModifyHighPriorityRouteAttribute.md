**Example 1: 修改高优路由表条目属性**

修改高优路由表条目属性

Input: 

```
tccli vpc ModifyHighPriorityRouteAttribute --cli-unfold-argument  \
    --HighPriorityRouteTableId hprtb-hd4tl8cg \
    --HighPriorityModifyItems.0.HighPriorityRouteId hprti-896n82of \
    --HighPriorityModifyItems.0.Description ivan_test
```

Output: 
```
{
    "Response": {
        "RequestId": "a1802b6d-a956-4303-a3c7-515e4b5b2b19"
    }
}
```

