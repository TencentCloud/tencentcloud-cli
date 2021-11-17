**Example 1: 查询门店明细接口成功示例**

查询门店明细接口成功

Input: 

```
tccli cpdp ViewShop --cli-unfold-argument  \
    --OpenId f2cc268b9c95fbbb230a19397fe35f8d \
    --OpenKey e30051d527bd4e621e7090c9392739ec \
    --ShopNo Test5333
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
            "AddTime": "2016-12-06 14:38:35",
            "UpdateTime": "2016-12-06 14:47:03",
            "TerminalCount": "0",
            "AppCount": "0",
            "OutShopId": "123456",
            "Status": "1",
            "Remark": "无",
            "PictureOne": "201601/123456.jpg",
            "PictureTwo": "201601/123456.jpg",
            "PictureThree": "201601/123456.jpg",
            "PictureFour": "201601/123456.jpg",
            "Longitude": "113.947107",
            "Latitude": "22.547374",
            "LongitudeTwo": "113.947107",
            "LatitudeTwo": "22.547374"
        }
    }
}
```

