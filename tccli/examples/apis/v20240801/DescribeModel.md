**Example 1: 查询模型详情**



Input: 

```
tccli apis DescribeModel --cli-unfold-argument  \
    --InstanceID ins-a7af1980 \
    --ID mod-e6866e22
```

Output: 
```
{
    "Response": {
        "Data": {
            "AppID": 1300273807,
            "CheckTargetCertsError": false,
            "CreateTime": "2026-02-03T07:35:59.803Z",
            "CredentialID": "",
            "CredentialName": "",
            "HttpProtocolType": "https",
            "HttpProtocolVersion": "1.1",
            "ID": "mod-e6866e22",
            "InstanceID": "ins-a7af1980",
            "LastUpdateTime": "2026-02-03T07:35:59.803Z",
            "ModelServiceCount": 0,
            "Name": "deepseek",
            "TargetHosts": [
                {
                    "Host": "10.2.1.0",
                    "Rank": 10
                }
            ],
            "TargetPath": "/v1",
            "Uin": "700001136234"
        },
        "RequestId": "3cd3dfe6-2aac-44f2-a886-03e4412eb618"
    }
}
```

