**Example 1: QueryBankTransactionDetails**



Input: 

```
tccli cpdp QueryBankTransactionDetails --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2 \
    --ImageId img-pmqg1cw7 \
    --MrchCode 1234 \
    --FunctionFlag 2 \
    --SubAcctNo ' 1234000000006047' \
    --QueryFlag 1 \
    --StartDate 20191101 \
    --EndDate 20191130 \
    --PageNum 1
```

Output: 
```
{
    "Response": {
        "TranItemArray": [
            {
                "TranAmt": "5000.0",
                "InSubAcctNo": "12345678910",
                "TranDate": "20191106",
                "FrontSeqNo": "1911060076971376",
                "TranStatus": "0",
                "BookingFlag": "1",
                "BookingType": "4",
                "TranTime": "154107",
                "OutSubAcctNo": "1234000000000002",
                "Remark": ""
            }
        ],
        "TxnReturnCode": "000000",
        "EndFlag": "1",
        "TotalNum": "1",
        "RequestId": "4e52b16b-ffd8-450f-a494-c39fd8eef963",
        "ResultNum": "1",
        "TxnReturnMsg": "交易成功",
        "ReservedMsg": "",
        "CnsmrSeqNo": "",
        "StartRecordNo": "1"
    }
}
```

