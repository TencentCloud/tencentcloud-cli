**Example 1: 输入ApiKeyId查询 API 密钥详情**

输入ApiKeyId查询 API 密钥详情

Input: 

```
tccli tokenhub DescribeApiKey --cli-unfold-argument  \
    --Platform maas \
    --ApiKeyId ak-20260325-xxxxxx
```

Output: 
```
{
    "Response": {
        "ApiKey": "sk-xxxxxx",
        "ApiKeyId": "ak-20260325-xxxxxx",
        "AppId": "111111",
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
        "Remark": "test-new-remark",
        "RequestId": "b56014db-c0e2-4a0f-b2dc-0155684771ac",
        "Status": "disable",
        "SubUin": "112233",
        "Uin": "112233",
        "UpdateTime": "2026-03-25 20:43:53"
    }
}
```

