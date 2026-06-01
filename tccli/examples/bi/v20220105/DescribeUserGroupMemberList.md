**Example 1: DescribeUserGroupMemberList**

DescribeUserGroupMemberList

Input: 

```
tccli bi DescribeUserGroupMemberList --cli-unfold-argument  \
    --PageNo 0 \
    --PageSize 10 \
    --GroupIds 256
```

Output: 
```
{
    "Response": {
        "Msg": "默认业务成功",
        "RequestId": "e56bb79b-f4ea-4ba3-92a7-431d23e6371c",
        "Extra": "",
        "Data": {
            "List": [
                {
                    "UserName": "99999",
                    "UserId": "700000401505",
                    "CreatedBy": "700000280185",
                    "CreatedOn": "2025-06-18 16:12:14"
                }
            ],
            "Total": 1,
            "TotalPages": 1
        }
    }
}
```

