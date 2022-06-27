**Example 1: CreateOpenBankAggregatedSubMerchantRegistration**



Input: 

```
tccli cpdp CreateOpenBankAggregatedSubMerchantRegistration --cli-unfold-argument  \
    --OutRegistrationNo 123456 \
    --ChannelMerchantId 12345678 \
    --OutSubMerchantId 12345678 \
    --ChannelName HELIPAY \
    --PaymentMethod UNIFIED_PAYMENT \
    --OutSubMerchantType ENTERPRISE \
    --OutSubMerchantName 测试 \
    --OutSubMerchantShortName 测试 \
    --NotifyUrl http://xxxx.com \
    --BusinessLicenseInfo.BusinessLicenseType CREDITCODE \
    --BusinessLicenseInfo.BusinessLicenseNumber 123456 \
    --BusinessLicenseInfo.BusinessLicenseValidityType LONGTERM \
    --BusinessLicenseInfo.BusinessLicenseEffectiveDate 2021-09-01 \
    --BusinessLicenseInfo.BusinessLicenseExpireDate 2031-09-01 \
    --OutSubMerchantExtensionInfo.RegionCode 110101 \
    --OutSubMerchantExtensionInfo.RegisterAddress 北京市-朝阳区 \
    --OutSubMerchantExtensionInfo.MailingAddress 测试 \
    --OutSubMerchantExtensionInfo.BusinessAddress 测试 \
    --OutSubMerchantExtensionInfo.ServicePhone 156*****567 \
    --OutSubMerchantExtensionInfo.WebSiteUrl http://xxx.com \
    --OutSubMerchantExtensionInfo.EmailAddress  \
    --LegalPersonInfo.IdType IDCARD \
    --LegalPersonInfo.IdNumber 12345678 \
    --LegalPersonInfo.PersonName 测试 \
    --LegalPersonInfo.IdValidityType OTHER \
    --LegalPersonInfo.IdEffectiveDate 2010-09-01 \
    --LegalPersonInfo.IdExpireDate 2030-09-01 \
    --LegalPersonInfo.ContactPhone 156*****567 \
    --LegalPersonInfo.ContactAddress 测试 \
    --LegalPersonInfo.EmailAddress  \
    --NaturalPersonList.0.PersonType 4 \
    --NaturalPersonList.0.IdType IDCARD \
    --NaturalPersonList.0.IdNumber 12345678 \
    --NaturalPersonList.0.PersonName 测试 \
    --NaturalPersonList.0.IdValidityType OTHER \
    --NaturalPersonList.0.IdEffectiveDate 2010-09-01 \
    --NaturalPersonList.0.IdExpireDate 2030-09-01 \
    --NaturalPersonList.0.ContactPhone 156*****567 \
    --NaturalPersonList.0.ContactAddress 测试 \
    --NaturalPersonList.0.EmailAddress 123456@qq.com \
    --NaturalPersonList.1.PersonType 2 \
    --NaturalPersonList.1.IdType IDCARD \
    --NaturalPersonList.1.IdNumber 12345678 \
    --NaturalPersonList.1.PersonName 测试 \
    --NaturalPersonList.1.IdValidityType OTHER \
    --NaturalPersonList.1.IdEffectiveDate 2010-09-01 \
    --NaturalPersonList.1.IdExpireDate 2030-09-01 \
    --NaturalPersonList.1.ContactPhone 156*****567 \
    --NaturalPersonList.1.ContactAddress 测试 \
    --NaturalPersonList.1.EmailAddress  \
    --SettleInfo.SettleAccountType BUSINESS \
    --SettleInfo.SettleAccountNumber 12345678 \
    --SettleInfo.SettleAccountName 测试名称 \
    --SettleInfo.BankBranchId 12345678 \
    --SettleInfo.BankBranchName  \
    --SettleInfo.SettleMode AUTO \
    --SettleInfo.SettlePeriod T1 \
    --InterConnectionSubMerchantData {"IndustryType":"171","MerchantCategory":"TICKETING_TRAVEL"}
```

Output: 
```
{
    "Response": {
        "RequestId": "340b9ddc-09f1-43ab-8edc-cfaf1532f974",
        "Result": {
            "RegistrationStatus": "SUCCESS",
            "RegistrationMessage": "success",
            "ChannelRegistrationNo": "R1234567",
            "ChannelSubMerchantId": "CM12345678"
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

