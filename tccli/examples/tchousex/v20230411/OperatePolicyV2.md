**Example 1: 创建策略**



Input: 

```
tccli tchousex OperatePolicyV2 --cli-unfold-argument  \
    --ApiType Create \
    --PolicyType 2 \
    --InstanceId instance-gpzb9mp1 \
    --PolicyName hangguolvtest \
    --Database data_mask3 \
    --Table orders
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "",
        "ReturnData": "\"2a106914-66e8-4e43-a9d1-c7022a56a29a\"",
        "RequestId": "0d830c35-67ea-476e-95ad-0582f4ba00de"
    }
}
```

