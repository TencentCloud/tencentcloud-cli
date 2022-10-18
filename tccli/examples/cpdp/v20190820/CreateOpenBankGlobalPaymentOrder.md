**Example 1: 订单已受理**

订单已受理

Input: 

```
tccli cpdp CreateOpenBankGlobalPaymentOrder --cli-unfold-argument  \
    --ChannelMerchantId CM641220368383868928 \
    --ChannelName CNP \
    --OutOrderId test21210337 \
    --TotalAmount 1000 \
    --PayType CREDIT_GATEWAY \
    --NotifyUrl http://127.0.0.1/pay/notfiy \
    --FrontLanguage zh \
    --Remark test \
    --Currency HKD \
    --FrontUrl http://127.0.0.1/pay/notfiy \
    --GoodsInfos.0.Sku 123121 \
    --GoodsInfos.0.GoodsName test测试 \
    --GoodsInfos.0.Price 113.9989 \
    --GoodsInfos.0.Quantity 800 \
    --GoodsInfos.0.ProductImage imageUrl \
    --GoodsInfos.0.ProductUrl goodsUrl \
    --ShippingInfo.AddressOne 广东省广州市测试 测试 测试测试 测试 测试* \
    --ShippingInfo.AddressTwo 广东省广州市测试 Another \
    --ShippingInfo.City shagnhai \
    --ShippingInfo.Country CN \
    --ShippingInfo.FirstName Peter 三 \
    --ShippingInfo.LastName zh张 \
    --ShippingInfo.Phone 1231230080 \
    --ShippingInfo.State shagnhai \
    --ShippingInfo.ZipCode 440000 \
    --BillingInfo.AddressOne 广东省广州市测试 测试 测试测试 测试 测试* \
    --BillingInfo.AddressTwo 广东省广州市测试 测试 测试测试 测试RRRRRRRRRR \
    --BillingInfo.City shagnhai \
    --BillingInfo.Country CN \
    --BillingInfo.FirstName 杰伦 \
    --BillingInfo.LastName 周 \
    --BillingInfo.Phone 1231230080 \
    --BillingInfo.State shanghai \
    --BillingInfo.ZipCode 440000 \
    --ExternalPaymentData {"Email":"961836760@qq.com"}
```

Output: 
```
{
    "Response": {
        "RequestId": "1",
        "Result": {
            "OutOrderId": "test21210337",
            "ChannelOrderId": "657611110534541312",
            "ThirdPayOrderId": null,
            "RedirectInfo": {
                "Url": "https://test.allinpayhk.com/pay-web-h5/cnp_payxxxx",
                "ExpireTime": null,
                "MpPath": null,
                "MpAppId": null,
                "MpUserName": null,
                "FormInfo": null,
                "QRCodeUrl": null,
                "QRCodeKey": null
            },
            "PayInfo": null,
            "PayInfoType": null
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

