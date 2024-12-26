**Example 1: 查询直播套餐包信息**



Input: 

```
tccli live DescribeLivePackageInfo --cli-unfold-argument  \
    --PackageType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "53fc3618-4152-4e12-a1e6-3805e647a602",
        "LivePackageInfoList": [
            {
                "Id": "281975",
                "Type": 0,
                "Status": 1,
                "Total": 500000000000,
                "Used": 2365271265,
                "Left": 497634728735,
                "BuyTime": "2024-07-16 18:46:08",
                "ExpireTime": "2025-07-16 18:46:08",
                "WillRenew": 0,
                "RenewalResult": 0
            },
            {
                "Id": "272177",
                "Type": 0,
                "Status": 4,
                "Total": 500000000000,
                "Used": 500000000000,
                "Left": 0,
                "BuyTime": "2023-12-05 10:17:04",
                "ExpireTime": "2024-12-05 10:17:04",
                "WillRenew": 0,
                "RenewalResult": 0
            },
            {
                "Id": "265480",
                "Type": 0,
                "Status": 4,
                "Total": 100000000000,
                "Used": 100000000000,
                "Left": 0,
                "BuyTime": "2023-07-14 14:14:30",
                "ExpireTime": "2024-07-14 14:14:30",
                "WillRenew": 0,
                "RenewalResult": 0
            },
            {
                "Id": "242917",
                "Type": 0,
                "Status": 4,
                "Total": 1000000000000,
                "Used": 1000000000000,
                "Left": 0,
                "BuyTime": "2022-09-30 10:01:19",
                "ExpireTime": "2023-09-30 10:01:19",
                "WillRenew": 0,
                "RenewalResult": 0
            },
            {
                "Id": "224805",
                "Type": 0,
                "Status": 4,
                "Total": 100000000000,
                "Used": 100000000000,
                "Left": 0,
                "BuyTime": "2022-04-01 10:13:27",
                "ExpireTime": "2023-04-01 10:13:27",
                "WillRenew": 0,
                "RenewalResult": 0
            },
            {
                "Id": "224804",
                "Type": 0,
                "Status": 4,
                "Total": 100000000000,
                "Used": 100000000000,
                "Left": 0,
                "BuyTime": "2022-04-01 10:13:27",
                "ExpireTime": "2023-04-01 10:13:27",
                "WillRenew": 0,
                "RenewalResult": 0
            },
            {
                "Id": "210034",
                "Type": 0,
                "Status": 4,
                "Total": 100000000000,
                "Used": 100000000000,
                "Left": 0,
                "BuyTime": "2021-11-16 16:48:39",
                "ExpireTime": "2022-11-16 16:48:39",
                "WillRenew": 0,
                "RenewalResult": 0
            },
            {
                "Id": "174007",
                "Type": 0,
                "Status": 4,
                "Total": 100000000000,
                "Used": 100000000000,
                "Left": 0,
                "BuyTime": "2021-03-19 16:21:52",
                "ExpireTime": "2022-03-19 16:21:52",
                "WillRenew": 0,
                "RenewalResult": 0
            },
            {
                "Id": "138556",
                "Type": 0,
                "Status": 4,
                "Total": 20000000000,
                "Used": 20000000000,
                "Left": 0,
                "BuyTime": "2020-09-09 12:45:48",
                "ExpireTime": "2021-09-09 12:45:48",
                "WillRenew": 0,
                "RenewalResult": 0
            }
        ],
        "PackageBillMode": 204,
        "FluxPackageBillMode": "204,204,204,204,-1,-1",
        "TotalPage": 1,
        "TotalNum": 9,
        "PageNum": 1,
        "PageSize": 100
    }
}
```

