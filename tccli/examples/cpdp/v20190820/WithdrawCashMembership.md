**Example 1: WithdrawCashMembership**



Input: 

```
tccli cpdp WithdrawCashMembership --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2 \
    --ImageId img-pmqg1cw7 \
    --MrchCode 1234 \
    --TranWebName APITEST \
    --MemberGlobalType 1 \
    --MemberGlobalId ' 433112345210255839' \
    --TranNetMemberCode ' YAPI100015' \
    --MemberName demo \
    --TakeCashAcctNo ' 6230280003161991234' \
    --OutAmtAcctName demo \
    --Ccy RMB \
    --CashAmt 33
```

Output: 
```
{
    "Response": {
        "TxnReturnCode": "000000",
        "RequestId": "000fc964-9cca-41de-b41b-7a000d065096",
        "TxnReturnMsg": "交易接收成功,请稍后查询处理结果",
        "FrontSeqNo": "1912060087179879",
        "ReservedMsg": "",
        "TransferFee": "0.00",
        "CnsmrSeqNo": "U862831912061575633475"
    }
}
```

