**Example 1: license列表**

查询用户购买的license列表以及设备绑定情况

Input: 

```
tccli trro GetLicenses --cli-unfold-argument  \
    --PageNum 1 \
    --PageSize 20
```

Output: 
```
{
    "Response": {
        "Licenses": [
            {
                "Status": 0,
                "Duration": "86400",
                "ExpireTime": "1686362610",
                "RemainDay": 82,
                "Count": 2,
                "LicenseIds": [
                    "trro-2e24a74a-67ea-1732-076d-75bf772529a",
                    "trro-2e24a74a-67ea-1732-073d-75bf772579a"
                ]
            },
            {
                "Status": 0,
                "Duration": "186400",
                "ExpireTime": "1689386610",
                "RemainDay": 117,
                "LicenseIds": [
                    "trro-2e24a74a-67ea-1732-076d-75bf772529a",
                    "trro-2e24a74a-67ea-1732-073d-75bf772579a"
                ],
                "Count": 2
            }
        ],
        "TotalCount": 3,
        "RequestId": "xxx"
    }
}
```

