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
        "LivePackageInfoList": [
            {
                "Id": "abc",
                "Total": 0,
                "Used": 0,
                "Left": 0,
                "BuyTime": "abc",
                "ExpireTime": "abc",
                "Type": 0,
                "Status": 0,
                "WillRenew": 0,
                "RenewalResult": 0
            }
        ],
        "PackageBillMode": 0,
        "TotalPage": 0,
        "TotalNum": 0,
        "PageNum": 0,
        "PageSize": 0,
        "FluxPackageBillMode": "abc",
        "RequestId": "abc"
    }
}
```

