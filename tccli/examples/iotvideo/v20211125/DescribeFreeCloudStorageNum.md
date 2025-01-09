**Example 1: 查询云存卡套餐信息**



Input: 

```
tccli iotvideo DescribeFreeCloudStorageNum --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "PackageInfos": [
            {
                "Num": 10,
                "PackageId": "lye1w3d",
                "PackageName": "低功耗3天会看周套餐",
                "UsedNum": 5
            },
            {
                "Num": 10,
                "PackageId": "lye1w3d",
                "PackageName": "低功耗3天会看两周套餐",
                "UsedNum": 3
            }
        ],
        "RequestId": "c2cc1650-17bb-4996-a88a-8f8471c7d6d5"
    }
}
```

