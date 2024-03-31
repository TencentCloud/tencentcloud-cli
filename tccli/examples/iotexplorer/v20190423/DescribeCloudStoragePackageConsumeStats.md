**Example 1: 获取云存套餐包消耗详统计**



Input: 

```
tccli iotexplorer DescribeCloudStoragePackageConsumeStats --cli-unfold-argument  \
    --StartDate 2020-10-11 \
    --EndDate 2021-03-06
```

Output: 
```
{
    "Response": {
        "RequestId": "a9545416-7eac-4e2e-a4a0-9735b0ee7682",
        "Stats": [
            {
                "PackageId": "",
                "PackageName": "全时3天月卡",
                "Cnt": 3,
                "Source": 1,
                "Price": 600
            },
            {
                "PackageId": "",
                "PackageName": "全时3天月卡",
                "Cnt": 1,
                "Source": 1,
                "Price": 595
            },
            {
                "PackageId": "",
                "PackageName": "全时7天月卡",
                "Cnt": 2,
                "Source": 1,
                "Price": 1000
            }
        ]
    }
}
```

