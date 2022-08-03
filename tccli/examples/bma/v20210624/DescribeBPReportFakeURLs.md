**Example 1: DescribeBPReportFakeURLs**



Input: 

```
tccli bma DescribeBPReportFakeURLs --cli-unfold-argument  \
    --PageSize 10 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "ReportFakeURLInfos": [
            {
                "DetectTime": "xx",
                "Status": 1,
                "FakeURLId": 123,
                "FakeURLExpireTime": "xx",
                "FakeURL": "xx",
                "FakeURLCreateTime": "xx",
                "Heat": 123,
                "ProtectWeb": "xx",
                "Note": "xx",
                "BlockTime": "xx",
                "ProtectURL": "xx",
                "Snapshot": "xx",
                "FakeURLCompany": "xx",
                "IP": "xx",
                "FakeURLAttr": "xx",
                "FakeURLICP": "xx",
                "FakeURLName": "xx",
                "IPLoc": "xx"
            }
        ],
        "RequestId": "xx",
        "TotalCount": 10
    }
}
```

