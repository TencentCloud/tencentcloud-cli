**Example 1: 续费 DB Custom 节点**



Input: 

```
tccli dbdc RenewDBCustomNode --cli-unfold-argument  \
    --NodeId dbcn-wamuy21e \
    --Period 1 \
    --AutoRenew 2 \
    --AutoVoucher 1 \
    --VoucherIds OZRCGNAVHYEQPQUVPZWIHD
```

Output: 
```
{
    "Response": {
        "RequestId": "55246970-8cf2-4a5a-a817-ef71d6777d08"
    }
}
```

