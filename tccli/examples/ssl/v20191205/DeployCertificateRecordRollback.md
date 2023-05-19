**Example 1: 云资源部署一键回滚**

云资源部署一键回滚

Input: 

```
tccli ssl DeployCertificateRecordRollback --cli-unfold-argument  \
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

