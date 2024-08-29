**Example 1: 查询跨库联查空间列表**



Input: 

```
tccli dmc DescribeJoinSpaces --cli-unfold-argument  \
    --Offset 0 \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "JoinSpaceList": [
            {
                "Id": 2,
                "AppId": 1301792469,
                "Uin": "100013717858",
                "SubAccountUin": "100034888414",
                "SpaceId": "space-9z26466s",
                "SpaceName": "默认",
                "DefaultSpace": true,
                "ResourceIds": [
                    "dmc-rloi1wd2",
                    "dmc-qpk4z8my"
                ],
                "CreatedAt": "2024-07-23 15:03:31",
                "UpdatedAt": "2024-07-23 15:03:31"
            }
        ],
        "RequestId": "3526f709-460a-4d9d-b632-53cabbf4df9f"
    }
}
```

