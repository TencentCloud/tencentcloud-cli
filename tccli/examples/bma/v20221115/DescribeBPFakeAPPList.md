**Example 1: 查询仿冒应用列表**

查询仿冒应用列表

Input: 

```
tccli bma DescribeBPFakeAPPList --cli-unfold-argument  \
    --Filters.0.Name BrandName \
    --Filters.0.Value 品牌名称 \
    --Filters.1.Name Origin \
    --Filters.1.Value 0 \
    --Filters.2.Name BlockStatus \
    --Filters.2.Value 0 \
    --Filters.3.Name OfflineStatus \
    --Filters.3.Value 0 \
    --Filters.4.Name FakeAPP \
    --Filters.4.Value xxx \
    --Filters.5.Name StartTime \
    --Filters.5.Value 2022-10-01 00:00:00 \
    --Filters.6.Name EndTime \
    --Filters.6.Value 2022-10-01 23:59:59 \
    --PageSize 10 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "FakeAPPList": [
            {
                "FakeAPPId": 123,
                "BrandName": "品牌名称",
                "Origin": 0,
                "FakeAPPName": "仿冒应用名称",
                "FakeAPPPackageName": "仿冒应用包名",
                "FakeAPPCert": "仿冒应用证书",
                "FakeAPPSize": "仿冒应用大小",
                "Heat": 100,
                "BlockStatus": 0,
                "BlockNote": "协助处置状态说明",
                "OfflineStatus": 0,
                "OfflineNote": "下架状态说明",
                "DownloadWay": "app来源",
                "InsertTime": "2022-10-01 00:00:00",
                "DownloadCosURL": "cos下载链接",
                "CertificationStatus": 0
            }
        ],
        "TotalCount": 100,
        "RequestId": "xxx"
    }
}
```

