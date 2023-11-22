**Example 1: 创建汽车信息——同步模式**



Input: 

```
tccli tbaas Invoke --cli-unfold-argument  \
    --Module transaction \
    --Operation invoke \
    --ClusterId 251005746envnew \
    --Peers.0.PeerName peer0.neworg02.envnew \
    --Peers.0.OrgName NewOrg02 \
    --ChannelName ch042103 \
    --ChaincodeName cc050301 \
    --FuncName createCar \
    --Args CAR92 Chevy Volt Black Nick \
    --GroupName NewOrg02
```

Output: 
```
{
    "Response": {
        "Events": "myOrgpeer0.myorg.envnew:VALID",
        "RequestId": "0b82b65e-7100-49f1-9f29-e934a8833711",
        "TxId": "0366ab8f31c9f8aa6b9fc9506fa841e55d1ecd492b3ecc373c0f66ca49f33ea1"
    }
}
```

**Example 2: 创建汽车信息——异步模式**



Input: 

```
tccli tbaas Invoke --cli-unfold-argument  \
    --Module transaction \
    --Operation invoke \
    --ClusterId 251005746envnew \
    --Peers.0.PeerName peer0.neworg02.envnew \
    --Peers.0.OrgName NewOrg02 \
    --ChannelName ch042103 \
    --ChaincodeName cc050301 \
    --FuncName createCar \
    --Args CAR92 Chevy Volt Black Nick \
    --AsyncFlag 1 \
    --GroupName NewOrg02
```

Output: 
```
{
    "Response": {
        "Events": "",
        "RequestId": "51ad1047-30c0-4397-b672-37e8ffd65d9f",
        "TxId": "280e9f1436c3ce045af4f3c7060ff217583585d41faf1f1daa99387419bac07c"
    }
}
```

