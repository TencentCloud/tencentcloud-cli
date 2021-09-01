**Example 1: QueryBankWithdrawCashDetails**



Input: 

```
tccli cpdp QueryBankWithdrawCashDetails --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2 \
    --ImageId img-pmqg1cw7 \
    --MrchCode 1234 \
    --FunctionFlag 1 \
    --SubAcctNo 1234000000006047 \
    --QueryFlag 2 \
    --PageNum 1
```

Output: 
```
{
    "Response": {
        "TranItemArray": [
            {
                "TranAmt": "33.0",
                "TranDate": "20191106",
                "FrontSeqNo": "1911060076971993",
                "TranNetMemberCode": "YAPI100000",
                "Commission": "0.0",
                "TranStatus": "0",
                "BookingMsg": "提现",
                "SubAcctName": "demo",
                "BookingFlag": "01",
                "SubAcctNo": "12345678910",
                "TranTime": "154713",
                "Remark": "U862831911061573026431"
            }
        ],
        "TxnReturnCode": "000000",
        "EndFlag": "1",
        "TotalNum": "1",
        "RequestId": "1826504f-e319-46d9-94bf-2d28a6d66979",
        "ResultNum": "1",
        "TxnReturnMsg": "交易成功",
        "ReservedMsg": "",
        "CnsmrSeqNo": "",
        "StartRecordNo": "1"
    }
}
```

