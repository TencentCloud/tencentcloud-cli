**Example 1: 获取交易详情**



Input: 

```
tccli tbaas GetTransactionDetailForUser --cli-unfold-argument  \
    --Module transaction \
    --Operation transaction_detail_for_user \
    --ClusterId 251005746bcd6xjfka7pi \
    --GroupName org2 \
    --ChannelName tyler \
    --BlockId 0 \
    --TransactionId 42c562517707bf53f08fe6e5a1cf5f50c784352ff0d8166e77514ebe518bd6c0
```

Output: 
```
{
    "Response": {
        "BlockHash": "a0f1bd5819e1e664873c3d903d005f9f24661986c2c4c541a185f613fdeaff52",
        "BlockHeight": 1,
        "BlockId": 0,
        "ChannelName": "tyler",
        "ContractName": "",
        "CreateOrgName": "org2",
        "CreateTime": "2019-10-28 18:48:28",
        "EndorserOrgList": [
            {
                "EndorserGroupName": "org2",
                "EndorserPeerList": [
                    "Admin.org2.bcd6xjfka7pi"
                ]
            }
        ],
        "RequestId": "a13c4aed-ba4a-4357-850a-66707d7d5e74",
        "TransactionData": "\"\"",
        "TransactionHash": "",
        "TransactionId": "42c562517707bf53f08fe6e5a1cf5f50c784352ff0d8166e77514ebe518bd6c0",
        "TransactionStatus": "VALID",
        "TransactionType": "CONFIG"
    }
}
```

