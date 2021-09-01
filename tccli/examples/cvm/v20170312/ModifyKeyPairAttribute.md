**Example 1: 修改密钥对名称**

本示例用于修改密钥对名称。

Input: 

```
tccli cvm ModifyKeyPairAttribute --cli-unfold-argument  \
    --KeyId skey-mv9yzyjj \
    --KeyName Tencent
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

**Example 2: 修改密钥对描述信息**

本示例用于修改密钥对描述信息。

Input: 

```
tccli cvm ModifyKeyPairAttribute --cli-unfold-argument  \
    --KeyId skey-mv9yzyjj \
    --Description Tencent
```

Output: 
```
{
    "Response": {
        "RequestId": "aea2227b-fbb7-4cc7-bf29-d49b2b6db97c"
    }
}
```

