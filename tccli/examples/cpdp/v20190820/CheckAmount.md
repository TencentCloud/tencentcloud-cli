**Example 1: CheckAmount**



Input: 

```
tccli cpdp CheckAmount --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2 \
    --ImageId img-pmqg1cw7 \
    --MrchCode 1234 \
    --TranNetMemberCode ' YAPI100016' \
    --TakeCashAcctNo ' 6231582000409285123' \
    --AuthAmt 0.01 \
    --Ccy RMB
```

Output: 
```
{
    "Response": {
        "TxnReturnCode": "000000",
        "RequestId": "a9baed23-dac5-48ff-b02a-085618d9c7db",
        "TxnReturnMsg": "交易成功",
        "FrontSeqNo": "1912060087178757",
        "ReservedMsg": "",
        "CnsmrSeqNo": "U862831912061575632834"
    }
}
```

