**Example 1: 会员间交易退款**

会员间交易退款

Input: 

```
tccli cpdp RefundMemberTransaction --cli-unfold-argument  \
    --MidasSecretId 1587005497659 \
    --MidasSignature 111 \
    --MidasAppId unibank10001 \
    --RequestType MemberTransactionRefundReq \
    --MerchantCode 4087 \
    --PayChannel bank_pingan \
    --PayChannelSubId 1 \
    --OutSubAccountName 水惠壮 \
    --InSubAccountName 水惠壮 \
    --OutSubAccountNumber 4087000000016017 \
    --InSubAccountNumber 4087000000061027 \
    --OldTransSequenceNumber F088722003121180926752 \
    --BankAccountNumber 15000093978307 \
    --CurrencyAmount 0.03 \
    --TransSequenceNumber 33233 \
    --OldOrderId 332222211111 \
    --OrderId 777323232111 \
    --OutTransNetMemberCode 2019080500002 \
    --InTransNetMemberCode ninggyang_test \
    --ReservedMessage  \
    --PlatformShortNumber F08872 \
    --TransType 2 \
    --TransFee 0.01 \
    --MidasEnvironment development
```

Output: 
```
{
    "Response": {
        "FrontSequenceNumber": "6124889676724932",
        "ReservedMessage": "",
        "RequestType": "MemberTransactionRefundAns",
        "RequestId": "7c8256aa-1a63-402e-ba14-e0e138135eae"
    }
}
```

