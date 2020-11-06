**Example 1: 会员间交易**



Input: 

```
tccli cpdp ExecuteMemberTransaction --cli-unfold-argument  \
    --MidasSecretId 1587005497659 \
    --MidasSignature 111 \
    --MidasAppId unibank10001 \
    --RequestType MemberTransactionReq \
    --MerchantCode 4087 \
    --PayChannel bank_pingan \
    --PayChannelSubId 1 \
    --OutSubAccountName 水惠壮 \
    --InSubAccountName 水惠壮 \
    --OutSubAccountNumber 4087000000016017 \
    --InSubAccountNumber 4087000000016017 \
    --BankAccountNumber 15000093978307 \
    --CurrencyUnit 1 \
    --CurrencyType RMB \
    --CurrencyAmount 0.03 \
    --TransSequenceNumber 1223333 \
    --OrderId 22233344 \
    --OutTransNetMemberCode 2019080500002 \
    --InTransNetMemberCode ninggyang_test \
    --MidasEnvironment development
```

Output: 
```
{
    "Response": {
        "RequestId": "7c8256aa-1a63-402e-ba14-e0e138135eae",
        "FrontSequenceNumber": "6124889676724932",
        "RequestType": "MemberTransactionAns",
        "ReservedMessage": ""
    }
}
```

