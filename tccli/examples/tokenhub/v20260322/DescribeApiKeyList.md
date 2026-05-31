**Example 1: 查询 API 密钥列表。**

查询当前用户的 API 密钥列表，密钥值脱敏展示。支持分页、过滤和排序。

Input: 

```
tccli tokenhub DescribeApiKeyList --cli-unfold-argument  \
    --Platform maas \
    --Filters.0.Name apiKeyName \
    --Filters.0.Op EXACT \
    --Filters.0.Values my-apikey
```

Output: 
```
{
    "Response": {
        "ApiKeySet": [
            {
                "ApiKey": "sk-2b***3sQc",
                "ApiKeyId": "ak-20260325-xxxxxx",
                "AppId": "1300056794",
                "BindType": "model_custom_endpoint_custom",
                "BindingItems": [
                    {
                        "ResourceId": "deepseek-v3.2",
                        "ResourceType": "model"
                    }
                ],
                "CreateTime": "2026-03-25 19:50:56",
                "Creator": "",
                "Editable": true,
                "Name": "my-apikey",
                "Platform": "maas",
                "Remark": "for test use",
                "Status": "enable",
                "SubUin": "1234556",
                "Uin": "1234556",
                "UpdateTime": "2026-03-25 19:50:56"
            }
        ],
        "RequestId": "3ec32d91-3e21-40bf-8874-516fa9197d5b",
        "TotalCount": 1
    }
}
```

