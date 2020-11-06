**Example 1: BindRelateAcctUnionPay**



Input: 

```
tccli cpdp BindRelateAcctUnionPay --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2 \
    --ImageId img-pmqg1cw7 \
    --TranNetMemberCode YAPI100015 \
    --MemberName test \
    --MemberGlobalType 1 \
    --MemberGlobalId 431100195223255123 \
    --MemberAcctNo 6235180000561997123 \
    --BankType 1 \
    --AcctOpenBranchName xx银行 \
    --EiconBankBranchId 3075322051998 \
    --Mobile 11111111111 \
    --MrchCode 1234
```

Output: 
```
{
    "Response": {
        "TxnReturnCode": "000000",
        "RequestId": "414efcd9-61fd-44d4-a1fe-134b60a48128",
        "TxnReturnMsg": "银联验证成功，等待客户回填验证码",
        "ReservedMsg": "",
        "CnsmrSeqNo": "U862831912061575632485"
    }
}
```

