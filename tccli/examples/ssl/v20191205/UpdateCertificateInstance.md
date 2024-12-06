**Example 1: 一键更新旧证书资源**

一键更新旧证书资源

Input: 

```
tccli ssl UpdateCertificateInstance --cli-unfold-argument  \
    --CertificateId Th**jj \
    --OldCertificateId gej**kkk \
    --ResourceTypes clb \
    --Regions ap-guangzhou \
    --ResourceTypesRegions.0.ResourceType clb \
    --ResourceTypesRegions.0.Regions ap-guangzhou
```

Output: 
```
{
    "Response": {
        "DeployRecordId": 1763489,
        "DeployStatus": 0,
        "UpdateSyncProgress": [
            {
                "ResourceType": "clb",
                "UpdateSyncProgressRegions": [
                    {
                        "Region": "ap-guangzhou",
                        "TotalCount": 0,
                        "OffsetCount": 0,
                        "Status": 0
                    }
                ],
                "Status": 0
            }
        ],
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

