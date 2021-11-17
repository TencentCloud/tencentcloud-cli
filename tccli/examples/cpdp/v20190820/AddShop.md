**Example 1: 添加门店接口成功示例**

添加门店接口成功

Input: 

```
tccli cpdp AddShop --cli-unfold-argument  \
    --OpenId f2cc268b9c95fbbb230a19397fe35f8d \
    --OpenKey e30051d527bd4e621e7090c9392739ec \
    --OutShopId S0001 \
    --MerchantNo M0001 \
    --ShopName 南山店 \
    --ShopFullName 江山小厨（南山店） \
    --CityId 440300 \
    --Address 大学城 \
    --Telephone 11111111111 \
    --PictureOne picture1 \
    --PictureTwo picture2 \
    --PictureThree picture3 \
    --Longitude N22°32′ \
    --Latitude E114°03′ \
    --LongitudeTwo N22°32′ \
    --LatitudeTwo E114°03′ \
    --OpenHours 9:00-12:00,13:00-18:00 \
    --Contact 张三 \
    --FinancialTelephone 11111111111 \
    --OtherPicture picture4
```

Output: 
```
{
    "Response": {
        "RequestId": null,
        "ErrCode": "0",
        "ErrMessage": "提交成功",
        "Result": {
            "ShopNo": "S0001"
        }
    }
}
```

