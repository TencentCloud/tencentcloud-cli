**Example 1: 恢复计划删除中的凭据**



Input: 

```
tccli ssm RestoreSecret --cli-unfold-argument  \
    --SecretName test
```

Output: 
```
{
    "Response": {
        "RequestId": "bf199317-0d31-4dba-a5e7-217dc37df2d4",
        "SecretName": "test"
    }
}
```

