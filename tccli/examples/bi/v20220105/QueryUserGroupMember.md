**Example 1: QueryUserGroupMember**

QueryUserGroupMember

Input: 

```
tccli bi QueryUserGroupMember --cli-unfold-argument  \
    --FilterGroupIds 256 \
    --AllPage True
```

Output: 
```
{
    "Response": {
        "Msg": "默认业务成功",
        "RequestId": "b0f8718f-d45d-47ef-a395-804a82746fff",
        "Extra": "",
        "Data": {
            "List": [
                {
                    "UserName": "kira_sub_user",
                    "UserId": "700000286953",
                    "CreatedBy": null,
                    "CreatedOn": "2022-03-21 16:34:56"
                }
            ],
            "Total": 1,
            "TotalPages": 1
        }
    }
}
```

