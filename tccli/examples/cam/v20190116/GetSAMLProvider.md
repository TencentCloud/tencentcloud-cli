**Example 1: 查询身份提供商详情**

查询身份提供商详情

Input: 

```
tccli cam GetSAMLProvider --cli-unfold-argument  \
    --Name okta
```

Output: 
```
{
    "Response": {
        "Name": "okta",
        "Description": "okta",
        "CreateTime": "2018-09-17 17:18:03",
        "ModifyTime": "2018-09-17 17:18:03",
        "SAMLMetadata": "U0FNTE1ldGFkYXRh",
        "RequestId": "fea0ebe5-3062-4b5a-b95e-8cce5a3b0512"
    }
}
```

