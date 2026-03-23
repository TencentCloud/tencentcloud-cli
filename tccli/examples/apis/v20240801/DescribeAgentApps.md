**Example 1: 查询app列表**

查询app列表

Input: 

```
tccli apis DescribeAgentApps --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --InstanceID ins-e6fbc9b9
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "ApiKeys": [
                        "sk-***************************"
                    ],
                    "AppID": 1300273807,
                    "AuthType": "apiKey",
                    "CreateTime": "2025-07-14T06:09:49.354Z",
                    "Description": "desp",
                    "ID": "aga-71702335",
                    "InstanceID": "ins-e6fbc9b9",
                    "Name": "测试",
                    "SecretKeys": [],
                    "Status": "normal",
                    "Uin": "700001136234",
                    "UpdateTime": "2025-07-14T06:09:49.354Z"
                }
            ],
            "Total": 1
        },
        "RequestId": "73c48cae-cbf1-4377-b230-f1f42c89ff4c"
    }
}
```

