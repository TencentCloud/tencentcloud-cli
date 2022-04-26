**Example 1: ApplyOpenBankOrderDetailReceipt**



Input: 

```
tccli cpdp ApplyOpenBankOrderDetailReceipt --cli-unfold-argument  \
    --OutApplyId xx \
    --ChannelMerchantId CM598093665441488896 \
    --ChannelSubMerchantId CM599202010869022720 \
    --ChannelName ALIPAY \
    --PaymentMethod SAFT_ISV \
    --ChannelOrderId 599279735088078848
```

Output: 
```
{
    "Response": {
        "RequestId": "string",
        "Result": {
            "ChannelApplyId": "RE20220411599279856622231552",
            "ReceiptStatus": "PROCESSING",
            "ReceiptMessage": "申请中",
            "DownloadUrl": null,
            "ExpireTime": null
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

**Example 2: 单笔交易回单申请**



Input: 

```
tccli cpdp ApplyOpenBankOrderDetailReceipt --cli-unfold-argument  \
    --ChannelOrderId 599279735088078848 \
    --ChannelMerchantId CM598093665441488896 \
    --ChannelSubMerchantId CM599202010869022720 \
    --ChannelName ALIPAY \
    --PaymentMethod SAFT_ISV \
    --OutApplyId 
```

Output: 
```
{
    "Response": {
        "RequestId": "e5f61238-9099-4467-a3b6-ae026ba4087d",
        "Result": {
            "ChannelApplyId": "RE20220411599285386061275136",
            "ReceiptStatus": "PROCESSING",
            "ReceiptMessage": "申请中",
            "DownloadUrl": null,
            "ExpireTime": null
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

