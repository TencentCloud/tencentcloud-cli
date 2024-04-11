**Example 1: 轮转认证**

轮转认证

Input: 

```
tccli cam RotateDataFlowAuth --cli-unfold-argument  \
    --ResourceId cdb-df31ss \
    --ResourceRegion ap-shanghai \
    --ResourceAccount ReadOnly \
    --ResourceType cdb \
    --AccountHost %
```

Output: 
```
{
    "Response": {
        "CredentialName": "DBTKN*ReadOnly",
        "RequestId": "1e1ef548-5138-4a9a-aa1e-70df71065799"
    }
}
```

