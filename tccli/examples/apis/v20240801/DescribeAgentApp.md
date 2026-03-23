**Example 1: 查询app详情**

查询app详情

Input: 

```
tccli apis DescribeAgentApp --cli-unfold-argument  \
    --ID aga-71702335 \
    --InstanceID ins-e6fbc9b9
```

Output: 
```
{
    "Response": {
        "Data": {
            "ApiKeys": [
                "sk-d3b6f59b27B792B7dd6aeb26554D0DAC"
            ],
            "AppID": 1300273807,
            "AuthType": "apiKey",
            "CreateTime": "2025-07-14T06:09:49.354Z",
            "Description": "测试desp",
            "ID": "aga-71702335",
            "InstanceID": "ins-e6fbc9b9",
            "Name": "测试app",
            "SecretKeys": [],
            "Status": "normal",
            "Uin": "700001136234",
            "UpdateTime": "2025-07-14T06:13:55.995Z"
        },
        "RequestId": "7020c298-312c-4cc6-9f77-66d64c22936e"
    }
}
```

