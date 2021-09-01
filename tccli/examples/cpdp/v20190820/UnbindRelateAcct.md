**Example 1: UnbindRelateAcct**



Input: 

```
tccli cpdp UnbindRelateAcct --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2 \
    --ImageId img-pmqg1cw7 \
    --MrchCode 1234 \
    --FunctionFlag 1 \
    --TranNetMemberCode YAPI100000 \
    --MemberAcctNo ' 6230582000059121234'
```

Output: 
```
{
    "Response": {
        "TxnReturnCode": "000000",
        "RequestId": "01f7c43c-7429-4a0f-9e56-583a0746c0d5",
        "TxnReturnMsg": "交易成功",
        "FrontSeqNo": "1911060076987819",
        "ReservedMsg": "",
        "CnsmrSeqNo": "U862831911061573031795"
    }
}
```

