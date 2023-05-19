**Example 1: 获取组织成员访问身份列表**

获取组织成员访问身份列表

Input: 

```
tccli organization ListOrganizationIdentity --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "IdentityId": 1,
                "IdentityAliasName": "test",
                "Description": "",
                "IdentityPolicy": [
                    {
                        "PolicyId": 1,
                        "PolicyName": "AdministratorAccess"
                    }
                ],
                "IdentityType": 1,
                "UpdateTime": "2021-07-15 21:08:38"
            }
        ],
        "RequestId": "1d744bef-fa56-40e9-8e3b-5a88b122ad5e",
        "Total": 1
    }
}
```

