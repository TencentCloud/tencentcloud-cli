**Example 1: 1**

1

Input: 

```
tccli ioa DescribeAggrSoftCategorySoftList --cli-unfold-argument  \
    --OsType 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Page": {
                "PageSize": 1,
                "PageNum": 1,
                "PageCount": 1,
                "Total": 1
            },
            "Total": 0,
            "AggrSoftCategorySoftList": [
                {
                    "ID": 0,
                    "Name": "11",
                    "PiracyRisk": 0,
                    "OsType": 0,
                    "CorpName": "11",
                    "InstalledDeviceNum": 0,
                    "PiracyInstalledDeviceNum": 0,
                    "InstalledUserNum": 0,
                    "PiracyInstalledUserNum": 0,
                    "AuthNum": 0,
                    "GenuineRate": 0
                }
            ]
        },
        "RequestId": "11"
    }
}
```

