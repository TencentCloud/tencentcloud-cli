**Example 1: 解除实例的密钥绑定关系**



Input: 

```
tccli cvm DisassociateInstancesKeyPairs --cli-unfold-argument  \
    --InstanceIds ins-w34e5rl9 \
    --KeyIds skey-e3r6y7ji
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

