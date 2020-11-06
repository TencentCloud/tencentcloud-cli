**Example 1: ModifyMntMbrBindRelateAcctBankCode**



Input: 

```
tccli cpdp ModifyMntMbrBindRelateAcctBankCode --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2 \
    --ImageId img-pmqg1cw7 \
    --MrchCode 1234 \
    --SubAcctNo 1234000000006047 \
    --MemberBindAcctNo 6230551200054286369 \
    --AcctOpenBranchName 平安银行 \
    --EiconBankBranchId 307513207998
```

Output: 
```
{
    "Response": {
        "TxnReturnCode": "000000",
        "RequestId": "f8ee5d4b-9c32-46ec-80bd-96f7b4e2156a",
        "TxnReturnMsg": "交易成功",
        "ReservedMsg": "",
        "CnsmrSeqNo": "U862831911051572947730"
    }
}
```

