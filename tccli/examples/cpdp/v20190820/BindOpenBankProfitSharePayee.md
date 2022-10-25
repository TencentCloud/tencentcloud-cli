**Example 1: 正常返回**



Input: 

```
tccli cpdp BindOpenBankProfitSharePayee --cli-unfold-argument  \
    --ChannelMerchantId CM635846524835979264 \
    --ChannelName HELIPAY \
    --ChannelSubMerchantId CM615222155219103744 \
    --AccountNo test21212328671312312120361 \
    --NotifyUrl  \
    --ExternalProfitSharingData  \
    --Environment  \
    --ProfitSharePayeeInfo.Province xx \
    --ProfitSharePayeeInfo.City xx \
    --ProfitSharePayeeInfo.ExpireDate xx \
    --ProfitSharePayeeInfo.TransferBankNo xx \
    --ProfitSharePayeeInfo.Address xx \
    --ProfitSharePayeeInfo.IsOSA xx \
    --ProfitSharePayeeInfo.Nature xx \
    --ProfitSharePayeeInfo.LegalIdNo xx \
    --ProfitSharePayeeInfo.Country xx \
    --ProfitSharePayeeInfo.BicCode xx \
    --ProfitSharePayeeInfo.BankName xx \
    --ProfitSharePayeeInfo.SwiftCode xx \
    --ProfitSharePayeeInfo.Telephone xx \
    --ProfitSharePayeeInfo.AccountName xx \
    --ProfitSharePayeeInfo.Currency xx \
    --ProfitSharePayeeInfo.Cnaps xx \
    --ProfitSharePayeeInfo.Fid xx \
    --ProfitSharePayeeInfo.Flag xx \
    --ProfitSharePayeeInfo.BankAddress xx \
    --ProfitSharePayeeInfo.DepositCountry xx
```

Output: 
```
{
    "Response": {
        "RequestId": "1",
        "Result": null,
        "ErrCode": "COMMON.SYSTEM_DISABLED",
        "ErrMessage": ""
    }
}
```

