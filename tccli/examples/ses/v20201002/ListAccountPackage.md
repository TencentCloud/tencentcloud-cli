**Example 1: 获取用户套餐包**



Input: 

```
tccli ses ListAccountPackage --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72",
        "AccountPackages": [
            {
                "UsedQuota": 3000,
                "PackageStatus": 0,
                "PackageQuota": 5000,
                "AvailableQuota": 2000,
                "LastUpdateTime": "2020-09-22 00:00:00",
                "PackageID": "8979fc2958ce679b72"
            },
            {
                "UsedQuota": 2000,
                "PackageStatus": 0,
                "PackageQuota": 6000,
                "AvailableQuota": 4000,
                "LastUpdateTime": "2020-09-22 00:00:00",
                "PackageID": "8979fc1e9564bf7d"
            }
        ]
    }
}
```

