**Example 1: QuerySingleTransactionStatus**



Input: 

```
tccli cpdp QuerySingleTransactionStatus --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2 \
    --ImageId img-pmqg1cw7 \
    --MrchCode 1234 \
    --FunctionFlag 3 \
    --TranNetSeqNo U12345678910
```

Output: 
```
{
    "Response": {
        "TranAmt": "33.0",
        "InSubAcctNo": "",
        "TxnReturnCode": "000000",
        "RequestId": "9d819325-245d-4f3c-aec1-03b4f682a09b",
        "TranDate": "20191106",
        "TxnReturnMsg": "交易成功",
        "FailMsg": "提现交易已成功",
        "TranStatus": "0",
        "CnsmrSeqNo": "U862831911061573026540",
        "BookingFlag": "3",
        "TranTime": "154713",
        "OutSubAcctNo": ""
    }
}
```

