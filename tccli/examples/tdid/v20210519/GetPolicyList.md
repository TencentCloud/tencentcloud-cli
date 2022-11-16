**Example 1: GetPolicyList**

披露策略Policy管理列表

Input: 

```
tccli tdid GetPolicyList --cli-unfold-argument  \
    --DisplayStart 0 \
    --DisplayLength 10
```

Output: 
```
{
    "Response": {
        "PolicyDataList": [
            {
                "Id": 39,
                "Name": "",
                "ClusterId": "bcos-fmtkyt8xne",
                "GroupId": 1,
                "ServiceId": 0,
                "ContractAppId": 5,
                "PolicyId": 2000047,
                "CptId": 3000007,
                "PolicyJson": "{\"cptType\": \"original\",\"$schema\": \"http://json-schema.org/draft-04/schema#\",\"description\": \"rtehreher\",\"title\": \"fwwfwfw\",\"type\": \"object\",\"properties\": {\"rtrey\": {      \"description\": \"wrwetwe\",\"type\": \"string\"    },\"age\": {      \"description\": \"the age of certificate owner\",      \"type\": \"number\"    }  }, \"required\": [    \"rtrey\",\"age\"  ]}",
                "CreateTime": "2021-07-19 10:24:19",
                "UpdateTime": "2021-07-19 10:24:19",
                "CreatorDid": "did:tdid:1:0x3c4d1e80a1bb5a2558b50ca4b76b85c88bfbf472",
                "AppName": "tesaba4"
            }
        ],
        "AllCount": 39,
        "RequestId": "b447f3a7-8c7c-4550-bbd8-ba47a7255768"
    }
}
```

