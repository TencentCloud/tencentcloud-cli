**Example 1: 绑定密钥对到实例**

绑定一个密钥对到实例上。

Input: 

```
tccli lighthouse AssociateInstancesKeyPairs --cli-unfold-argument  \
    --InstanceIds lhins-ruy9d2tw \
    --KeyIds lhkp-f7rjie1q
```

Output: 
```
{
    "Response": {
        "RequestId": "f192c1a9-580e-4653-9d54-ba42cd4353a3"
    }
}
```

