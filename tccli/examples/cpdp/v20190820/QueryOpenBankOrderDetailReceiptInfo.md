**Example 1: 查询单笔交易回单结果**

查询单笔交易回单结果成功示例

Input: 

```
tccli cpdp QueryOpenBankOrderDetailReceiptInfo --cli-unfold-argument  \
    --ChannelSubMerchantId CM599202010869022720 \
    --ChannelMerchantId CM598093665441488896 \
    --ChannelApplyId RE20220411599285386061275136 \
    --ChannelName ALIPAY \
    --PaymentMethod SAFT_ISV
```

Output: 
```
{
    "Response": {
        "RequestId": "539942ea-d2a7-48a5-a999-6f003a3642ff",
        "Result": {
            "ChannelApplyId": "RE20220411599285386061275136",
            "ReceiptStatus": "SUCCESS",
            "ReceiptMessage": "申请成功",
            "DownloadUrl": "http://xxx.xx.com/8076642.pdf?sign=b9c15f",
            "ExpireTime": "2022-04-13 17:40:30"
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

