**Example 1: 修改路由接收策略属性。**

修改路由接收策略属性。

Input: 

```
tccli vpc ModifyRoutePolicyAttribute --cli-unfold-argument  \
    --RoutePolicyId rrp-n0qp4w5a \
    --RoutePolicyName TEST \
    --RoutePolicyDescription TEST
```

Output: 
```
{
    "Response": {
        "RequestId": "49a4e5e2-28d6-492c-ac6b-55192e7dd29b"
    }
}
```

