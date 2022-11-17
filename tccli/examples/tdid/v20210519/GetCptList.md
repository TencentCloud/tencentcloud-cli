**Example 1: GetCptList**

凭证模版列表

Input: 

```
tccli tdid GetCptList --cli-unfold-argument  \
    --DisplayStart 0 \
    --DisplayLength 10 \
    --CptType 3
```

Output: 
```
{
    "Response": {
        "CptDataList": [
            {
                "Id": 2,
                "Name": "",
                "ClusterId": "bcos-fmtkyt8xne",
                "GroupId": 1,
                "ServiceId": 1,
                "ContractAppId": 5,
                "CptId": 3000009,
                "CptType": 3,
                "Description": "",
                "CptJson": "{\n  \"cptType\": \"original\",\n  \"$schema\": \"http://json-schema.org/draft-04/schema#\",\n  \"description\": \"rtehreher\",\n  \"title\": \"fwwfwfw\",\n  \"type\": \"object\",\n  \"properties\": {\n    \"rtrey\": {\n      \"description\": \"wrwetwe\",\n      \"type\": \"string\"\n    },\n\"age\": {\n      \"description\": \"the age of certificate owner\",\n      \"type\": \"number\"\n    }\n  },\n  \"required\": [\n    \"rtrey\",\"age\"\n  ]\n}",
                "CreateTime": "2021-07-14 22:21:39",
                "UpdateTime": "2021-07-14 22:21:39",
                "CreatorDid": "did:tdid:1:0x3c4d1e80a1bb5a2558b50ca4b76b85c88bfbf472",
                "AppName": "tesaba4"
            },
            {
                "Id": 3,
                "Name": "test",
                "ClusterId": "bcos-fmtkyt8xne",
                "GroupId": 1,
                "ServiceId": 1,
                "ContractAppId": 5,
                "CptId": 3000010,
                "CptType": 3,
                "Description": "aaaaa",
                "CptJson": "{\n  \"cptType\": \"original\",\n  \"$schema\": \"http://json-schema.org/draft-04/schema#\",\n  \"description\": \"rtehreher\",\n  \"title\": \"fwwfwfw\",\n  \"type\": \"object\",\n  \"properties\": {\n    \"rtrey\": {\n      \"description\": \"wrwetwe\",\n      \"type\": \"string\"\n    },\n\"age\": {\n      \"description\": \"the age of certificate owner\",\n      \"type\": \"number\"\n    }\n  },\n  \"required\": [\n    \"rtrey\",\"age\"\n  ]\n}",
                "CreateTime": "2021-07-14 22:22:33",
                "UpdateTime": "2021-07-14 22:22:33",
                "CreatorDid": "did:tdid:1:0x3c4d1e80a1bb5a2558b50ca4b76b85c88bfbf472",
                "AppName": "tesaba4"
            },
            {
                "Id": 4,
                "Name": "test",
                "ClusterId": "bcos-fmtkyt8xne",
                "GroupId": 1,
                "ServiceId": 1,
                "ContractAppId": 5,
                "CptId": 3000011,
                "CptType": 3,
                "Description": "aaaaa",
                "CptJson": "{\n  \"cptType\": \"original\",\n  \"$schema\": \"http://json-schema.org/draft-04/schema#\",\n  \"description\": \"rtehreher\",\n  \"title\": \"fwwfwfw\",\n  \"type\": \"object\",\n  \"properties\": {\n    \"rtrey\": {\n      \"description\": \"wrwetwe\",\n      \"type\": \"string\"\n    },\n\"age\": {\n      \"description\": \"the age of certificate owner\",\n      \"type\": \"number\"\n    }\n  },\n  \"required\": [\n    \"rtrey\",\"age\"\n  ]\n}",
                "CreateTime": "2021-07-15 00:14:47",
                "UpdateTime": "2021-07-15 00:14:47",
                "CreatorDid": "did:tdid:1:0x3c4d1e80a1bb5a2558b50ca4b76b85c88bfbf472",
                "AppName": "tesaba4"
            }
        ],
        "AllCount": 4,
        "RequestId": ""
    }
}
```

