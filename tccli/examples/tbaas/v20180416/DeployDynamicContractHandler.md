**Example 1: 动态部署合约**



Input: 

```
tccli tbaas DeployDynamicContractHandler --cli-unfold-argument  \
    --Module contract \
    --Operation deploy_dynamic_contract \
    --GroupPk 11_1 \
    --ContractName StorageCell \
    --AbiInfo [{"outputs":[{"name":"","type":"string"}],"constant":true,"payable":false,"inputs":[],"name":"getVersion","stateMutability":"view","type":"function"},{"outputs":[{"name":"","type":"string"},{"name":"","type":"string"}],"constant":true,"payable":false,"inputs":[],"name":"getStorageCell","stateMutability":"view","type":"function"},{"outputs":[],"constant":false,"payable":false,"inputs":[{"name":"n","type":"string"}],"name":"setVersion","stateMutability":"nonpayable","type":"function"},{"payable":false,"inputs":[{"name":"storageHash","type":"string"},{"name":"storageInfo","type":"string"}],"stateMutability":"nonpayable","type":"constructor"}] \
    --ByteCodeBin 608060405234801561001057600080fd5b50604051610xxx...xxa2f0029 \
    --ConstructorParams aaaaa
```

Output: 
```
{
    "Response": {
        "RequestId": "2cfd9111-1954-4c2e-9564-975ce1d9ad2b",
        "ContractAddress": "0xasdfasdf23fasdfas2Qreffasfaefad"
    }
}
```

