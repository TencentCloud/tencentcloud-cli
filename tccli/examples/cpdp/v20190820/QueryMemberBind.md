**Example 1: QueryMemberBind**



Input: 

```
tccli cpdp QueryMemberBind --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2 \
    --ImageId img-pmqg1cw7 \
    --MrchCode 1234 \
    --QueryFlag 2 \
    --SubAcctNo 12345678910 \
    --PageNum 1
```

Output: 
```
{
    "Response": {
        "TranItemArray": [
            {
                "MemberGlobalId": "610451294112054529",
                "MemberAcctNo": "6230553000051286369",
                "EiconBankBranchId": "30758511007998",
                "TranNetMemberCode": "YAPI100000",
                "CnapsBranchId": "",
                "MemberName": "demo",
                "BankType": "1",
                "Mobile": "11111111111",
                "SubAcctNo": "1234000000006047",
                "FundSummaryAcctNo": "150001015123971",
                "AcctOpenBranchName": "平安银行",
                "MemberGlobalType": "1"
            }
        ],
        "TxnReturnCode": "000000",
        "EndFlag": "1",
        "TotalNum": "1",
        "RequestId": "3ca7d7df-7007-41e9-b1fd-70a43dcb957f",
        "ResultNum": "1",
        "TxnReturnMsg": "交易成功",
        "ReservedMsg": "",
        "CnsmrSeqNo": "U862831911051572947583",
        "StartRecordNo": "1"
    }
}
```

