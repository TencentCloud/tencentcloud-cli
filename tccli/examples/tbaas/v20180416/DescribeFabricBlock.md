**Example 1: DescribeFabricBlock**

DescribeFabricBlock

Input: 

```
tccli tbaas DescribeFabricBlock --cli-unfold-argument  \
    --ClusterId fabric-65z42qi150 \
    --ChannelId channel-9xej4d \
    --BlockHeight 4
```

Output: 
```
{
    "Response": {
        "BlockHash": "e0421ecc20340425a2cf01808469b2523651f8100da92a0287b3769115e57370",
        "BlockHeight": 4,
        "CreateTimestamp": "2023-08-05 07:44:04",
        "PreBlockHash": "f69b2b5a1884e5bbb077a3025378e2210b83bbada23b5c17045b0bf537a53bd0",
        "ProposerOrg": "区块链测试机构pettychen",
        "RequestId": "a6288649-01c0-4d8f-bdd4-ba02163d0721",
        "TransactionList": [
            {
                "BlockHeight": 4,
                "ChaincodeName": "_lifecycle",
                "CreateTime": "2023-08-05 15:44:04",
                "Sender": "区块链测试机构pettychen",
                "TxId": "03389f4a5af1883347ecdb15471e70abf3a8e6cf5b6648dc789674af7930e229"
            }
        ],
        "TxCount": 1
    }
}
```

