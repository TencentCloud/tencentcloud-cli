**Example 1: InvokeFabricChaincode**

InvokeFabricChaincode

Input: 

```
tccli tbaas InvokeFabricChaincode --cli-unfold-argument  \
    --ClusterId fabric-65z42qi150 \
    --ChannelId channel-9xej4d \
    --ChaincodeName mytest \
    --FuncName Set \
    --FuncParam D 40 \
    --WithAsyncResult False
```

Output: 
```
{
    "Response": {
        "RequestId": "bab100f3-be40-415c-b29b-3a44c77b25fe",
        "TxId": "0595a33e308170b035e0d97c1a79274ac55badf048c0c8fc569719e14a2990c5",
        "TxResult": "",
        "TxStatus": "VALID"
    }
}
```

