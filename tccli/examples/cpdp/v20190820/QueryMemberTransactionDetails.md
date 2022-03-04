**Example 1: 聚鑫-查询会员间交易信息列表**



Input: 

```
tccli cpdp QueryMemberTransactionDetails --cli-unfold-argument  \
    --MidasEnvironment development \
    --PageOffSet 1 \
    --QueryDateType 2 \
    --QueryStartDate 20220201 \
    --QueryEndDate 20220302 \
    --QueryTranType 1 \
    --SubAccountNumber 2031000000001000 \
    --BankAccountNumber 15000101075856
```

Output: 
```
{
    "Response": {
        "RequestId": "abb4aa8b-6dfa-47eb-9c4a-de464da32e68",
        "Result": {
            "ResultCount": 2,
            "TotalCount": 2,
            "EndFlag": "1",
            "TranItemArray": [
                {
                    "TransType": "1",
                    "TranStatus": "0",
                    "TransAmount": "222.22",
                    "TransDate": "20220302",
                    "TransTime": "140916",
                    "BankSequenceNumber": "2203020174100913",
                    "BankBookingType": "1",
                    "InSubAccountNumber": "2031000000096048",
                    "OutSubAccountNumber": "2031000000001000",
                    "Remark": ""
                },
                {
                    "TransType": "2",
                    "TranStatus": "0",
                    "TransAmount": "222.22",
                    "TransDate": "20220302",
                    "TransTime": "140708",
                    "BankSequenceNumber": "2203020174100837",
                    "BankBookingType": "4",
                    "InSubAccountNumber": "2031000000001000",
                    "OutSubAccountNumber": "2031000000000002",
                    "Remark": ""
                }
            ]
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

