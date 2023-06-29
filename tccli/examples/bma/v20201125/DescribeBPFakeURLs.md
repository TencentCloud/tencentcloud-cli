**Example 1: 查询仿冒链接列表**



Input: 

```
tccli bma DescribeBPFakeURLs --cli-unfold-argument  \
    --Filters.0.Name Status \
    --Filters.0.Value xxx \
    --Filters.1.Name StartTime \
    --Filters.1.Value 2020-06-01 00:00:00 \
    --Filters.2.Name EndTime \
    --Filters.2.Value 2020-12-01 00:00:00 \
    --PageSize 10 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "FakeURLInfos": [
            {
                "FakeURLId": 123,
                "DetectTime": "xxx",
                "FakeURL": "xxx",
                "IP": "xxx",
                "IPLoc": "xxx",
                "Heat": 123,
                "Status": 1,
                "Note": "xxx",
                "FakeURLCompany": "xxx",
                "FakeURLAttr": "xxx",
                "FakeURLName": "xxx",
                "FakeURLICP": "xxx",
                "FakeURLCreateTime": "xxx",
                "FakeURLExpireTime": "xxx"
            }
        ],
        "TotalCount": 10,
        "RequestId": "xxx",
        "ExportURL": "xxx"
    }
}
```

