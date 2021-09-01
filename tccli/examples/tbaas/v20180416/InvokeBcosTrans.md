**Example 1: 发送Bcos合约交易**



Input: 

```
tccli tbaas InvokeBcosTrans --cli-unfold-argument  \
    --ContractAddress 0xec17aa9c9d530108529c68b41701231b9ae458ef \
    --ClusterId 251005746bc987bojjue8 \
    --SignUserId 2SSS200021 \
    --FuncName set \
    --AbiInfo [{"constant":false,"inputs":[{"name":"n","type":"string"}],"name":"set","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}] \
    --GroupId 1 \
    --FuncParam [10]
```

Output: 
```
{
    "Response": {
        "RequestId": "5461dfd7-ca9e-486d-9655-843bfa7bd9b8",
        "TransactionRsp": "{\"blockHash\":\"0x8be0f6288e887c84db48c48248f5e3cd41be81417c3294b0359f4b739beb661c\",\"blockNumber\":12,\"constant\":false,\"from\":\"0x1aa8003024e222205bfed0fc4786c3945dfe6090\",\"gasUsed\":23964,\"input\":\"0x4ed3885e0000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000573746f6e65000000000000000000000000000000000000000000000000000000\",\"output\":\"0x\",\"queryInfo\":null,\"status\":\"0x0\",\"to\":\"0x1b5fda9060597595afb818ee344499cf030ac445\",\"transactionHash\":\"0x950ee123437c4ebf115c94212b61ab759e56f2e2d1dd25b78de7383f16b40d72\"}"
    }
}
```

