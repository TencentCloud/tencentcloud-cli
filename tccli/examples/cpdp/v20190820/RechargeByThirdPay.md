**Example 1: 在途充值**



Input: 

```
tccli cpdp RechargeByThirdPay --cli-unfold-argument  \
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
    --TransNetMemberCode xxx \
    --BankSubAccountNumber xx \
    --TransFee xxx \
    --ThirdPayChannel 0001 \
    --ThirdPayChannelMerchantCode xx \
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

**Example 2: 处理失败示例**



Input: 

```
tccli cpdp RechargeByThirdPay --cli-unfold-argument  \
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
    --TransNetMemberCode xxx \
    --BankSubAccountNumber xx \
    --TransFee xxx \
    --ThirdPayChannel 0001 \
    --ThirdPayChannelMerchantCode xx \
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
        "RequestType": "MemberRechargeThirdPayAns",
        "RequestId": "67257811-59c6-4f19-acf3-51b388a2f9f5"
    }
}
```

