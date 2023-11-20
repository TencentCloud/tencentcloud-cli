**Example 1: 查询规格的参考价格**

查询规格的参考价格

Input: 

```
tccli sqlserver DescribeSpecSellStatus --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "DescribeSpecSellStatusSet": [
            {
                "Architecture": "SINGLE",
                "Id": "11000036233",
                "InstanceType": "SI",
                "MultiZonesStatus": "Invalid",
                "PayModeStatus": "ALL",
                "Price": {
                    "PostpaidPrice": 47,
                    "PostpaidPriceUnit": "H",
                    "PrepaidPrice": 26000,
                    "PrepaidPriceUnit": "M"
                },
                "SpecId": 62,
                "Status": 1,
                "Style": "EXCLUSIVE",
                "Version": "2016SP1",
                "ZoneStatusSet": [
                    {
                        "Region": "ap-guangzhou",
                        "Status": 1,
                        "Zone": "ap-guangzhou-3"
                    },
                    {
                        "Region": "ap-guangzhou",
                        "Status": 3,
                        "Zone": "ap-guangzhou-4"
                    },
                    {
                        "Region": "ap-guangzhou",
                        "Status": 1,
                        "Zone": "ap-guangzhou-6"
                    },
                    {
                        "Region": "ap-singapore",
                        "Status": 1,
                        "Zone": "ap-singapore-2"
                    },
                    {
                        "Region": "ap-singapore",
                        "Status": 1,
                        "Zone": "ap-singapore-1"
                    },
                    {
                        "Region": "ap-hongkong",
                        "Status": 1,
                        "Zone": "ap-hongkong-2"
                    },
                    {
                        "Region": "ap-shanghai",
                        "Status": 1,
                        "Zone": "ap-shanghai-2"
                    },
                    {
                        "Region": "ap-shanghai",
                        "Status": 1,
                        "Zone": "ap-shanghai-3"
                    },
                    {
                        "Region": "ap-shanghai",
                        "Status": 1,
                        "Zone": "ap-shanghai-4"
                    },
                    {
                        "Region": "ap-shanghai",
                        "Status": 1,
                        "Zone": "ap-shanghai-5"
                    },
                    {
                        "Region": "ap-beijing",
                        "Status": 1,
                        "Zone": "ap-beijing-2"
                    },
                    {
                        "Region": "ap-beijing",
                        "Status": 1,
                        "Zone": "ap-beijing-3"
                    },
                    {
                        "Region": "ap-beijing",
                        "Status": 1,
                        "Zone": "ap-beijing-5"
                    },
                    {
                        "Region": "ap-beijing",
                        "Status": 1,
                        "Zone": "ap-beijing-6"
                    },
                    {
                        "Region": "ap-beijing",
                        "Status": 1,
                        "Zone": "ap-beijing-7"
                    },
                    {
                        "Region": "ap-nanjing",
                        "Status": 1,
                        "Zone": "ap-nanjing-1"
                    },
                    {
                        "Region": "ap-nanjing",
                        "Status": 1,
                        "Zone": "ap-nanjing-2"
                    }
                ]
            }
        ],
        "RequestId": "df9508b2-db7c-43ac-91dc-3ba19433ae09"
    }
}
```

