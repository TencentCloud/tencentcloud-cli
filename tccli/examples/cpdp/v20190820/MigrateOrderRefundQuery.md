**Example 1: 查询退款状态接口请求示例**

此接口适用于查询退款结果的场景。

Input: 

```
tccli cpdp MigrateOrderRefundQuery --cli-unfold-argument  \
    --MerchantId 商户号 \
    --PayChannel 支付渠道 \
    --RefundOrderId refund1212112 \
    --TradeSerialNo 106776467648827392
```

Output: 
```
{
    "Response": {
        "RequestId": "0b159749-5a42-4a6f-92cb-77961d755fb2",
        "IsSuccess": true,
        "TradeSerialNo": "106776467648827392",
        "TradeMsg": "成功",
        "TradeStatus": 2,
        "ThirdChannelOrderId": "2020072922001405871428466841"
    }
}
```

