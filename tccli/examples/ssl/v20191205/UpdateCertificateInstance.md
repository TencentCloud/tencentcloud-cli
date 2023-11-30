**Example 1: 一键更新旧证书资源**

一键更新旧证书资源

Input: 

```
tccli ssl UpdateCertificateInstance --cli-unfold-argument  \
    --CertificateId abc \
    --OldCertificateId abc \
    --ResourceTypes abc \
    --Regions abc \
    --ResourceTypesRegions.0.ResourceType abc \
    --ResourceTypesRegions.0.Regions abc
```

Output: 
```
{
    "Response": {
        "DeployRecordId": 1,
        "DeployStatus": 0,
        "UpdateSyncProgress": [
            {
                "ResourceType": "abc",
                "UpdateSyncProgressRegions": [
                    {
                        "Region": "abc",
                        "TotalCount": 0,
                        "OffsetCount": 0,
                        "Status": "abc"
                    }
                ],
                "Status": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

