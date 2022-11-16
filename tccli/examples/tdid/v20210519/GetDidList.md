**Example 1: GetDidList**

DID列表

Input: 

```
tccli tdid GetDidList --cli-unfold-argument  \
    --Did did:tdid:bcos558:0x046553b6d60dde4255e406117c57c031878337bb \
    --ClusterId bcos-fmtkyt8xne \
    --GroupId 13 \
    --PageSize 10 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "DataList": [
            {
                "ServiceId": 51,
                "GroupId": 13,
                "AppName": "测试",
                "Did": "did:tdid:bcos558:0x046553b6d60dde4255e406117c57c031878337bb",
                "Remark": "",
                "AuthorityState": 0,
                "LabelName": "",
                "CreatedAt": "2021-07-24 09:04:05",
                "ClusterId": "bcos-fmtkyt8xne",
                "AllianceName": "bigbang",
                "LabelId": 0
            }
        ],
        "RequestId": "41a9acae-cef4-4949-b144-48c65ad5e425",
        "AllCount": 1
    }
}
```

