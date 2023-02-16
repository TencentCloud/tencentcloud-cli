**Example 1: 查询仿冒网址列表**

查询仿冒网址列表

Input: 

```
tccli bma DescribeBPFakeURLs --cli-unfold-argument ```

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
                "CertificationStatus": 0
            }
        ],
        "TotalCount": 100,
        "RequestId": "xxx"
    }
}
```

