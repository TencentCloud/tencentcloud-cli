**Example 1: 正常返回**



Input: 

```
tccli cpdp QueryOpenBankSubMerchantSignOnline --cli-unfold-argument  \
    --ChannelMerchantId CM614829654947741696 \
    --ChannelName HELIPAY \
    --OutSubMerchantId  \
    --ChannelSubMerchantId CM615222155219103744
```

Output: 
```
{
    "Response": {
        "RequestId": "111111",
        "Result": {
            "SignStatus": "PROCESSING",
            "SignMessage": "进行中"
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

