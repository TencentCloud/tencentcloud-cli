**Example 1: 结算中心-创建用户**



Input: 

```
tccli cpdp CreateFlexPayee --cli-unfold-argument  \
    --IdType 1 \
    --Remark 字符串 \
    --ServiceProviderId channel-002 \
    --Name 字符串 \
    --OutUserId 00013 \
    --TaxInfo.TaxServiceProviderId 7 \
    --TaxInfo.TaxEntityType NATURAL \
    --TaxInfo.TaxpayerIdNo 111 \
    --TaxInfo.TaxTemplateInfoList.0.IncomeType LABOR \
    --TaxInfo.TaxTemplateInfoList.0.TaxTemplateId 106 \
    --AccountName 李二的账户 \
    --IdNo 36011119940625093X
```

Output: 
```
{
    "Response": {
        "ErrCode": "COMMON.INVALID_PARAMETER",
        "ErrMessage": "参数错误:纳税人识别号不能为空,",
        "Result": null,
        "RequestId": "aa7d2d8d-c1f9-4251-ba1a-71bd5a6fe172"
    }
}
```

