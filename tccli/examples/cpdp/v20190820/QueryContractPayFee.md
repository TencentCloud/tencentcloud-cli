**Example 1: 查询支付方式费率及自定义表单项接口成功示例**

查询支付方式费率及自定义表单项接口成功

Input: 

```
tccli cpdp QueryContractPayFee --cli-unfold-argument  \
    --OpenId f2cc268b9c95fbbb230a19397fe35f8d \
    --OpenKey e30051d527bd4e621e7090c9392739ec \
    --PaymentId 21
```

Output: 
```
{
    "Response": {
        "RequestId": "171304d7-1084-4c98-9baa-fa1e8d2af7d0",
        "ErrCode": "0",
        "ErrMessage": "提交成功",
        "Result": {
            "Pay": {
                "PaymentId": "21",
                "PaymentType": "2,3,4",
                "PaymentTag": "Weixin",
                "PaymentName": "微信",
                "PaymentInternalName": "微信支付（九江银行）",
                "PaymentIcon": "2017/a61611233156.jpg",
                "PaymentDiscountFee": "日期"
            },
            "PayFee": [
                {
                    "PaymentClassificationId": "13",
                    "PaymentClassificationName": "线下实体商户",
                    "PaymentClassificationMinFee": "0.200",
                    "PaymentClassificationMaxFee": "0.600",
                    "PaymentClassificationLimit": "0",
                    "OrganizationFeeType": "1",
                    "OrganizationFee": "0.200"
                }
            ],
            "ExtraInput": "无"
        }
    }
}
```

