**Example 1: 关闭CAM认证**

关闭CAM认证

Input: 

```
tccli cam CloseDataFlowAuth --cli-unfold-argument  \
    --ResourceId cdb-de32s4 \
    --ResourceRegion ap-guangzhou \
    --ResourceAccount ReadOnly \
    --ResourceType cdb \
    --AccountHost %
```

Output: 
```
{
    "Response": {
        "CredentialName": "DBTKN*ReadOnly",
        "RequestId": "de27022a-9561-4431-951d-f7b6a88ede05"
    }
}
```

