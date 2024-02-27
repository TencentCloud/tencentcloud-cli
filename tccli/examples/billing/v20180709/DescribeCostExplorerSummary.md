**Example 1: 按月查询成本分析接口**



Input: 

```
tccli billing DescribeCostExplorerSummary --cli-unfold-argument  \
    --Dimensions business \
    --PeriodType month \
    --FeeType cost \
    --BillType 1 \
    --BeginTime 2023-12-31 00:00:00 \
    --EndTime 2024-01-07 23:00:00 \
    --PageSize 100 \
    --PageNo 1
```

Output: 
```
{
    "Response": {
        "Total": 21,
        "Header": {
            "Name": "产品",
            "Total": "总计",
            "HeadDetail": [
                {
                    "Name": "2023-12-01 00:00:00"
                },
                {
                    "Name": "2023-12-02 00:00:00"
                }
            ]
        },
        "ConditionValue": {},
        "Detail": [
            {
                "Name": "云服务器CVM",
                "Total": "211.52000096",
                "TimeDetail": [
                    {
                        "Time": "2023-12-01 00:00:00",
                        "Money": "211.52000048"
                    },
                    {
                        "Time": "2023-12-02 00:00:00",
                        "Money": "0.00000048"
                    }
                ]
            },
            {
                "Name": "弹性MapReduce",
                "Total": "169.55291616",
                "TimeDetail": [
                    {
                        "Time": "2023-12-01 00:00:00",
                        "Money": "84.77645808"
                    },
                    {
                        "Time": "2023-12-02 00:00:00",
                        "Money": "84.77645808"
                    }
                ]
            },
            {
                "Name": "T-Sec-主机安全（CWP）",
                "Total": "104.40081600",
                "TimeDetail": [
                    {
                        "Time": "2023-12-01 00:00:00",
                        "Money": "52.20040800"
                    },
                    {
                        "Time": "2023-12-02 00:00:00",
                        "Money": "52.20040800"
                    }
                ]
            },
            {
                "Name": "计费测试商品",
                "Total": "100.00000000",
                "TimeDetail": [
                    {
                        "Time": "2023-12-01 00:00:00",
                        "Money": "100.00000000"
                    },
                    {
                        "Time": "2023-12-02 00:00:00",
                        "Money": "0"
                    }
                ]
            },
            {
                "Name": "云数据库MySQL",
                "Total": "38.77000000",
                "TimeDetail": [
                    {
                        "Time": "2023-12-01 00:00:00",
                        "Money": "0.00000000"
                    },
                    {
                        "Time": "2023-12-02 00:00:00",
                        "Money": "38.77000000"
                    }
                ]
            },
            {
                "Name": "人脸识别",
                "Total": "36.00000000",
                "TimeDetail": [
                    {
                        "Time": "2023-12-01 00:00:00",
                        "Money": "0"
                    },
                    {
                        "Time": "2023-12-02 00:00:00",
                        "Money": "36.00000000"
                    }
                ]
            },
            {
                "Name": "容器服务 TKE",
                "Total": "19.00184160",
                "TimeDetail": [
                    {
                        "Time": "2023-12-01 00:00:00",
                        "Money": "9.50092080"
                    },
                    {
                        "Time": "2023-12-02 00:00:00",
                        "Money": "9.50092080"
                    }
                ]
            },
            {
                "Name": "NAT网关",
                "Total": "16.28275200",
                "TimeDetail": [
                    {
                        "Time": "2023-12-01 00:00:00",
                        "Money": "8.14137600"
                    },
                    {
                        "Time": "2023-12-02 00:00:00",
                        "Money": "8.14137600"
                    }
                ]
            },
            {
                "Name": "黑石弹性公网IP",
                "Total": "9.60076800",
                "TimeDetail": [
                    {
                        "Time": "2023-12-01 00:00:00",
                        "Money": "4.80038400"
                    },
                    {
                        "Time": "2023-12-02 00:00:00",
                        "Money": "4.80038400"
                    }
                ]
            },
            {
                "Name": "节省计划",
                "Total": "7.20000000",
                "TimeDetail": [
                    {
                        "Time": "2023-12-01 00:00:00",
                        "Money": "3.60000000"
                    },
                    {
                        "Time": "2023-12-02 00:00:00",
                        "Money": "3.60000000"
                    }
                ]
            }
        ],
        "TotalDetail": {
            "Name": "总计",
            "Total": "724.5825514",
            "TimeDetail": [
                {
                    "Time": "2023-12-01 00:00:00",
                    "Money": "480.64255140"
                },
                {
                    "Time": "2023-12-02 00:00:00",
                    "Money": "243.94000000"
                }
            ]
        },
        "RequestId": "18619d53-8b77-45f2-a685-ac4490e74c06"
    }
}
```

