**Example 1: 删除策略的关联对象**



Input: 

```
tccli monitor UnBindingPolicyObject --cli-unfold-argument  \
    --UniqueId 3dd5113208fd467b2e5d0c1111111111 \
    --GroupId 11111 \
    --Module monitor
```

Output: 
```
{
    "Response": {
        "RequestId": "0dbb66c2-1111-1111-1111-11111111111"
    }
}
```

