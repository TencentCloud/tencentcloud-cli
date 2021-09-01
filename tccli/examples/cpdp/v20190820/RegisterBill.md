**Example 1: 登记挂账(支持撤销)**

登记挂账(支持撤销)

Input: 

```
tccli cpdp RegisterBill --cli-unfold-argument  \
    --MidasSecretId 1587005497659 \
    --MidasSignature 111 \
    --MidasAppId unibank10001 \
    --RequestType MemberRechargeThirdPayReq \
    --OrderId 2020042180081 \
    --PlatformShortNo F08872 \
    --AcquiringChannelType 04 \
    --BankAccountNo 15000093978307 \
    --PayChannelSubId 1 \
    --PayChannel bank_pingan \
    --MerchantCode 4087 \
    --TransSeqNo F088722004270543493495 \
    --TranNetMemberCode xxx \
    --BankSubAccountNo xx \
    --TranFee 0.0 \
    --OrderAmt 1 \
    --TranType 0 \
    --MidasEnvironment dev
```

Output: 
```
{
    "Response": {
        "RequestId": "2c96c4eb-ab02-4ba6-a6c6-7d97c698b127",
        "RequestType": "RegBillSupportWithdrawAns",
        "FrontSeqNo": "2005080253306846",
        "ReservedMessage": ""
    }
}
```

