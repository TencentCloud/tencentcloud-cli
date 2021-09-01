**Example 1: 请求店铺当前网络状态**



Input: 

```
tccli youmall DescribeNetworkInfo --cli-unfold-argument  \
    --Time 1536139452 \
    --CompanyId tencent \
    --ShopId 10086
```

Output: 
```
{
    "Response": {
        "RequestId": "fd2705d2-7444-4522-a9af-46c4b2911b40",
        "InstanceSet": {
            "Count": 1,
            "Infos": [
                {
                    "CompanyId": "tencent",
                    "ShopId": 10086,
                    "Province": "上海",
                    "City": "浦东",
                    "ShopName": "优图实验室",
                    "Upload": 2.29,
                    "Download": 1.01,
                    "MinRtt": -1,
                    "AvgRtt": -1,
                    "MaxRtt": -1,
                    "MdevRtt": -1,
                    "Loss": 100,
                    "UpdateTime": 1536136734
                }
            ]
        }
    }
}
```

