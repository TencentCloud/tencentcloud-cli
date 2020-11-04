**Example 1: 存量订单退款请求**

用于系统迁移时存量订单退款

Input: 

```
tccli cpdp MigrateOrderRefund --cli-unfold-argument  \
    --MerchantId 商户号\
    --PayAmt 123\
    --PayChannel 支付渠道\
    --PayOrderId 1023232989\
    --RefundAmt 10\
    --RefundOrderId 9\
    --ThirdChannelOrderId 123230902323899
```

Output: 
```
{
    "Response": {
        "RequestId": "b0e17cc6-8404-4403-bc46-944fc7b9f93f",
        "IsSuccess": true,
        "TradeSerialNo": "106776467648827392",
        "TradeMsg": "请求成功"
    }
}
```

