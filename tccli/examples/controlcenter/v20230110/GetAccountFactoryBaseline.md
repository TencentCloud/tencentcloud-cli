**Example 1: 示例**

获取用户基线配置

Input: 

```
tccli controlcenter GetAccountFactoryBaseline --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "OwnerUin": 100000000001,
        "Name": "default",
        "BaselineConfigItems": [
            {
                "Identifier": "ACS-BP_ACCOUNT_FACTORY_ACCOUNT_CONTACT",
                "Configuration": "{\"Contacts\":[{\"Name\":\"dest\",\"Email\":\"ia@22.com\",\"Mobile\":\"12345678910\",\"Position\":\"Technical Director\"}]}",
                "ApplyCount": 5
            }
        ],
        "CreateTime": "2022-08-18 12:00:00",
        "UpdateTime": "2022-08-18 12:00:00",
        "RequestId": "e2f35fb3-3c8c-431e-b318-b4746cfe076c"
    }
}
```

