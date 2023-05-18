**Example 1: 云资源更新一键回滚**

云资源更新一键回滚

Input: 

```
tccli ssl UpdateCertificateRecordRollback --cli-unfold-argument  \
    --DeployRecordId 1
```

Output: 
```
{
    "Response": {
        "DeployRecordId": 0,
        "RequestId": "xx"
    }
}
```

