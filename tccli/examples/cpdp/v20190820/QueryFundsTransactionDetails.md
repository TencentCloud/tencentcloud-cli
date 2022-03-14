**Example 1: 聚鑫-查询会员资金交易信息列表**



Input: 

```
tccli cpdp QueryFundsTransactionDetails --cli-unfold-argument  \
    --MidasEnvironment development \
    --PageOffSet 1 \
    --QueryDateType 2 \
    --QueryStartDate 20220301 \
    --QueryEndDate 20220302 \
    --QueryTranType 2 \
    --SubAccountNumber 2031000000096048 \
    --BankAccountNumber 15000101075856
```

Output: 
```
{
    "Response": {
        "RequestId": "6f1e4537-16d2-40fd-bdf5-6ed22be524d5",
        "Result": {
            "ResultCount": 1,
            "TotalCount": 1,
            "EndFlag": "1",
            "TranItemArray": [
                {
                    "TransType": "1",
                    "BankBookingMessage": "提现",
                    "TranStatus": "0",
                    "TransNetMemberCode": "20211202B",
                    "SubAccountNumber": "2031000000096048",
                    "SubAccountName": "曹盈",
                    "TransAmount": "222.22",
                    "TransFee": "0.0",
                    "TransDate": "20220302",
                    "TransTime": "141028",
                    "BankSequenceNumber": "2203020174101096",
                    "Remark": "H190482203020792346770"
                }
            ]
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

