**Example 1: 获取组织总览数据**

获取组织总览数据

Input: 

```
tccli organization DescribeOrganizationOverView --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "MemberNum": 2,
        "NodeNum": 7,
        "RoleNum": 10,
        "SubAccountNum": 101,
        "IdentityNum": 5,
        "LoginSubAccountNum": 3,
        "LoginMemberNum": 4,
        "HostAuthName": "test",
        "AuthRelationNum": 2,
        "RequestId": "23047bb6-80a1-459e-8482-8396883e68a7"
    }
}
```

