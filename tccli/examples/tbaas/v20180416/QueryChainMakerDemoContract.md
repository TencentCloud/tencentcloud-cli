**Example 1: 调用长安链体验网络合约查询**

调用长安链体验网络合约查询

Input: 

```
tccli tbaas QueryChainMakerDemoContract --cli-unfold-argument  \
    --ChainId chain_test \
    --ClusterId chainmaker-demo \
    --ContractName test \
    --FuncParam {"file_hash":"1234567"} \
    --FuncName find_by_file_hash
```

Output: 
```
{
    "Response": {
        "RequestId": "fac6ef5a-7637-4a75-a2d3-0f7d87b5b8b5",
        "Result": {
            "Code": 0,
            "CodeMessage": "OK",
            "Message": "",
            "TxId": "3ae794a658af4a219f849f5891d7a390eae524de4d614339ace2411059aaa19c",
            "GasUsed": 6100540,
            "Result": "b2s="
        }
    }
}
```

