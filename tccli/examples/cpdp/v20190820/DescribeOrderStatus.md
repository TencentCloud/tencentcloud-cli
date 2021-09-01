**Example 1: 查询订单状态**

查询订单状态

Input: 

```
tccli cpdp DescribeOrderStatus --cli-unfold-argument  \
    --MidasSecretId 1587005497659 \
    --MidasSignature 111 \
    --MidasAppId unibank10001 \
    --RequestType QueryOrderStatusReq \
    --OrderId 2020042180081 \
    --PlatformShortNumber F08872 \
    --BankAccountNumber 15000093978307 \
    --PayChannelSubId 1 \
    --PayChannel bank_pingan \
    --MerchantCode 4087 \
    --TransSequenceNumber F088722004270543493495 \
    --QueryType 1 \
    --MidasEnvironment dev
```

Output: 
```
{
    "Response": {
        "FailMessage": "提现交易已成功",
        "InSubAccountNumber": "",
        "RequestId": "67741274-4ae0-4c76-ad19-f332b893bf70",
        "OrderStatus": "0",
        "BookingFlag": "3",
        "OrderTime": "214021",
        "OutSubAccountNumber": "",
        "RequestType": "QueryOrderStatusAns",
        "OrderAmount": "0.01",
        "OrderDate": "20200319"
    }
}
```

