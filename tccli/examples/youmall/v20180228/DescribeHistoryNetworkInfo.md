**Example 1: 拉取指定店铺网络状态历史**



Input: 

```
tccli youmall DescribeHistoryNetworkInfo --cli-unfold-argument  \
    --Time 1536135402 \
    --CompanyId tencent \
    --ShopId 10086 \
    --StartDay 2018-09-04 \
    --EndDay 2018-09-05 \
    --Limit 3 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "RequestId": "08f44066-6850-4a77-b663-166fff95fb7b",
        "InstanceSet": {
            "Count": 48,
            "CompanyId": "tencent",
            "ShopId": 10086,
            "Province": "上海",
            "City": "浦东",
            "ShopName": "优图实验室",
            "Infos": [
                {
                    "Upload": 29.15,
                    "Download": 221.29,
                    "MinRtt": -1,
                    "AvgRtt": -1,
                    "MaxRtt": -1,
                    "MdevRtt": -1,
                    "Loss": 100,
                    "UpdateTime": 1536071030
                },
                {
                    "Upload": 2.47,
                    "Download": 1.22,
                    "MinRtt": -1,
                    "AvgRtt": -1,
                    "MaxRtt": -1,
                    "MdevRtt": -1,
                    "Loss": 100,
                    "UpdateTime": 1536067912
                },
                {
                    "Upload": 74.33,
                    "Download": 230.16,
                    "MinRtt": -1,
                    "AvgRtt": -1,
                    "MaxRtt": -1,
                    "MdevRtt": -1,
                    "Loss": 100,
                    "UpdateTime": 1536066884
                }
            ]
        }
    }
}
```

