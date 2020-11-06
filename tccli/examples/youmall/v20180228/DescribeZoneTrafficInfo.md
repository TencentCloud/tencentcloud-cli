**Example 1: 获取区域客流人次及停留时间 - 成功示例**



Input: 

```
tccli youmall DescribeZoneTrafficInfo --cli-unfold-argument  \
    --CompanyId testCompany1 \
    --ShopId 1 \
    --StartDate 2016-10-10 \
    --EndDate 2017-06-01 \
    --Offset 0 \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "CompanyId": "testCompany1",
        "TotalCount": 2,
        "ZoneTrafficInfoSet": [
            {
                "Date": "2016-10-10",
                "ZoneTrafficInfoDetailSet": [
                    {
                        "AvgStayTime": 130,
                        "TrafficCount": 122,
                        "ZoneId": 1,
                        "ZoneName": "洗漱用品区"
                    },
                    {
                        "AvgStayTime": 1300,
                        "TrafficCount": 1202,
                        "ZoneId": 2,
                        "ZoneName": "厨房用品区"
                    }
                ]
            },
            {
                "Date": "2016-10-11",
                "ZoneTrafficInfoDetailSet": [
                    {
                        "AvgStayTime": 130,
                        "TrafficCount": 122,
                        "ZoneId": 1,
                        "ZoneName": "洗漱用品区"
                    },
                    {
                        "AvgStayTime": 1300,
                        "TrafficCount": 1202,
                        "ZoneId": 2,
                        "ZoneName": "厨房用品区"
                    }
                ]
            }
        ],
        "RequestId": "6ec80684-0879-405e-8932-72e7c0c48ef8",
        "ShopId": 1
    }
}
```

**Example 2: 获取区域客流人次及停留时间 - 失败示例**



Input: 

```
tccli youmall DescribeZoneTrafficInfo --cli-unfold-argument  \
    --CompanyId testCompany1 \
    --StartDate 2016-10-10 \
    --EndDate 2017-06-01 \
    --Offset 0 \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter",
            "Message": "Parameter ShopId is missing"
        },
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

