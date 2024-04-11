**Example 1: 开启CAM认证**

开启CAM认证

Input: 

```
tccli cam OpenDataFlowAuth --cli-unfold-argument  \
    --ResourceId cdb-ed23s1 \
    --ResourceRegion ap-shanghai \
    --ResourceAccount ReadOnly \
    --ResourceType cdb \
    --AccountHost %
```

Output: 
```
{
    "Response": {
        "CredentialName": "DBTKN_*Only",
        "RequestId": "586de8c1-58a2-48f7-b765-9843085b4c53"
    }
}
```

