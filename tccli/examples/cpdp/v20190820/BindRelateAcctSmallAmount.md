**Example 1: BindRelateAcctSmallAmount**



Input: 

```
tccli cpdp BindRelateAcctSmallAmount --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2 \
    --ImageId img-pmqg1cw7 \
    --MrchCode 1234 \
    --TranNetMemberCode ' YAPI100016' \
    --MemberName test \
    --MemberGlobalType 1 \
    --MemberGlobalId ' 631103897532298123' \
    --MemberAcctNo ' 6210582030042585123' \
    --BankType 1 \
    --AcctOpenBranchName xx银行 \
    --EiconBankBranchId ' 307123007998' \
    --Mobile 11111111111
```

Output: 
```
{
    "Response": {
        "TxnReturnCode": "000000",
        "RequestId": "7575459a-ebf5-4ba2-b5d7-1ba5e3272072",
        "TxnReturnMsg": "交易成功",
        "ReservedMsg": "",
        "CnsmrSeqNo": "U862831912061575632763"
    }
}
```

