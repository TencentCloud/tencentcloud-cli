**Example 1: 查询商户明细接口成功示例**

查询商户明细接口成功

Input: 

```
tccli cpdp ViewMerchant --cli-unfold-argument  \
    --OpenId f2cc268b9c95fbbb230a19397fe35f8d \
    --OpenKey e30051d527bd4e621e7090c9392739ec \
    --MerchantNo Test10
```

Output: 
```
{
    "Response": {
        "RequestId": null,
        "ErrCode": "0",
        "ErrMessage": "提交成功",
        "Result": {
            "MerchantNo": "20743873",
            "MerchantName": "API进件测试的商户",
            "BrandName": "招牌名称",
            "Province": "北京",
            "City": "北京",
            "Country": "东城区",
            "CityId": "110100",
            "ClassificationIds": "100,101",
            "ClassificationNames": "美食,粤菜",
            "Address": "科技园科苑大道讯美科技广场2栋12楼",
            "Telephone": "13800138000",
            "OpenHours": "9:00-12:00,13:00-18:00",
            "Status": "2",
            "Remark": "无",
            "AddTime": "2016-12-06 13:29:41",
            "UpdateTime": "2016-12-06 16:08:52",
            "ShopCount": "1",
            "TerminalCount": "0",
            "ContractCount": "1",
            "AppCount": "0",
            "BossName": "林三",
            "BossSex": "1",
            "BossIdCount": "CHN",
            "BossIdType": "1",
            "BossStartDate": "2016-01-01",
            "BossEndDate": "2026-01-01",
            "BossIdNo": "431227198208081122",
            "BossPositive": "201601/12345.jpg",
            "BossBack": "201601/12345.jpg",
            "BusinessLicenseType": "1",
            "BusinessLicenseStartDate": "2016-01-01",
            "BusinessLicenseEndDate": "2016-12-01",
            "BusinessLicenseNo": "1234567890ABC",
            "BankName": "招商银行",
            "AccountName": "林三",
            "AccountNo": "6222202888899999",
            "AccountType": "1",
            "BankNo": "123456789"
        }
    }
}
```

