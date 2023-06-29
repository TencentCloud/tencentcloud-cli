**Example 1: DescribeBPReportFakeURLs**



Input: 

```
tccli bma DescribeBPReportFakeURLs --cli-unfold-argument  \
    --Filters.0.Name URL \
    --Filters.0.Value xxx \
    --Filters.1.Name Status \
    --Filters.1.Value 1 \
    --Filters.2.Name StartTime \
    --Filters.2.Value 2020-06-01 00:00:00 \
    --Filters.3.Name EndTime \
    --Filters.3.Value 2020-12-01 00:00:00 \
    --PageSize 10 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "ReportFakeURLInfos": [
            {
                "FakeURLId": 123,
                "DetectTime": "xxx",
                "ProtectURL": "xxx",
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
        "RequestId": "xxx"
    }
}
```

