**Example 1: 添加商户接口成功示例**

添加商户接口成功

Input: 

```
tccli cpdp AddMerchant --cli-unfold-argument  \
    --OpenId f2cc268b9c95fbbb230a19397fe35f8d \
    --OpenKey e30051d527bd4e621e7090c9392739ec \
    --OutMerchantId 10 \
    --MerchantName 北极星 \
    --BrandName 北国风光 \
    --CityId 111000 \
    --Address 东湖路 \
    --Telephone 11111111111 \
    --OpenHours 9:00-12:00,13:00-18:00 \
    --ClassificationIds 100 100200 \
    --BossName 张三 \
    --BossSex 1 \
    --BossIdCountry 中国CHN \
    --BossIdType 1 \
    --BossStartDate 2019-9-9 \
    --BossEndDate 2029-9-9 \
    --BossIdNo 00000000000000000 \
    --BossTelephone 11111111111 \
    --BossEmail 11111111111@163.com \
    --BossJob 学生 \
    --BossAddress 北京朝阳区 \
    --BossPositive picture1 \
    --BossBack picture2 \
    --BusinessLicenseType 1 \
    --BusinessLicenseStartDate 2019-9-9 \
    --BusinessLicenseEndDate 2029-9-9 \
    --BusinessLicenseNo 100 \
    --BusinessLicensePicture picture3 \
    --BankName 中国银行 \
    --AccountName 100 \
    --AccountNo 10000 \
    --AccountType 1 \
    --BankNo 1 \
    --AccountBoss 1 \
    --AccountIdType 1 \
    --AccountIdNo 11111111111111112 \
    --Intro 互联网商户 \
    --AccountManagerName 李四 \
    --OrganizationNo 00000 \
    --OrganizationStartDate 2019-9-9 \
    --OrganizationEndDate 2029-9-9 \
    --OrganizationPicture picture4 \
    --TaxRegistrationNo 00100 \
    --TaxRegistrationStartDate 2019-9-9 \
    --TaxRegistrationEndDate 2029-9-9 \
    --TaxRegistrationPicture picture5 \
    --Tag 10 \
    --FinancialContact 张三 \
    --FinancialTelephone 11111111111 \
    --Logo 北极星 \
    --LicencePicture picture5 \
    --LicencePictureTwo picture6 \
    --OtherPictureOne 资料1 \
    --OtherPictureTwo 资料2 \
    --OtherPictureThree 资料3 \
    --OtherPictureFour 资料4
```

Output: 
```
{
    "Response": {
        "RequestId": "171304d7-1084-4c98-9baa-fa1e8d2af7d0",
        "ErrCode": "0",
        "ErrMessage": "提交成功",
        "Result": {
            "MerchantNo": "M0001"
        }
    }
}
```

