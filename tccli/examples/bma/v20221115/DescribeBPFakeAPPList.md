**Example 1: 查询仿冒应用列表**

查询仿冒应用列表

Input: 

```
tccli bma DescribeBPFakeAPPList --cli-unfold-argument ```

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
                "DownloadCosURL": "cos下载链接"
            }
        ],
        "TotalCount": 100,
        "RequestId": "xxx"
    }
}
```

