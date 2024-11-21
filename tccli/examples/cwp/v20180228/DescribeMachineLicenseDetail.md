**Example 1: 示例**



Input: 

```
tccli cwp DescribeMachineLicenseDetail --cli-unfold-argument  \
    --Quuids 15c76928-e4e1-4f0d-8a2a-46c7de78****
```

Output: 
```
{
    "Response": {
        "MachineLicense": [
            {
                "Quuid": "e5b4724c-49af-46ab-bd84-cdbae897e7e0",
                "PayMode": 1,
                "ResourceId": "testid",
                "LicenseType": 0,
                "SourceType": 1,
                "InquireKey": "yunjing-vip",
                "AutoRenewFlag": 1,
                "Deadline": "2022-01-01 00:00:00",
                "BuyTime": "2022-01-01 00:00:00",
                "LicenseCnt": 1
            }
        ],
        "RequestId": "12e44a0c-9da1-4600-9196-6e27308aeef6",
        "TotalCount": 0
    }
}
```

