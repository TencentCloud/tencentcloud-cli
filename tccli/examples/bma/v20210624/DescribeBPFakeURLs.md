**Example 1: 查询仿冒链接**



Input: 

```
tccli bma DescribeBPFakeURLs --cli-unfold-argument  \
    --PageSize 10 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 10,
        "ExportURL": "xx",
        "FakeURLInfos": [
            {
                "DetectTime": "xx",
                "Status": 1,
                "FakeURLId": 123,
                "FakeURLExpireTime": "xx",
                "FakeURL": "xx",
                "FakeURLCreateTime": "xx",
                "ProtectWeb": "xx",
                "Note": "xx",
                "Heat": 123,
                "Snapshot": "xx",
                "FakeURLCompany": "xx",
                "IP": "xx",
                "FakeURLAttr": "xx",
                "FakeURLICP": "xx",
                "FakeURLName": "xx",
                "IPLoc": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

