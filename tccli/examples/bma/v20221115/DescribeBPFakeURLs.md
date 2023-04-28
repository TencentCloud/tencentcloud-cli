**Example 1: 查询仿冒网址列表**

查询仿冒网址列表

Input: 

```
tccli bma DescribeBPFakeURLs --cli-unfold-argument  \
    --Filters.0.Name BrandName \
    --Filters.0.Value 品牌名称 \
    --Filters.1.Name Origin \
    --Filters.1.Value 0 \
    --Filters.2.Name BlockStatus \
    --Filters.2.Value 0 \
    --Filters.3.Name OfflineStatus \
    --Filters.3.Value 0 \
    --Filters.4.Name FakeURL \
    --Filters.4.Value 仿冒网址 \
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
        "FakeURLs": [
            {
                "FakeURLId": 123,
                "BrandName": "品牌名称",
                "Origin": 0,
                "FakeURL": "仿冒网址",
                "FakeDomain": "仿冒域名",
                "Snapshot": "网址截图",
                "Heat": 100,
                "BlockStatus": 0,
                "BlockNote": "协助处置状态说明",
                "OfflineStatus": 0,
                "OfflineNote": "关停状态说明",
                "IP": "ip地址",
                "IPLocation": "ip地理位置",
                "WebCompany": "网站所属单位",
                "WebAttribute": "网站性质",
                "WebName": "网站名称",
                "WebICP": "备案号",
                "WebCreateTime": "2022-10-01 00:00:00",
                "WebExpireTime": "2022-10-01 00:00:00",
                "InsertTime": "2022-10-01 00:00:00",
                "CertificationStatus": 0,
                "AccountStatus": 0
            }
        ],
        "TotalCount": 100,
        "RequestId": "请求id"
    }
}
```

