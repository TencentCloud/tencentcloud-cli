**Example 1: QueryCustAcctIdBalance**



Input: 

```
tccli cpdp QueryCustAcctIdBalance --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2 \
    --ImageId img-pmqg1cw7 \
    --MrchCode 1234 \
    --SubAcctNo 1234000000006047 \
    --QueryFlag 2 \
    --PageNum 1
```

Output: 
```
{
    "Response": {
        "TxnReturnCode": "000000",
        "EndFlag": "1",
        "TotalNum": "1",
        "RequestId": "b0fc9772-d6b9-4caa-9ac6-1605c0cad50f",
        "ResultNum": "1",
        "TxnReturnMsg": "交易成功",
        "ReservedMsg": "",
        "CnsmrSeqNo": "",
        "StartRecordNo": "1",
        "AcctArray": [
            {
                "AcctAvailBal": "0.00",
                "TranNetMemberCode": "YAPI100000",
                "CashAmt": "0.00",
                "SubAcctName": "demo",
                "MaintenanceDate": "20191105",
                "SubAcctNo": "1234000000006047",
                "SubAcctProperty": "1"
            }
        ]
    }
}
```

