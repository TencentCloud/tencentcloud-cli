**Example 1: 查询合同明细接口成功示例**

查询合同明细接口成功

Input: 

```
tccli cpdp ViewContract --cli-unfold-argument  \
    --OpenId f2cc268b9c95fbbb230a19397fe35f8d \
    --OpenKey e30051d527bd4e621e7090c9392739ec \
    --ContractId TestC115
```

Output: 
```
{
    "Response": {
        "RequestId": null,
        "ErrCode": "0",
        "ErrMessage": "提交成功",
        "Result": {
            "ContractId": "301385",
            "Code": "123456",
            "StartDate": "2016-11-01",
            "EndDate": "2017-11-01",
            "PaymentId": "13",
            "PaymentType": "2",
            "PaymentTag": "WeixinJJYH",
            "PaymentName": "微信支付",
            "PaymentInternalName": "微信支付(九江银行)",
            "PaymentClassificationId": "38",
            "PaymentClassificationName": "线下实体商户",
            "Fee": "0.32",
            "PaymentClassificationLimit": "0",
            "MerchantNo": "20743873",
            "MerchantName": "API进件测试的商户",
            "BrandName": "招牌名称",
            "Province": "北京",
            "City": "北京",
            "Country": "东城区",
            "CityId": "110101",
            "Address": "南山区科技园科苑大道讯美科技广场2栋12楼",
            "AddTime": "2016-12-06 15:37:34",
            "UpdateTime": "2016-12-06 15:41:04",
            "OutContractId": "123456",
            "SignDate": "2016-11-01",
            "ShopCount": "1",
            "AutoSign": "1",
            "Status": "0",
            "PictureOne": "201601/123456.jpg",
            "PictureTwo": "201601/123456.jpg"
        }
    }
}
```

