**Example 1: 根据动态部署的合约发送交易**



Input: 

```
tccli tbaas TransByDynamicContractHandler --cli-unfold-argument  \
    --Module transaction \
    --Operation trans_by_dynamic_contract \
    --GroupPk 11_1 \
    --ContractAddress 0x19aa8753e76fd20adf97e893b63444565b862d1b \
    --ContractName StorageCell \
    --AbiInfo [{"outputs":[{"name":"","type":"string"}],"constant":true,"payable":false,"inputs":[],"name":"getVersion","stateMutability":"view","type":"function"},{"outputs":[{"name":"","type":"string"},{"name":"","type":"string"}],"constant":true,"payable":false,"inputs":[],"name":"getStorageCell","stateMutability":"view","type":"function"},{"outputs":[],"constant":false,"payable":false,"inputs":[{"name":"n","type":"string"}],"name":"setVersion","stateMutability":"nonpayable","type":"function"},{"payable":false,"inputs":[{"name":"storageHash","type":"string"},{"name":"storageInfo","type":"string"}],"stateMutability":"nonpayable","type":"constructor"}] \
    --FuncName getStorageCell \
    --FuncParam aaaa
```

Output: 
```
{
    "Response": {
        "RequestId": "2cfd9111-1954-4c2e-9564-975ce1d9ad2b",
        "TransactionRsp": "{\"transactionHash\":\"0xx\",\"blockHash\":\"0xx\"}"
    }
}
```

