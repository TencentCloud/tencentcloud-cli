**Example 1: 会员在途充值(经第三方支付渠道)**



Input: 

```
tccli cpdp RechargeMemberThirdPay --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2 \
    --ImageId img-pmqg1cw7 \
    --TranNetMemberCode ' YAPI100000' \
    --MemberFillAmt 2000 \
    --Commission 10 \
    --Ccy RMB \
    --PayChannelType 0002 \
    --PayChannelAssignMerNo ' ALI0001' \
    --PayChannelTranSeqNo ' ALIPAY2019111801' \
    --EjzbOrderNo ' JZB2019111806' \
    --EjzbOrderContent iPhone11Pro \
    --MrchCode 1234
```

Output: 
```
{
    "Response": {
        "ReservedMsgTwo": "",
        "TxnReturnCode": "000000",
        "RequestId": "73e6e5ce-6a37-4d73-bf19-18a70557891c",
        "TxnReturnMsg": "交易成功",
        "FrontSeqNo": "1911180079874881",
        "CnsmrSeqNo": "U862831911181574068258",
        "MemberSubAcctPreAvailBal": "7200.0",
        "ReservedMsgOne": ""
    }
}
```

