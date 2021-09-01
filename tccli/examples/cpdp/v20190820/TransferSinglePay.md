**Example 1: TransferSinglePay**



Input: 

```
tccli cpdp TransferSinglePay --cli-unfold-argument  \
    --TransferType 3 \
    --TransferAmount 1 \
    --MerchantId faryrong \
    --MerchantAppId faryrong \
    --OrderId 123179 \
    --PayeeId 15000100714720 \
    --PayeeName 前端数据支持测试山西惟垂有限公司 \
    --PayeeExtends {"PayeeBankName":"平安银行","CcyCode":"RMB","UnionFlag":1}
```

Output: 
```
{
    "Response": {
        "ErrMessage": "xx",
        "Result": {
            "TradeSerialNo": "xx"
        },
        "RequestId": "xx",
        "ErrCode": "xx"
    }
}
```

