**Example 1: 获取区块内的交易列表**



Input: 

```
tccli tbaas GetBlockTransactionListForUser --cli-unfold-argument  \
    --Module transaction \
    --Operation block_transaction_list_for_user \
    --ClusterId 251005746bcdk3eis17qe \
    --GroupName org1 \
    --ChannelName fronttest3 \
    --BlockId 2 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "4697d721-ef88-4dba-96b2-5c9143773a6f",
        "TotalCount": 1,
        "TransactionList": [
            {
                "BlockHeight": 3,
                "BlockId": 2,
                "CreateOrgName": "org1",
                "CreateTime": "2020-01-06 22:18:15",
                "TransactionHash": "b5e398182b07bbde523e63804ee24690323bd5e190db99da079a00af2d71b652",
                "TransactionId": "0af5b0ae129b0435aa4ec8547c7500f428673dee363331f2f5f8d61d49e43e68",
                "TransactionStatus": "VALID",
                "TransactionType": "ENDORSER_TRANSACTION"
            }
        ]
    }
}
```

