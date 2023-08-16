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
        "Error": {
            "Code": "FailedOperation.PABankError",
            "Message": "E90006:%E6%97%A0%E5%8C%B9%E9%85%8D%E7%9A%84%E4%BC%9A%E5%91%98%E5%AD%90%E8%B4%A6%E6%88%B7%E6%88%96%E4%BC%9A%E5%91%98%E5%AD%90%E8%B4%A6%E6%88%B7%E5%B7%B2%E5%A4%B1%E6%95%88"
        },
        "RequestType": "MemberRechargeThirdPayAns",
        "RequestId": "67257811-59c6-4f19-acf3-51b388a2f9f5"
    }
}
```

