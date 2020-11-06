**Example 1: 修改会员属性-普通商户子账户**



Input: 

```
tccli cpdp ReviseMbrProperty --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2 \
    --ImageId img-pmqg1cw7 \
    --MrchCode 1234 \
    --SubAcctNo 1234000000001008 \
    --MemberProperty SH
```

Output: 
```
{
    "Response": {
        "TxnReturnCode": "000000",
        "RequestId": "63ba30a8-b4ca-41db-a171-60a8ee048f25",
        "TxnReturnMsg": "交易成功",
        "ReservedMsg": "",
        "CnsmrSeqNo": "U862831911061573031534"
    }
}
```

