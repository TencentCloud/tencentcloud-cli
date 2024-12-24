**Example 1: 授权用户云资源**



Input: 

```
tccli dsgc AuthorizeDSPAMetaResources --cli-unfold-argument  \
    --AuthType automatic \
    --DspaId dspa-6fb60936 \
    --MetaType cdb \
    --ResourceRegion ap-guangzhou \
    --ResourcesAccount.0.ResourceId cdb-9loqa8ed \
    --ResourcesAccount.0.UserName root \
    --ResourcesAccount.0.Password password
```

Output: 
```
{
    "Response": {
        "RequestId": "c1b55d08-d956-447e-9852-a93bbb6f5d55",
        "DspaId": "dspa-6fb60936",
        "Results": [
            {
                "Result": "success",
                "ResultDescription": "auth resource success",
                "ResourceId": "cdb-9loqa8ed",
                "MetaType": "cdb"
            }
        ]
    }
}
```

