**Example 1: 查询虚拟分组包含的账号信息**

DescribeVirtualAccounts

Input: 

```
tccli ioa DescribeVirtualAccounts --cli-unfold-argument  \
    --VirtualGroupId 554 \
    --DomainInstanceId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AccountGroupId": 2759,
                    "AccountGroups": null,
                    "AccountId": 5495,
                    "ExtraInfo": "{\"email\": \"\", \"phone\": \"\", \"avatar\": \"\", \"status\": 1, \"miniIAM_guid\": \"1468771581428763555\", \"one_id_union_id\": \"1468771581428763555\", \"iam_disable_account\": 0}",
                    "GroupName": "古月",
                    "Id": 969,
                    "Itime": "2026-07-15 16:54:34",
                    "MobileBindNum": 0,
                    "NamePath": "全网账户.古月.古月",
                    "PcBindNum": 0,
                    "Source": 20522,
                    "Status": 1,
                    "UserId": "1468771581428763555",
                    "UserName": "OneID账号72511721",
                    "Utime": "2026-07-15 16:54:34"
                }
            ],
            "Page": {
                "PageCount": 0,
                "PageNum": 0,
                "PageSize": 0,
                "Total": 1
            }
        },
        "RequestId": "0ed05161-a50e-45ce-9d8b-5c9c32c7ff4e"
    }
}
```

