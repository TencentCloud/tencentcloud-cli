**Example 1: QuerySmallAmountTransfer**



Input: 

```
tccli cpdp QuerySmallAmountTransfer --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2 \
    --ImageId img-pmqg1cw7 \
    --MrchCode 1234 \
    --OldTranSeqNo U12345678910 \
    --TranDate 20191206
```

Output: 
```
{
    "Response": {
        "TxnReturnCode": "000000",
        "RequestId": "36c86a8d-516e-4e4a-82af-3c33ecd18955",
        "ReturnMsg": "绑定已成功",
        "TxnReturnMsg": "交易成功",
        "ReservedMsg": "",
        "ReturnStatus": "0",
        "CnsmrSeqNo": "U862831912061575632926"
    }
}
```

