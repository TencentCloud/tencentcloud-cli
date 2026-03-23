**Example 1: 查询Credential列表**

查询Credential列表

Input: 

```
tccli apis DescribeAgentCredentials --cli-unfold-argument  \
    --Limit 10 \
    --InstanceID ins-e6fbc9b9 \
    --Offset 0 \
    --Keyword test
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AppID": 1300273807,
                    "Content": {
                        "Headers": [
                            {
                                "Key": "x-rio-signature",
                                "Value": "123456789"
                            }
                        ],
                        "STSService": "",
                        "STSSystem": ""
                    },
                    "CreateTime": "2025-07-14T07:22:40.347Z",
                    "ID": "agc-f4431972",
                    "InstanceID": "ins-e6fbc9b9",
                    "LastUpdateTime": "2025-07-14T07:22:40.347Z",
                    "Name": "测试凭据",
                    "RelateAgentAppNum": 0,
                    "RelateMcpServerNum": 0,
                    "Status": "normal",
                    "Type": "reqKey",
                    "Uin": "700001136234"
                }
            ],
            "Total": 1
        },
        "RequestId": "77fc4cfd-ca44-4986-9f71-9175b3aaaaca"
    }
}
```

