**Example 1: 创建SSH密钥对凭据**

创建SSH密钥对凭据

Input: 

```
tccli ssm CreateSSHKeyPairSecret --cli-unfold-argument  \
    --SecretName test2-sshkey-secret \
    --ProjectId 0 \
    --Description 描述信息 \
    --KmsKeyId 6abd1fdb-86d4-11ef-b72d-52540089bc41 \
    --Tags.0.TagKey env \
    --Tags.0.TagValue dev \
    --SSHKeyName test2_key
```

Output: 
```
{
    "Response": {
        "RequestId": "591e2b21-20e9-4621-8e4a-2697b89e985a",
        "SSHKeyID": "skey-e0vbh2ts",
        "SSHKeyName": "test2_key",
        "SecretName": "test2-sshkey-secret",
        "TagCode": 0,
        "TagMsg": "ok"
    }
}
```

