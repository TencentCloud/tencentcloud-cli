**Example 1: 调用长安链体验网络合约执行交易**

调用长安链体验网络合约执行交易

Input: 

```
tccli tbaas InvokeChainMakerDemoContract --cli-unfold-argument  \
    --ChainId chain_demo \
    --FuncParam {"key":"key1","field":"field1","value":"value1"} \
    --ClusterId chainmaker-demo \
    --FuncName save \
    --AsyncFlag 0 \
    --ContractName fact
```

Output: 
```
{
    "Response": {
        "RequestId": "2974e7ac-72e2-49c3-ae39-bc2bc6a7330b",
        "Result": {
            "Code": 0,
            "CodeMessage": "OK",
            "Message": "",
            "TxId": "963b8210f10e45e6ab6fe5cd37ba7f6719db5948a38c494ca9137fa2b8c9033d",
            "GasUsed": 9573483,
            "Result": "b2s="
        }
    }
}
```

