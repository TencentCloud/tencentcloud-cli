**Example 1: 查询长安链体验网络指定高度区块的交易**

查询长安链体验网络指定高度区块的交易

Input: 

```
tccli tbaas QueryChainMakerDemoBlockTransaction --cli-unfold-argument  \
    --BlockHeight 2 \
    --ChainId chain_test \
    --ClusterId chainmaker-demo
```

Output: 
```
{
    "Response": {
        "RequestId": "0c64831e-a310-47c7-bf6c-a625c5cfde17",
        "BlockHeight": 2,
        "TxCount": 1,
        "BlockTimestamp": 1627267176,
        "Result": [
            {
                "Code": 0,
                "CodeMessage": "",
                "Message": "",
                "TxId": "f6cf450f9b0b496f9ee6d332e739b8b182fe1e3b34ed446ab068a151f1ee8cbe",
                "Timestamp": 1627267173,
                "GasUsed": 230871,
                "BlockHeight": 2,
                "ContractEvent": ""
            }
        ]
    }
}
```

