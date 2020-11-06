**Example 1: 撤销在途充值**



Input: 

```
tccli cpdp RevokeRechargeByThirdPay --cli-unfold-argument  \
    --MidasSecretId 1587005497659 \
    --MidasSignature 111 \
    --MidasAppId unibank10001 \
    --RequestType MemberRechargeThirdPayReq \
    --OrderId 2020042180081 \
    --PlatformShortNumber F08872 \
    --AcquiringChannelType 04 \
    --BankAccountNumber 15000093978307 \
    --PayChannelSubId 1 \
    --PayChannel bank_pingan \
    --MerchantCode 4087 \
    --TransSequenceNumber F088722004270543493495 \
    --OldFrontSequenceNumber F088722004270543493495 \
    --TranNetMemberCode xxx \
    --BankSubAccountNumber xx \
    --TransFee xxx \
    --ThirdPayChannel 0001 \
    --ThirdPayChannelOrderId xxxx \
    --CurrencyAmount 1 \
    --CurrencyUnit 1 \
    --CurrencyType RMB \
    --MidasEnvironment dev
```

Output: 
```
{
    "Response": {
        "RequestId": "2c96c4eb-ab02-4ba6-a6c6-7d97c698b127",
        "RequestType": "MemberRechargeThirdPayAns",
        "FrontSequenceNumber": "2005080253306846",
        "ReservedMessage": ""
    }
}
```

