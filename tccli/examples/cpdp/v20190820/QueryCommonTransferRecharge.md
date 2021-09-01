**Example 1: QueryCommonTransferRecharge**



Input: 

```
tccli cpdp QueryCommonTransferRecharge --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2 \
    --ImageId img-pmqg1cw7 \
    --MrchCode 1234 \
    --FunctionFlag 0 \
    --StartDate 20191001 \
    --EndDate 20191101 \
    --PageNum 1
```

Output: 
```
{
    "Response": {
        "TranItemArray": [
            {
                "BankName": "",
                "TranAmt": "1000000.0",
                "FrontSeqNo": "1910180070999566",
                "InAcctName": "",
                "TranNetMemberCode": "1234000000000002",
                "Ccy": "RMB",
                "InAcctNo": "",
                "InAcctType": "03",
                "AccountingDate": "20191018",
                "SubAcctNo": "12345678910",
                "Remark": "19101811667519"
            }
        ],
        "TxnReturnCode": "000000",
        "EndFlag": "1",
        "TotalNum": "1",
        "RequestId": "50b3df36-dc17-4c0c-b750-a771a7794572",
        "ResultNum": "1",
        "TxnReturnMsg": "交易成功",
        "ReservedMsg": "",
        "CnsmrSeqNo": "",
        "StartRecordNo": "1"
    }
}
```

