**Example 1: QueryBankClear**



Input: 

```
tccli cpdp QueryBankClear --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2 \
    --ImageId img-pmqg1cw7 \
    --MrchCode 1234 \
    --FunctionFlag 1 \
    --PageNum 1
```

Output: 
```
{
    "Response": {
        "TranItemArray": [
            {
                "SubAcctType": "7",
                "TotalAmt": "0.0",
                "ClearingReturnMsg": "",
                "ReconcileReturnMsg": "在途对账成功",
                "ClearingStatus": "0",
                "Date": "20191018",
                "ReconcileStatus": "0"
            }
        ],
        "TxnReturnCode": "000000",
        "EndFlag": "1",
        "TotalNum": "1",
        "RequestId": "02ed16a0-735c-4b18-8a56-ea45b7410940",
        "ResultNum": "1",
        "TxnReturnMsg": "交易成功",
        "ReservedMsg": "",
        "CnsmrSeqNo": "U862831911061573029503",
        "StartRecordNo": "1"
    }
}
```

