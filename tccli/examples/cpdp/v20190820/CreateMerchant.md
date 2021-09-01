**Example 1: CreateMerchant**



Input: 

```
tccli cpdp CreateMerchant --cli-unfold-argument  \
    --InvoicePlatformId 0 \
    --BankName 银行名称 \
    --BankAccount 621281240305123200 \
    --Drawer drawer \
    --Payee payee \
    --Reviewer reviewer \
    --State 1 \
    --TaxpayerNum 111212222233338 \
    --TaxpayerName 测试名称 \
    --LegalPersonName 测试名称 \
    --ContactsName 联系人 \
    --Email test@email.com \
    --Phone 11111111111 \
    --RegionCode 44 \
    --CityName 深圳市 \
    --Address 地址 \
    --TaxRegistrationCertificate 营业执照base64编码文件
```

Output: 
```
{
    "Response": {
        "RequestId": "CPDP-1585012073321",
        "Result": {
            "Message": "success",
            "Data": {
                "SerialNo": "CPDP",
                "TaxpayerNum": "",
                "TaxpayerName": ""
            },
            "Code": 0
        }
    }
}
```

