**Example 1: 创建SSH密钥对凭据**

创建SSH密钥对凭据

Input: 

```
tccli ssm CreateSSHKeyPairSecret --cli-unfold-argument  \
    --ProjectId 0 \
    --Tags.0.TagKey xx \
    --Tags.0.TagValue xx \
    --KmsKeyId xx \
    --Description xx \
    --SecretName xx \
    --SSHKeyName xx
```

Output: 
```
{
    "Response": {
        "SSHKeyID": "xx",
        "TagMsg": "xx",
        "TagCode": 1,
        "RequestId": "xx",
        "SecretName": "xx",
        "SSHKeyName": "xx"
    }
}
```

