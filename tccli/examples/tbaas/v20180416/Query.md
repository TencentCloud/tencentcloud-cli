**Example 1: 查询汽车信息**



Input: 

```
tccli tbaas Query --cli-unfold-argument  \
    --Module transaction \
    --Operation query \
    --ClusterId 251005746envnew \
    --Peers.0.PeerName peer0.neworg02.envnew \
    --Peers.0.OrgName NewOrg02 \
    --ChannelName ch042103 \
    --ChaincodeName cc050301 \
    --FuncName queryCar \
    --Args CAR92 \
    --GroupName NewOrg02
```

Output: 
```
{
    "Response": {
        "Data": [
            "{\"make\":\"Chevy\",\"model\":\"Volt\",\"colour\":\"Black\",\"owner\":\"Nick\"}"
        ],
        "RequestId": "3f6836c5-e889-431e-b932-47a1653c5f7b"
    }
}
```

