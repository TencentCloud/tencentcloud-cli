**Example 1: 从云联网撤销**

从云联网撤销路由

Input: 

```
tccli vpc WithdrawNotifyRoutes --cli-unfold-argument  \
    --RouteTableId rtb-9wzwlnhc \
    --RouteItemIds rti-i8bap903
```

Output: 
```
{
    "Response": {
        "RequestId": "627c2362-890f-4f9e-9158-5e457b80d48b"
    }
}
```

