**Example 1: DescribeApiKey**



Input: 

```
tccli tokenhub DescribeApiKey --cli-unfold-argument  \
    --Platform maas \
    --ApiKeyId ak-20260609-f294a4aa4e2a7412780914226ad3ffd8
```

Output: 
```
{
    "Response": {
        "ApiKey": "sk-7PNKNHibBH617l8ly8xTzUj5Jej359BOJMjguq2St22CVEtM",
        "ApiKeyId": "ak-20260609-f294a4aa4e2a7412780914226ad3ffd8",
        "AppId": "1300056794",
        "BindType": "all",
        "BindingItems": [],
        "CreateTime": "2026-06-09 20:55:16",
        "Creator": "",
        "Editable": true,
        "IpWhitelist": [],
        "Name": "my-api-key",
        "Platform": "maas",
        "Remark": "",
        "Status": "enable",
        "SubUin": "600000563014",
        "Uin": "600000563014",
        "UpdateTime": "2026-06-09 20:55:16",
        "RequestId": "9a5c9c84-0566-4a8c-9be9-135d834e668c"
    }
}
```

