**Example 1: 获取已设置管理员的互信主体关系列表**

获取已设置管理员的互信主体关系列表

Input: 

```
tccli organization DescribeOrganizationAuthNode --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "RelationId": 1,
                "AuthName": "auth_name",
                "Manager": {
                    "MemberUin": 10000000001,
                    "MemberName": "member_name"
                }
            }
        ],
        "RequestId": "1d744bef-fa56-40e9-8e3b-5a88b122ad5e",
        "Total": 1
    }
}
```

