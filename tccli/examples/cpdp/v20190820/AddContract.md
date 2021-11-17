**Example 1: 添加合同接口成功示例**

添加合同接口成功

Input: 

```
tccli cpdp AddContract --cli-unfold-argument  \
    --OpenId f2cc268b9c95fbbb230a19397fe35f8d \
    --OpenKey e30051d527bd4e621e7090c9392739ec \
    --OutContractId C0001 \
    --MerchantNo M0001 \
    --Code 11111 \
    --SignName 北极星 \
    --SignDate 2019-9-9 \
    --SignMan 张三 \
    --StartDate 2019-9-9 \
    --EndDate 2029-9-9 \
    --Contact 张三 \
    --ContactTelephone 13800138000 \
    --AutoSign 0 \
    --PictureOne 201901/123456.jpg \
    --PaymentId 0 \
    --PaymentClassificationId 03-1 \
    --Fee 0.32 \
    --PaymentClassificationLimit 0 \
    --PictureTwo 201901/123456.jpg \
    --PaymentOptionOne open_id \
    --PaymentOptionTwo open_key \
    --PaymentOptionThree 九江银行商户号 \
    --PaymentOptionFour 微信子商户号 \
    --PaymentOptionFive 微信子商户号 \
    --PaymentOptionSix 微信子商户号 \
    --PaymentOptionSeven 微信子商户号 \
    --PaymentOptionOther 微信子商户号 \
    --PaymentOptionNine 微信子商户号 \
    --PaymentOptionTen 微信子商户号 \
    --ChannelExtJson {"__category_id":"120102","__category_id_select":["天津","天津市","河东区"],"__mcc":"5811","__mcc_select":["餐娱类","包办伙食、宴会承包商"],"__mcht_type":"00","__mcht_type_select":["总店"],"__merchant_type":"00","__merchant_type_select":["否"]}
```

Output: 
```
{
    "Response": {
        "RequestId": null,
        "ErrCode": "0",
        "ErrMessage": "提交成功",
        "Result": {
            "ContractId": "C0001"
        }
    }
}
```

