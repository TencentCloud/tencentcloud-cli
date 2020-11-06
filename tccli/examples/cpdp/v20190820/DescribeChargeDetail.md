**Example 1: 查询充值明细**



Input: 

```
tccli cpdp DescribeChargeDetail --cli-unfold-argument  \
    --MidasSecretId 1587005497659 \
    --MidasSignature 111 \
    --MidasAppId unibank10001 \
    --RequestType ChargeDetailQueryReq \
    --OrderId 2020042180081 \
    --PlatformShortNumber F08872 \
    --AcquiringChannelType 04 \
    --BankAccountNumber 15000093978307 \
    --PayChannelSubId 1 \
    --PayChannel bank_pingan \
    --MerchantCode 4087 \
    --TransSequenceNumber F088722004270543493495 \
    --MidasEnvironment dev
```

Output: 
```
{
    "Response": {
        "OrderInSubAccountNumber": "4087000000016017",
        "FailMessage": "",
        "RequestId": "9320a070-aa82-4b2c-906e-e7c438115e3d",
        "OrderStatus": "0",
        "PayMode": "1",
        "OrderDate": "20200512",
        "OrderActualInSubAccountName": "水惠壮",
        "OrderAmount": "0.01",
        "CommissionAmount": "0.01",
        "OrderActualInSubAccountNumber": "4087000000016017",
        "FrontSequenceNumber": "2005120260085997",
        "RequestType": "ChargeDetailQueryAns",
        "OrderTime": "095302",
        "OrderInSubAccountName": "水惠壮"
    }
}
```

