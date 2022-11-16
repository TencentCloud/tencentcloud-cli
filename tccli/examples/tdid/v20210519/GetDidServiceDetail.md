**Example 1: ClusterName**

网络基本信息

Input: 

```
tccli tdid GetDidServiceDetail --cli-unfold-argument  \
    --ServiceId 1
```

Output: 
```
{
    "Response": {
        "DidService": {
            "Id": 1,
            "Appid": 251005745,
            "Uin": "1298334110",
            "ConsortiumId": 617,
            "ConsortiumName": "bigbang",
            "ClusterId": "bcos-fmtkyt8xne",
            "GroupId": 1,
            "ChainId": "",
            "RoleType": 0,
            "AgencyDid": "did:tdid:1:0x3c4d1e80a1bb5a2558b50ca4b76b85c88bfbf472",
            "CreateOrg": "test",
            "Endpoint": "http://127.0.0.1:6001",
            "CreateTime": "2021-07-12T21:27:23+08:00",
            "UpdateTime": "2021-07-12T21:27:23+08:00"
        },
        "RequestId": "41a9acae-cef4-4949-b144-48c65ad5e425"
    }
}
```

