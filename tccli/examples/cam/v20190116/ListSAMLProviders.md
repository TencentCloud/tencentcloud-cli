**Example 1: 查询身份提供商列表**

查询身份提供商列表

Input: 

```
tccli cam ListSAMLProviders --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 6,
        "SAMLProviderSet": [
            {
                "Name": "saml-sdk",
                "Description": "sdk",
                "CreateTime": "2018-12-17 16:33:35",
                "ModifyTime": "2019-02-26 13:34:58"
            },
            {
                "Name": "TestSAML",
                "Description": "111",
                "CreateTime": "2018-11-08 19:27:27",
                "ModifyTime": "2019-04-30 11:23:12"
            },
            {
                "Name": "OneLogin",
                "Description": "ONeLogin",
                "CreateTime": "2018-11-04 20:36:41",
                "ModifyTime": "2018-11-23 23:56:09"
            },
            {
                "Name": "Azure_AD",
                "Description": "Azure AD",
                "CreateTime": "2018-11-04 16:44:25",
                "ModifyTime": "2019-02-14 10:38:27"
            },
            {
                "Name": "api-test",
                "Description": "API测试",
                "CreateTime": "2018-10-30 11:40:19",
                "ModifyTime": "2018-10-30 11:40:19"
            },
            {
                "Name": "okta",
                "Description": "okta",
                "CreateTime": "2018-09-17 17:18:03",
                "ModifyTime": "2018-09-17 17:18:03"
            }
        ],
        "RequestId": "d644fa50-7e54-4448-84d8-64cb4dd9f737"
    }
}
```

