**Example 1: 批量查询子账号Linux用户信息**

批量查询子账号Linux用户信息

Input: 

```
tccli tione DescribeSubAccountLinuxUserInfos --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --Filters.0.Name SubUinName \
    --Filters.0.Values willyao \
    --Filters.0.Fuzzy True
```

Output: 
```
{
    "Response": {
        "SubAccountList": [
            {
                "EnableRootLogin": true,
                "LinuxGid": 20000,
                "LinuxUid": 20002,
                "LinuxUserName": "willyao",
                "SubUin": "100009152467",
                "SubUinName": "willyao",
                "Uin": "100031385875",
                "UpdateTime": "2026-03-26T16:52:34+08:00"
            }
        ],
        "TotalCount": 2,
        "RequestId": "99dcb853-bc96-432e-b0b4-d155688746a2"
    }
}
```

