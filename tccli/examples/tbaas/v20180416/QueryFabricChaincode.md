**Example 1: QueryFabricChaincode**

QueryFabricChaincode

Input: 

```
tccli tbaas QueryFabricChaincode --cli-unfold-argument  \
    --ClusterId fabric-65z42qi150 \
    --ChannelId channel-9xej4d \
    --ChaincodeName mytest \
    --FuncName Get \
    --FuncParam A
```

Output: 
```
{
    "Response": {
        "RequestId": "e431d04c-2a5c-43b4-a480-f127b3f46eb6",
        "TxId": "030acb112f9f2aa2ce537fea9d94d2f3c9ec6cf8e05aa62f5d3746167825dbe8",
        "TxResult": "10",
        "TxStatus": "VALID"
    }
}
```

