**Example 1: 创建账号**

创建账号

Input: 

```
tccli cdb CreateAccounts --cli-unfold-argument  \
    --InstanceId cdb-lzl4lvov \
    --CreateAccounts.0.User api_ssm_concurrent_test \
    --CreateAccounts.0.Host % \
    --CreateAccounts.0.SSMInfos.IsOpenSSM True \
    --CreateAccounts.0.SSMInfos.IsRotationAccount False \
    --CreateAccounts.0.SSMInfos.SecretName api_ssm_concurrent_test \
    --CreateAccounts.0.SSMInfos.EncryptType 1 \
    --CreateAccounts.0.SSMInfos.EnableRotation False \
    --Password fsdgfdgfd43564654 \
    --MaxUserConnections 33
```

Output: 
```
{
    "Response": {
        "AsyncRequestId": "5e0fd33e-1afe758f-8bebfc08-e7a9141b",
        "RequestId": "4da3ccd3-ac33-4e5a-b733-52cde384f4c4"
    }
}
```

