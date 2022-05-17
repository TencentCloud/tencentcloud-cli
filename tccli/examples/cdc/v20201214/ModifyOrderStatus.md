**Example 1: 修改订单状态**

修改订单状态

Input: 

```
tccli cdc ModifyOrderStatus --cli-unfold-argument  \
    --DedicatedClusterOrderId ord-aijx4ets \
    --SubOrderIds sord-aijxdfasdf \
    --Status 1
```

Output: 
```
{
    "Response": {
        "RequestId": "c1097ff7-eead-47de-bb86-2b9d88d29175"
    }
}
```

