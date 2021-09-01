**Example 1: 登记挂账撤销**



Input: 

```
tccli cpdp RevResigterBillSupportWithdraw --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2 \
    --ImageId img-pmqg1cw7 \
    --MrchCode 1234 \
    --TranNetMemberCode ' YAPI100007' \
    --OldOrderNo ' O2019110603' \
    --CancelAmt 5000 \
    --TranFee 0.0
```

Output: 
```
{
    "Response": {
        "TxnReturnCode": "000000",
        "RequestId": "10f464bc-01bf-478d-af7a-75b782887fd1",
        "TxnReturnMsg": "交易成功",
        "FrontSeqNo": "1911060076971280",
        "ReservedMsg": "",
        "CnsmrSeqNo": "U862831911061573026066"
    }
}
```

