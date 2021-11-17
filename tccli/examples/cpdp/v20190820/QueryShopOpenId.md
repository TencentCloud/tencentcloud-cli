**Example 1: 获取门店OpenId接口成功示例**

获取门店OpenId接口成功

Input: 

```
tccli cpdp QueryShopOpenId --cli-unfold-argument  \
    --OpenId f2cc268b9c95fbbb230a19397fe35f8d \
    --OpenKey e30051d527bd4e621e7090c9392739ec \
    --ShopNo TestS115
```

Output: 
```
{
    "Response": {
        "RequestId": null,
        "ErrCode": "0",
        "ErrMessage": "提交成功",
        "Result": {
            "ShopNo": "20260437",
            "ShopName": "南山店",
            "ShopFullName": "API进件测试的商户（南山店）",
            "MerchantNo": "20743873",
            "MerchantName": "API进件测试的商户",
            "BrandName": "招牌名称",
            "Province": "北京",
            "City": "北京",
            "County": "东城区",
            "CityId": "110101",
            "Address": "南山区科技园科苑大道讯美科技广场2栋12楼",
            "Telephone": "88888888",
            "OpenId": "eadca266c6d9a0aaa962323f3f778b576",
            "OpenKey": "1248d0bc506ff93e012364d16d449df3"
        }
    }
}
```

