**Example 1: 查询企业成员信息列表**

查询企业成员信息列表

Input: 

```
tccli wav QueryUserInfoList --cli-unfold-argument  \
    --Cursor +1H24tK0tELjSiTOR10DzA \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "NextCursor": "+1H24tK0tELjSiTOR10DzA==",
        "PageData": [
            {
                "UserId": 0,
                "UserName": "杨过",
                "UserOpenId": "YangGuo",
                "DealerId": 0,
                "ShopId": 0,
                "Phone": "134****1234",
                "OrgIds": "2,3",
                "MainDepartment": "1",
                "IsLeaderInDept": "1,0",
                "Status": 0,
                "JobNumber": "12345678"
            }
        ],
        "RequestId": "4d48312c-a062-4875-a5d5-69f0f11baf96"
    }
}
```

