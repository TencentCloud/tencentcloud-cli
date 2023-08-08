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
        "DeployStatus": 1,
        "RequestId": "c9c9d2fb-41c0-43b6-8c10-44c81de553c1"
    }
}
```

