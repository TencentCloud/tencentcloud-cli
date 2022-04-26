**Example 1: QueryOpenBankOrderDetailReceiptInfo**



Input: 

```
tccli cpdp QueryOpenBankOrderDetailReceiptInfo --cli-unfold-argument  \
    --ChannelMerchantId CM598093665441488896 \
    --ChannelSubMerchantId CM599202010869022720 \
    --ChannelName ALIPAY \
    --PaymentMethod SAFT_ISV \
    --ChannelApplyId RE20220411599279856622231552
```

Output: 
```
{
    "Response": {
        "RequestId": "string",
        "Result": {
            "ChannelApplyId": "RE20220411599279856622231552",
            "ReceiptStatus": "SUCCESS",
            "ReceiptMessage": "申请成功",
            "DownloadUrl": "http://malaitong-1257849200.cos.ap-guangzhou.myqcloud.com/alipay/receipt/CM598093665441488896/CM599202010869022720/227180978/%E8%BD%AC%E5%85%A5%E8%BD%AC%E5%87%BA%E8%AF%81%E6%98%8E_20220411110070001506220048076642.pdf?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKID7ct6dqAX0QuCNayR3zKAmIZw97TSafMp%26q-sign-time%3D1649666717%3B1649670317%26q-key-time%3D1649666717%3B1649670317%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3D1ff8d900323616f04ae92db09daee0cb00cdfdfb",
            "ExpireTime": "2022-04-13 16:45:17"
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

**Example 2: 查询单笔交易回单结果**



Input: 

```
tccli cpdp QueryOpenBankOrderDetailReceiptInfo --cli-unfold-argument  \
    --ChannelSubMerchantId CM599202010869022720 \
    --ChannelMerchantId CM598093665441488896 \
    --ChannelApplyId RE20220411599285386061275136 \
    --ChannelName ALIPAY \
    --PaymentMethod SAFT_ISV \
    --OutApplyId 
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
            "DownloadUrl": "http://malaitong-1257849200.cos.ap-guangzhou.myqcloud.com/alipay/receipt/CM598093665441488896/CM599202010869022720/227180978/%E8%BD%AC%E5%85%A5%E8%BD%AC%E5%87%BA%E8%AF%81%E6%98%8E_20220411110070001506220048076642.pdf?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKID7ct6dqAX0QuCNayR3zKAmIZw97TSafMp%26q-sign-time%3D1649670030%3B1649673630%26q-key-time%3D1649670030%3B1649673630%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3D02d0f81a33113e9cf1c3d46d59eb4a3d63b9c15f",
            "ExpireTime": "2022-04-13 17:40:30"
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

