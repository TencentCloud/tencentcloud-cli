**Example 1: 正常返回**



Input: 

```
tccli cpdp ApplyOpenBankSubMerchantSignOnline --cli-unfold-argument  \
    --ChannelMerchantId CM614829654947741696 \
    --ChannelName HELIPAY \
    --OutSubMerchantId  \
    --ChannelSubMerchantId CM615222155219103744 \
    --NotifyUrl http://127.0.0.1/pay/notfiy
```

Output: 
```
{
    "Response": {
        "RequestId": "111111",
        "Result": {
            "SignStatus": "PROCESSING",
            "ExternalReturnData": ""
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

