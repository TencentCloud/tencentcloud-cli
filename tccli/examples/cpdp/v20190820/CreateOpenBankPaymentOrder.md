**Example 1: 支付下单成功示例**

支付下单接口成功

Input: 

```
tccli cpdp CreateOpenBankPaymentOrder --cli-unfold-argument  \
    --ChannelMerchantId CM572433237990035456 \
    --ChannelName TENPAY \
    --PaymentMethod EBANK_PAYMENT \
    --OutOrderId test0039 \
    --TotalAmount 2 \
    --PaymentMode DIRECT \
    --NotifyUrl http://127.0.0.1/pay/notify \
    --Remark test \
    --Currency CNY \
    --ExpireTime 2022-02-02 11:10:44 \
    --FrontUrl http://127.0.0.1/pay/redirect \
    --RefreshUrl http://127.0.0.1/pay/refresh \
    --Attachment test123 \
    --ProfitShareFlag NO_NEED_SHARE \
    --GoodsInfo.GoodsName 测试商品 \
    --GoodsInfo.GoodsDetail 测试商品123456 \
    --GoodsInfo.GoodsDescription 测试测试测试测试 \
    --PayerInfo.PayerId test00003 \
    --PayerInfo.PayerName test00003 \
    --PayeeInfo.PayeeId test00002 \
    --PayeeInfo.PayeeName test00002 \
    --SceneInfo.DeviceId deviceId0001 \
    --SceneInfo.PayerClientIp 127.0.0.1 \
    --SceneInfo.PayerUa user agent
```

Output: 
```
{
    "Response": {
        "RequestId": "171304d7-1084-4c98-9baa-fa1e8d2af7d0",
        "ErrCode": "SUCCESS",
        "ErrMessage": "订单提交成功",
        "Result": ""
    }
}
```

**Example 2: 创建订单支付服务系统异常**



Input: 

```
tccli cpdp CreateOpenBankPaymentOrder --cli-unfold-argument  \
    --Remark remark \
    --ChannelName TENPAY \
    --ProfitShareFlag NO_NEED_SHARE \
    --NotifyUrl http://127.0.0.1/pay/notfiy \
    --GoodsInfo.GoodsName 测试商品 \
    --GoodsInfo.GoodsDescription 试测试测试 \
    --GoodsInfo.GoodsDetail 测试商品123456 \
    --PaymentMode DIRECT \
    --PayerInfo.PayerId test00003 \
    --PayerInfo.BindSerialNo test \
    --PayerInfo.PayerName test00003 \
    --RefreshUrl http://127.0.0.1/pay/notfiy \
    --ChannelMerchantId CM572433237990035456 \
    --ExpireTime 2022-02-18 11:10:44 \
    --OutOrderId testyunapi2022021809 \
    --ProfitShareInfoList.0.RecvId test \
    --ProfitShareInfoList.0.ProfitShareFee 1 \
    --SceneInfo.PayerUa user agent \
    --SceneInfo.PayerClientIp 127.0.0.1 \
    --SceneInfo.DeviceId deviceId0001 \
    --PayeeInfo.PayeeId test00002 \
    --PayeeInfo.PayeeName test00002 \
    --PayeeInfo.BankBranchId test \
    --PayeeInfo.BankAccountNumber test \
    --PayeeInfo.BankBranchName test \
    --FrontUrl http://127.0.0.1/pay/notfiy \
    --TotalAmount 1 \
    --Currency CNY \
    --PaymentMethod EBANK_PAYMENT \
    --Attachment test
```

Output: 
```
{
    "Response": {
        "RequestId": "c151fea1-2ad8-4eeb-b27c-a4fca7ed85a7",
        "Result": null,
        "ErrCode": "FailedOperation.SystemError",
        "ErrMessage": "系统未知异常"
    }
}
```

**Example 3: 订单已受理**



Input: 

```
tccli cpdp CreateOpenBankPaymentOrder --cli-unfold-argument  \
    --Remark 123 \
    --ChannelName TENPAY \
    --ProfitShareFlag  \
    --NotifyUrl http://127.0.0.1/pay/notify \
    --GoodsInfo.GoodsDetail 测试0001 \
    --GoodsInfo.GoodsDescription 测试001 \
    --GoodsInfo.GoodsBizType 字符串 \
    --PaymentMode FREEZE \
    --PayerInfo.PayerId CM618130447205666816 \
    --PayerInfo.BindSerialNo 123 \
    --PayerInfo.PayerName 测试 \
    --ChannelMerchantId CM584693967762206720 \
    --ExpireTime 2022-07-02 17:09:44 \
    --OutOrderId 202206270000001 \
    --ProfitShareInfoList.0.RecvId 11 \
    --ProfitShareInfoList.0.ProfitShareFee 1 \
    --SceneInfo.DeviceType GoodsInfo.GoodsName \
    --SceneInfo.PayerUa user agent \
    --SceneInfo.PayerClientIp 127.0.0.1 \
    --SceneInfo.OrderTime  \
    --SceneInfo.DeviceId 0001 \
    --PayeeInfo.BankAccountNumber 20220602170937 \
    --PayeeInfo.BindSerialNo 1002030191514840205164 \
    --PayeeInfo.BankBranchId 301290050123 \
    --PayeeInfo.BankBranchName  \
    --PayeeInfo.PayeeName 测试 \
    --PayeeInfo.PayeeId CM618130426611634176 \
    --TotalAmount 1 \
    --Currency CNY \
    --PaymentMethod EBANK_PAYMENT \
    --Attachment test123
```

Output: 
```
{
    "Response": {
        "RequestId": "c1c1ba98-a977-4ac0-a755-30c006e4a6fa",
        "Result": null,
        "ErrCode": "ORDER.RECORD_ALREADY_EXISTED",
        "ErrMessage": "订单已受理，请使用查询接口确认订单状态"
    }
}
```

