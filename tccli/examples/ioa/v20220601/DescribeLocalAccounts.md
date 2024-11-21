**Example 1: 根据账号模糊查询**

查询指定分组下，账号名包含“san47”的账号信息

Input: 

```
tccli ioa DescribeLocalAccounts --cli-unfold-argument  \
    --Condition.Filters.0.Field UserId \
    --Condition.Filters.0.Operator like \
    --Condition.Filters.0.Values san47 \
    --AccountGroupId 8205 \
    --ShowFlag 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AccountGroups": [],
                    "AccountId": 845,
                    "ActiveStatus": 0,
                    "ExtraInfo": "{\"salt\": \"5b52ea107e85a7b46d2c1b15a5faf722\", \"seat\": \"\", \"email\": \"\", \"phone\": \"\", \"is_new\": 0, \"id_card\": \"\", \"user_id\": \"zhangsan471\", \"password\": \"82a4c5b9e0e8bc57208e27ca08d090739ca02725b3bc9a282a8a95925e484cd6\", \"position\": \"测试248\", \"user_name\": \"zhangsan\", \"online_num\": 0, \"valid_time\": \"2030-10-10 00:00:00\", \"gesture_pwd\": \"\", \"is_modified\": 0, \"miniIAM_guid\": \"\", \"is_online_num\": 0, \"is_valid_time\": 1, \"valid_time_int\": 1917792000, \"iam_disable_account\": 0, \"ioa_disable_account\": 0}",
                    "GroupId": 8205,
                    "GroupName": "研发部",
                    "Id": 845,
                    "Itime": "2024-08-02 14:46:11",
                    "LoginTime": "2024-08-03 15:06:09",
                    "LogoutTime": "2024-08-03 18:01:09",
                    "MobileBindNum": 0,
                    "NamePath": "全网账户.自建目录.研发部",
                    "OnlineStatus": 0,
                    "PcBindNum": 0,
                    "RiskLevel": "low",
                    "Source": 0,
                    "Status": 1,
                    "UserId": "zhangsan471",
                    "UserName": "zhangsan",
                    "Utime": "2024-08-03 15:08:21"
                },
                {
                    "AccountGroups": [],
                    "AccountId": 844,
                    "ActiveStatus": 0,
                    "ExtraInfo": "{\"salt\": \"2d6cfa9479b615ce807305f727f55757\", \"seat\": \"\", \"email\": \"\", \"phone\": \"\", \"is_new\": 0, \"id_card\": \"\", \"user_id\": \"zhangsan470\", \"password\": \"608f9eac835f474f8e8eb43d3e4f9fbe675f467f25765655aa42926258a7c963\", \"position\": \"测试247\", \"user_name\": \"zhangsan\", \"online_num\": 0, \"valid_time\": \"2030-10-10\", \"gesture_pwd\": \"\", \"is_modified\": 0, \"miniIAM_guid\": \"\", \"is_online_num\": 0, \"is_valid_time\": 1, \"valid_time_int\": 1917792000, \"iam_disable_account\": 0, \"ioa_disable_account\": 0}",
                    "GroupId": 8205,
                    "GroupName": "研发部",
                    "Id": 844,
                    "Itime": "2024-08-02 14:46:11",
                    "LoginTime": "2024-09-03 06:56:09",
                    "LogoutTime": "2024-09-03 15:06:07",
                    "MobileBindNum": 0,
                    "NamePath": "全网账户.自建目录.研发部",
                    "OnlineStatus": 0,
                    "PcBindNum": 0,
                    "RiskLevel": "low",
                    "Source": 0,
                    "Status": 1,
                    "UserId": "zhangsan470",
                    "UserName": "zhangsan",
                    "Utime": "2024-08-02 14:46:11"
                }
            ],
            "Page": {
                "PageCount": 1,
                "PageNum": 1,
                "PageSize": 10,
                "Total": 2
            }
        },
        "RequestId": "ed2c6d00-8880-4a2a-8d6d-e89587dc5a21"
    }
}
```

