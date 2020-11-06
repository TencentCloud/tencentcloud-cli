**Example 1: CreateCustAcctId**



Input: 

```
tccli cpdp CreateCustAcctId --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2 \
    --ImageId img-pmqg1cw7 \
    --FunctionFlag 1 \
    --FundSummaryAcctNo 15041201553971 \
    --TranNetMemberCode YAPI100015 \
    --MemberProperty SH \
    --UserNickname APITEST \
    --Mobile 110 \
    --Email test@tencent.com \
    --MrchCode 1234 \
    --SelfBusiness false \
    --ContactName API \
    --SubAcctName API \
    --SubAcctShortName API \
    --SubAcctType 1
```

Output: 
```
{
    "Response": {
        "TxnReturnCode": "000000",
        "RequestId": "3f9eb098-d94a-4d34-aefc-35325956923c",
        "TxnReturnMsg": "交易成功",
        "ReservedMsg": "",
        "CnsmrSeqNo": "U862831912061575630632",
        "SubAcctNo": "3691000000021018"
    }
}
```

