**Example 1: 登记挂账**



Input: 

```
tccli cpdp RegisterBillSupportWithdraw --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2 \
    --ImageId img-pmqg1cw7 \
    --TranNetMemberCode ' YAPI100007' \
    --OrderNo ' O2019110603' \
    --SuspendAmt 1233 \
    --TranFee 0.0 \
    --MrchCode 1234
```

Output: 
```
{
    "Response": {
        "TxnReturnCode": "000000",
        "RequestId": "9746ad16-e2d6-4122-8e63-a39a805e1ea6",
        "TxnReturnMsg": "交易成功",
        "FrontSeqNo": "1911060076971376",
        "ReservedMsg": "",
        "CnsmrSeqNo": "U862831911061573026173"
    }
}
```

