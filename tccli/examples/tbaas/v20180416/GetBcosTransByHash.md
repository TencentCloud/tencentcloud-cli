**Example 1: 使用Hash查询交易**



Input: 

```
tccli tbaas GetBcosTransByHash --cli-unfold-argument  \
    --TransHash 0x950ee123437c4ebf115c94212b61ab759e56f2e2d1dd25b78de7383f16b40d72 \
    --ClusterId bcos-d292gp0toy \
    --GroupId 15
```

Output: 
```
{
    "Response": {
        "RequestId": "51083339-ffaa-42d4-a272-51f354c14759",
        "TransactionJson": "{\"blockHash\":\"0x8be0f6288e887c84db48c48248f5e3cd41be81417c3294b0359f4b739beb661c\",\"blockNumber\":12,\"blockNumberRaw\":\"12\",\"creates\":null,\"from\":\"0x1aa8003024e222205bfed0fc4786c3945dfe6090\",\"gas\":100000000,\"gasPrice\":100000000,\"gasPriceRaw\":\"100000000\",\"gasRaw\":\"100000000\",\"hash\":\"0x950ee123437c4ebf115c94212b61ab759e56f2e2d1dd25b78de7383f16b40d72\",\"input\":\"0x4ed3885e0000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000573746f6e65000000000000000000000000000000000000000000000000000000\",\"nonce\":3.0404523452847157e+74,\"nonceRaw\":\"304045234528471549282051329892726108126972099205346767472045445814934456175\",\"publicKey\":null,\"r\":null,\"raw\":null,\"s\":null,\"to\":\"0x1b5fda9060597595afb818ee344499cf030ac445\",\"transactionIndex\":0,\"transactionIndexRaw\":\"0\",\"v\":0,\"value\":0,\"valueRaw\":\"0\"}"
    }
}
```

