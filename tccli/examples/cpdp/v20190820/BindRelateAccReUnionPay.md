**Example 1: BindRelateAccReUnionPay**



Input: 

```
tccli cpdp BindRelateAccReUnionPay --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2 \
    --ImageId img-pmqg1cw7 \
    --MrchCode 1234 \
    --TranNetMemberCode YAPI100015 \
    --MemberAcctNo ' 6230515000261997142' \
    --MessageCheckCode 000000
```

Output: 
```
{
    "Response": {
        "TxnReturnCode": "000000",
        "RequestId": "562d84b1-a426-4d09-baaf-94fb94061503",
        "TxnReturnMsg": "交易成功",
        "FrontSeqNo": "1912060087178182",
        "ReservedMsg": "",
        "CnsmrSeqNo": "U862831912061575632588"
    }
}
```

