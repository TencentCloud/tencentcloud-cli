**Example 1: 查询AI模型列表**



Input: 

```
tccli tcb DescribeAIModels --cli-unfold-argument  \
    --EnvId test_envid
```

Output: 
```
{
    "Response": {
        "AIModels": [
            {
                "BaseUrl": "https://api.hunyuan.cloud.tencent.com",
                "GroupName": "hunyuan-exp",
                "Models": [
                    {
                        "EnableMCP": false,
                        "Model": "hunyuan-lite"
                    },
                    {
                        "EnableMCP": true,
                        "Model": "hunyuan-turbos-latest"
                    },
                    {
                        "EnableMCP": true,
                        "Model": "hunyuan-t1-latest"
                    }
                ],
                "Remark": "",
                "Secret": {
                    "ApiKey": "",
                    "SecretId": "",
                    "SecretKey": ""
                },
                "Status": 1,
                "Type": "builtin"
            },
            {
                "BaseUrl": "https://api.lkeap.cloud.tencent.com",
                "GroupName": "deepseek",
                "Models": [
                    {
                        "EnableMCP": false,
                        "Model": "deepseek-r1"
                    },
                    {
                        "EnableMCP": false,
                        "Model": "deepseek-v3"
                    },
                    {
                        "EnableMCP": false,
                        "Model": "deepseek-0324"
                    }
                ],
                "Remark": "",
                "Secret": {
                    "ApiKey": "",
                    "SecretId": "",
                    "SecretKey": ""
                },
                "Status": 1,
                "Type": "builtin"
            }
        ],
        "RequestId": "fd638756-5ea9-4b82-85ba-8544ce0d054d"
    }
}
```

