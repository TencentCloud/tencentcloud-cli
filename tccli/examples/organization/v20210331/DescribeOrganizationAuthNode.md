**Example 1: 获取可创建组织成员的认证主体关系列表**



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
                "AuthName": "腾讯云"
            }
        ],
        "RequestId": "1d744bef-fa56-40e9-8e3b-5a88b122ad5e",
        "Total": 1
    }
}
```

