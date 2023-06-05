**Example 1: 获取按项目汇总消耗详情**

获取按项目汇总消耗详情

Input: 

```
tccli billing DescribeCostSummaryByProject --cli-unfold-argument  \
    --NeedRecordNum 1 \
    --EndTime 2018-11 \
    --Limit 1 \
    --BeginTime 2018-11 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Total": {
            "RealTotalCost": "510.15"
        },
        "Data": [
            {
                "ProjectId": "0",
                "ProjectName": "默认项目",
                "RealTotalCost": "318.77",
                "Trend": {
                    "Type": "downward",
                    "Value": "0.92"
                },
                "Business": [
                    {
                        "BusinessCode": "p_ai_image_authentication",
                        "BusinessCodeName": "",
                        "RealTotalCost": "3.00",
                        "Trend": {
                            "Type": "downward",
                            "Value": "0.78"
                        }
                    },
                    {
                        "BusinessCode": "p_blackstone_eip",
                        "BusinessCodeName": "黑石弹性IP",
                        "RealTotalCost": "148.81",
                        "Trend": {
                            "Type": "upward",
                            "Value": "0.03"
                        }
                    },
                    {
                        "BusinessCode": "p_blackstone_lb",
                        "BusinessCodeName": "黑石负载均衡",
                        "RealTotalCost": "31.00",
                        "Trend": {
                            "Type": "upward",
                            "Value": "1.79"
                        }
                    },
                    {
                        "BusinessCode": "p_cas",
                        "BusinessCodeName": "归档存储",
                        "RealTotalCost": "0.02",
                        "Trend": {
                            "Type": "upward",
                            "Value": "0.00"
                        }
                    },
                    {
                        "BusinessCode": "p_cbs",
                        "BusinessCodeName": "云硬盘CBS",
                        "RealTotalCost": "17.03",
                        "Trend": {
                            "Type": "downward",
                            "Value": "0.23"
                        }
                    },
                    {
                        "BusinessCode": "p_cos",
                        "BusinessCodeName": "对象存储COS",
                        "RealTotalCost": "78.34",
                        "Trend": {
                            "Type": "upward",
                            "Value": "0.00"
                        }
                    },
                    {
                        "BusinessCode": "p_cvm",
                        "BusinessCodeName": "云服务器CVM",
                        "RealTotalCost": "34.74",
                        "Trend": {
                            "Type": "downward",
                            "Value": "0.67"
                        }
                    },
                    {
                        "BusinessCode": "p_vod",
                        "BusinessCodeName": "点播VOD",
                        "RealTotalCost": "6.52",
                        "Trend": {
                            "Type": "upward",
                            "Value": "0.03"
                        }
                    }
                ]
            }
        ],
        "RecordNum": 6,
        "Ready": 1,
        "RequestId": "59a408bc-5d95-4d40-bf21-58e5e8d48dd0"
    }
}
```

