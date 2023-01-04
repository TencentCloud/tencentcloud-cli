**Example 1: 查询异步模式下Invoke接口的调用结果**



Input: 

```
tccli tbaas GetInvokeTx --cli-unfold-argument  \
    --PeerGroup NewOrg02 \
    --ClusterId 251005746envnew \
    --PeerName peer0.neworg02.envnew \
    --Module transaction \
    --TxId 280e9f1436c3ce045af4f3c7060ff217583585d41faf1f1daa99387419bac07c \
    --GroupName NewOrg02 \
    --Operation query_txid \
    --ChannelName ch042103
```

Output: 
```
{
    "Response": {
        "BlockId": 6,
        "RequestId": "551b801e-6dbe-46be-aa46-f8cc3ff1cd09",
        "TxValidationCode": 0,
        "TxValidationMsg": "VALID"
    }
}
```

