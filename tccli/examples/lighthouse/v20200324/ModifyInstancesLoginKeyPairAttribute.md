**Example 1: 禁止使用默认密钥对登录实例**



Input: 

```
tccli lighthouse ModifyInstancesLoginKeyPairAttribute --cli-unfold-argument  \
    --InstanceIds lhins-ruy9d2tw \
    --PermitLogin NO
```

Output: 
```
{
    "Response": {
        "RequestId": "fb3c565c-1ce9-43de-9b4e-58855716b16d"
    }
}
```

