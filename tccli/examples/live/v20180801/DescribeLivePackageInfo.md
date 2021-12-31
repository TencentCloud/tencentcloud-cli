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
        "RequestId": "eac6b30c-a32x-493c-8e36-83b295459397",
        "PackageBillMode": 201,
        "TotalPage": 0,
        "TotalNum": 0,
        "PageNum": 0,
        "PageSize": 0,
        "FluxPackageBillMode": "xx",
        "LivePackageInfoList": [
            {
                "Id": "17",
                "Total": 10000,
                "Used": 3000,
                "Left": 7000,
                "Status": 1,
                "BuyTime": "2019-12-17 17:36:20",
                "ExpireTime": "2020-12-17 17:36:20",
                "Type": 0
            }
        ]
    }
}
```

