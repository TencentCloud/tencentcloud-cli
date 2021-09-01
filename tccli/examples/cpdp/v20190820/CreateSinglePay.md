**Example 1: CreateSinglePay**



Input: 

```
tccli cpdp CreateSinglePay --cli-unfold-argument  \
    --SerialNumber 20190505000000000013 \
    --PayAccountNumber 123123123 \
    --PayAccountName 测试付款账户 \
    --PayBankCnaps 321321321 \
    --Amount 1 \
    --RecvAccountNumber 123123123123 \
    --RecvAccountName 王大拿 \
    --RecvBankCnaps 321321321
```

Output: 
```
{
    "Response": {
        "RequestId": "be294bbb-47c9-4f01-9b1e-9e8ca3a72d4b",
        "Result": {
            "SerialNo": "20190505000000000013",
            "BankSerialNo": "123123123123123",
            "PayStatus": "P",
            "HandleStatus": "S",
            "BankRetMsg": null,
            "BankRetCode": null,
            "HandleMsg": "处理成功！"
        }
    }
}
```

