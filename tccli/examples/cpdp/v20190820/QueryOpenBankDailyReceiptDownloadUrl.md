**Example 1: 回单查询示例**

回单查询示例

Input: 

```
tccli cpdp QueryOpenBankDailyReceiptDownloadUrl --cli-unfold-argument  \
    --ChannelMerchantId CM572433237990035456 \
    --ChannelSubMerchantId sub0001 \
    --ChannelName TENPAY \
    --PaymentMethod OPENBANK_PAYMENT \
    --BindSerialNo 123243556 \
    --QueryDate 2020-01-11
```

Output: 
```
{
    "Response": {
        "RequestId": "991304d7-1084-4c98-9baa-fa1e8d2a223",
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功",
        "Result": {
            "DownloadUrl": "http://127.0.0.1/receipt/download",
            "ExpireTime": "2020-01-11 14:11:10",
            "ReceiptStatus": "READY"
        }
    }
}
```

**Example 2: 查询异常示例**



Input: 

```
tccli cpdp QueryOpenBankDailyReceiptDownloadUrl --cli-unfold-argument  \
    --BindSerialNo 23445 \
    --ChannelMerchantId 123 \
    --Environment sandbox \
    --ChannelSubMerchantId 3456 \
    --QueryDate 2020-01-17 \
    --ChannelName TENPAY \
    --PaymentMethod EBANK_PAYMENT
```

Output: 
```
{
    "Response": {
        "RequestId": "dabb2484-a71a-4a0c-b172-506b451f706e",
        "Result": null,
        "ErrCode": "FailedOperation.SystemError",
        "ErrMessage": "系统未知异常"
    }
}
```

