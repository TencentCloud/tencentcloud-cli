**Example 1: 购买图片并且支付订单**



Input: 

```
tccli ape CreateOrderAndPay --cli-unfold-argument  \
    --ImageId 4723211 \
    --AuthUserId apur-10xxxxx \
    --MarshalId 2
```

Output: 
```
{
    "Response": {
        "RequestId": "s1589767450135506558",
        "OrderId": "ord_001"
    }
}
```

