**Example 1: 外部联系人转换接口**



Input: 

```
tccli wav QueryExternalUserMappingInfo --cli-unfold-argument  \
    --CorpExternalUserIdList sacxhdsfknasddfasdf2332edsad safd32SADFSf23r2fdsfsd
```

Output: 
```
{
    "Response": {
        "ExternalUserIdMapping": [
            {
                "CorpExternalUserId": "safdIDSFNfsdxxxywsdfRwxxfdDXfs",
                "ExternalUserId": "safdIDSFNfsdxxxywsdfRwxxfdDXfs"
            }
        ],
        "RequestId": "b1a024bf-4d74-4b5d-a5bd-bbec330520e8"
    }
}
```

