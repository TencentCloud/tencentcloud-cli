**Example 1: RevokeMemberRechargeThirdPay**



Input: 

```
tccli cpdp RevokeMemberRechargeThirdPay --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2 \
    --ImageId img-pmqg1cw7 \
    --OldFillFrontSeqNo ' 1911190080016301' \
    --OldFillPayChannelType 0002 \
    --OldPayChannelTranSeqNo ' ALIPAY2019111904' \
    --OldFillEjzbOrderNo ' JZB2019111904' \
    --ApplyCancelMemberAmt 100 \
    --ApplyCancelCommission 1 \
    --MrchCode 1234
```

Output: 
```
{
    "Response": {
        "ReservedMsgTwo": "",
        "TxnReturnCode": "000000",
        "RequestId": "aef7a2ec-d2d6-4074-9fcd-cedc1d3420bf",
        "TxnReturnMsg": "交易成功",
        "FrontSeqNo": "1911180079875084",
        "CnsmrSeqNo": "U862831911181574068457",
        "ReservedMsgOne": ""
    }
}
```

