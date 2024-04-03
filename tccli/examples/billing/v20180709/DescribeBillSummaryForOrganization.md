**Example 1: 获取按地域汇总费用明细**

获取按地域汇总费用明细

Input: 

```
tccli billing DescribeBillSummaryForOrganization --cli-unfold-argument  \
    --Month 2023-04 \
    --GroupType region
```

Output: 
```
{
    "Response": {
        "Ready": 1,
        "RequestId": "a93087e2-c03a-4058-b09b-0ecc8dd493cb",
        "SummaryDetail": [
            {
                "Business": [
                    {
                        "BusinessCode": "p_rav",
                        "BusinessCodeName": "实时音视频",
                        "CashPayAmount": "5661.16",
                        "IncentivePayAmount": "0.00",
                        "RealTotalCost": "5661.16",
                        "TotalCost": "24600.63",
                        "TransferPayAmount": "0.00",
                        "VoucherPayAmount": "0.00"
                    },
                    {
                        "BusinessCode": "p_cdh",
                        "BusinessCodeName": "专用宿主机CDH",
                        "CashPayAmount": "4254.21",
                        "IncentivePayAmount": "0.00",
                        "RealTotalCost": "4254.21",
                        "TotalCost": "10920.00",
                        "TransferPayAmount": "0.00",
                        "VoucherPayAmount": "0.00"
                    }
                ],
                "CashPayAmount": "9915.37",
                "GroupKey": "1",
                "GroupValue": "华南地区（广州）",
                "IncentivePayAmount": "0.00",
                "RealTotalCost": "9915.37",
                "TotalCost": "35520.63",
                "TransferPayAmount": "0.00",
                "VoucherPayAmount": "0.00"
            },
            {
                "Business": [
                    {
                        "BusinessCode": "p_cvm",
                        "BusinessCodeName": "云服务器CVM",
                        "CashPayAmount": "3231.21",
                        "IncentivePayAmount": "0.00",
                        "RealTotalCost": "3359.21",
                        "TotalCost": "9809.48",
                        "TransferPayAmount": "0.00",
                        "VoucherPayAmount": "128.00"
                    }
                ],
                "CashPayAmount": "3231.21",
                "GroupKey": "25",
                "GroupValue": "亚太地区（日本）",
                "IncentivePayAmount": "0.00",
                "RealTotalCost": "3359.21",
                "TotalCost": "9809.48",
                "TransferPayAmount": "0.00",
                "VoucherPayAmount": "128.00"
            },
            {
                "Business": [
                    {
                        "BusinessCode": "p_dcdb",
                        "BusinessCodeName": "分布式数据库TDSQL MySQL版",
                        "CashPayAmount": "2094.29",
                        "IncentivePayAmount": "0.00",
                        "RealTotalCost": "2094.29",
                        "TotalCost": "4915.20",
                        "TransferPayAmount": "0.00",
                        "VoucherPayAmount": "0.00"
                    }
                ],
                "CashPayAmount": "2094.29",
                "GroupKey": "11",
                "GroupValue": "华南地区（深圳金融）",
                "IncentivePayAmount": "0.00",
                "RealTotalCost": "2094.29",
                "TotalCost": "4915.20",
                "TransferPayAmount": "0.00",
                "VoucherPayAmount": "0.00"
            }
        ]
    }
}
```

**Example 2: 获取按项目汇总费用明细**

获取按项目汇总费用明细

Input: 

```
tccli billing DescribeBillSummaryForOrganization --cli-unfold-argument  \
    --Month 2023-04 \
    --GroupType project
```

Output: 
```
{
    "Response": {
        "Ready": 1,
        "RequestId": "8e0a185f-a64c-4dca-ba23-ba8778d5ef6f",
        "SummaryDetail": [
            {
                "Business": [
                    {
                        "BusinessCode": "p_rav",
                        "BusinessCodeName": "实时音视频",
                        "CashPayAmount": "5661.16",
                        "IncentivePayAmount": "0.00",
                        "RealTotalCost": "5661.16",
                        "TotalCost": "24600.63",
                        "TransferPayAmount": "0.00",
                        "VoucherPayAmount": "0.00"
                    },
                    {
                        "BusinessCode": "p_cdh",
                        "BusinessCodeName": "专用宿主机CDH",
                        "CashPayAmount": "4254.20",
                        "IncentivePayAmount": "0.00",
                        "RealTotalCost": "4254.20",
                        "TotalCost": "10919.99",
                        "TransferPayAmount": "0.00",
                        "VoucherPayAmount": "0.00"
                    }
                ],
                "CashPayAmount": "9915.36",
                "GroupKey": "0",
                "GroupValue": "默认项目",
                "IncentivePayAmount": "0.00",
                "RealTotalCost": "9915.36",
                "TotalCost": "35520.62",
                "TransferPayAmount": "0.00",
                "VoucherPayAmount": "0.00"
            },
            {
                "Business": [
                    {
                        "BusinessCode": "p_cvm",
                        "BusinessCodeName": "云服务器CVM",
                        "CashPayAmount": "689.87",
                        "IncentivePayAmount": "0.00",
                        "RealTotalCost": "847.87",
                        "TotalCost": "1667.57",
                        "TransferPayAmount": "0.00",
                        "VoucherPayAmount": "158.00"
                    },
                    {
                        "BusinessCode": "p_eip",
                        "BusinessCodeName": "公网 IP",
                        "CashPayAmount": "9.69",
                        "IncentivePayAmount": "0.01",
                        "RealTotalCost": "9.71",
                        "TotalCost": "263.25",
                        "TransferPayAmount": "0.00",
                        "VoucherPayAmount": "0.00"
                    },
                    {
                        "BusinessCode": "p_cbs",
                        "BusinessCodeName": "云硬盘CBS",
                        "CashPayAmount": "3.15",
                        "IncentivePayAmount": "0.00",
                        "RealTotalCost": "3.15",
                        "TotalCost": "6.83",
                        "TransferPayAmount": "0.00",
                        "VoucherPayAmount": "0.00"
                    }
                ],
                "CashPayAmount": "702.71",
                "GroupKey": "1279809",
                "GroupValue": "PC端游戏",
                "IncentivePayAmount": "0.01",
                "RealTotalCost": "860.72",
                "TotalCost": "1937.65",
                "TransferPayAmount": "0.00",
                "VoucherPayAmount": "158.00"
            }
        ]
    }
}
```

**Example 3: 获取按产品维度汇总费用明细**

获取按产品维度汇总费用明细

Input: 

```
tccli billing DescribeBillSummaryForOrganization --cli-unfold-argument  \
    --Month 2023-04 \
    --GroupType business
```

Output: 
```
{
    "Response": {
        "Ready": 1,
        "RequestId": "db6f4a8c-c8b3-4d86-836a-b0897e772b22",
        "SummaryDetail": [
            {
                "Business": null,
                "CashPayAmount": "5661.16",
                "GroupKey": "p_rav",
                "GroupValue": "实时音视频",
                "IncentivePayAmount": "0.00",
                "RealTotalCost": "5661.16",
                "TotalCost": "24600.63",
                "TransferPayAmount": "0.00",
                "VoucherPayAmount": "0.00"
            },
            {
                "Business": null,
                "CashPayAmount": "4783.65",
                "GroupKey": "p_cvm",
                "GroupValue": "云服务器CVM",
                "IncentivePayAmount": "0.00",
                "RealTotalCost": "5069.65",
                "TotalCost": "13178.28",
                "TransferPayAmount": "0.00",
                "VoucherPayAmount": "286.00"
            }
        ]
    }
}
```

**Example 4: 获取按标签维度汇总费用明细**

获取按标签维度汇总费用明细

Input: 

```
tccli billing DescribeBillSummaryForOrganization --cli-unfold-argument  \
    --Month 2023-05 \
    --GroupType tag \
    --TagKey 测试键 部门分类
```

Output: 
```
{
    "Response": {
        "Ready": 1,
        "RequestId": "fdb44563-4a70-4c41-88a4-68b628a221a8",
        "SummaryDetail": [
            {
                "Business": [
                    {
                        "BusinessCode": "p_tencentmeeting_saas",
                        "BusinessCodeName": "腾讯会议（SAAS版）",
                        "CashPayAmount": "3284.27",
                        "IncentivePayAmount": "0.00",
                        "RealTotalCost": "3284.27",
                        "TotalCost": "7308.00",
                        "TransferPayAmount": "0.00",
                        "VoucherPayAmount": "0.00"
                    },
                    {
                        "BusinessCode": "p_cbs",
                        "BusinessCodeName": "云硬盘CBS",
                        "CashPayAmount": "2583.11",
                        "IncentivePayAmount": "0.00",
                        "RealTotalCost": "2583.43",
                        "TotalCost": "6383.01",
                        "TransferPayAmount": "0.00",
                        "VoucherPayAmount": "0.32"
                    }
                ],
                "CashPayAmount": "5867.38",
                "GroupKey": "测试键",
                "GroupValue": "",
                "IncentivePayAmount": "0.00",
                "RealTotalCost": "5867.70",
                "TotalCost": "13691.01",
                "TransferPayAmount": "0.00",
                "VoucherPayAmount": "0.32"
            },
            {
                "Business": [
                    {
                        "BusinessCode": "p_nat",
                        "BusinessCodeName": "NAT网关",
                        "CashPayAmount": "127.44",
                        "IncentivePayAmount": "0.00",
                        "RealTotalCost": "127.44",
                        "TotalCost": "188.93",
                        "TransferPayAmount": "0.00",
                        "VoucherPayAmount": "0.00"
                    },
                    {
                        "BusinessCode": "p_cls",
                        "BusinessCodeName": "日志服务CLS",
                        "CashPayAmount": "0.71",
                        "IncentivePayAmount": "0.00",
                        "RealTotalCost": "0.71",
                        "TotalCost": "1.08",
                        "TransferPayAmount": "0.00",
                        "VoucherPayAmount": "0.00"
                    }
                ],
                "CashPayAmount": "128.15",
                "GroupKey": "测试键",
                "GroupValue": "123456",
                "IncentivePayAmount": "0.00",
                "RealTotalCost": "128.15",
                "TotalCost": "190.01",
                "TransferPayAmount": "0.00",
                "VoucherPayAmount": "0.00"
            },
            {
                "Business": [
                    {
                        "BusinessCode": "p_tencentmeeting_saas",
                        "BusinessCodeName": "腾讯会议（SAAS版）",
                        "CashPayAmount": "3284.27",
                        "IncentivePayAmount": "0.00",
                        "RealTotalCost": "3284.27",
                        "TotalCost": "7308.00",
                        "TransferPayAmount": "0.00",
                        "VoucherPayAmount": "0.00"
                    },
                    {
                        "BusinessCode": "p_cbs",
                        "BusinessCodeName": "云硬盘CBS",
                        "CashPayAmount": "2583.11",
                        "IncentivePayAmount": "0.00",
                        "RealTotalCost": "2583.43",
                        "TotalCost": "6383.01",
                        "TransferPayAmount": "0.00",
                        "VoucherPayAmount": "0.32"
                    }
                ],
                "CashPayAmount": "5867.38",
                "GroupKey": "部门分类",
                "GroupValue": "",
                "IncentivePayAmount": "0.00",
                "RealTotalCost": "5867.70",
                "TotalCost": "13691.01",
                "TransferPayAmount": "0.00",
                "VoucherPayAmount": "0.32"
            },
            {
                "Business": [
                    {
                        "BusinessCode": "p_ckafka",
                        "BusinessCodeName": "消息服务CKafka",
                        "CashPayAmount": "1076.00",
                        "IncentivePayAmount": "0.00",
                        "RealTotalCost": "1076.00",
                        "TotalCost": "1076.00",
                        "TransferPayAmount": "0.00",
                        "VoucherPayAmount": "0.00"
                    }
                ],
                "CashPayAmount": "1076.00",
                "GroupKey": "部门分类",
                "GroupValue": "采购部",
                "IncentivePayAmount": "0.00",
                "RealTotalCost": "1076.00",
                "TotalCost": "1076.00",
                "TransferPayAmount": "0.00",
                "VoucherPayAmount": "0.00"
            },
            {
                "Business": [
                    {
                        "BusinessCode": "p_yunjing",
                        "BusinessCodeName": "T-Sec-主机安全（CWP）",
                        "CashPayAmount": "123.18",
                        "IncentivePayAmount": "0.00",
                        "RealTotalCost": "123.18",
                        "TotalCost": "180.00",
                        "TransferPayAmount": "0.00",
                        "VoucherPayAmount": "0.00"
                    }
                ],
                "CashPayAmount": "123.18",
                "GroupKey": "部门分类",
                "GroupValue": "行政部",
                "IncentivePayAmount": "0.00",
                "RealTotalCost": "123.18",
                "TotalCost": "180.00",
                "TransferPayAmount": "0.00",
                "VoucherPayAmount": "0.00"
            },
            {
                "Business": [
                    {
                        "BusinessCode": "p_clb",
                        "BusinessCodeName": "负载均衡CLB",
                        "CashPayAmount": "38.31",
                        "IncentivePayAmount": "0.00",
                        "RealTotalCost": "38.31",
                        "TotalCost": "112.20",
                        "TransferPayAmount": "0.00",
                        "VoucherPayAmount": "0.00"
                    },
                    {
                        "BusinessCode": "p_cos",
                        "BusinessCodeName": "COS 对象存储",
                        "CashPayAmount": "0.00",
                        "IncentivePayAmount": "0.00",
                        "RealTotalCost": "0.00",
                        "TotalCost": "0.00",
                        "TransferPayAmount": "0.00",
                        "VoucherPayAmount": "0.00"
                    }
                ],
                "CashPayAmount": "38.31",
                "GroupKey": "部门分类",
                "GroupValue": "业务部",
                "IncentivePayAmount": "0.00",
                "RealTotalCost": "38.31",
                "TotalCost": "112.20",
                "TransferPayAmount": "0.00",
                "VoucherPayAmount": "0.00"
            },
            {
                "Business": [
                    {
                        "BusinessCode": "p_cvm",
                        "BusinessCodeName": "云服务器CVM",
                        "CashPayAmount": "-43.67",
                        "IncentivePayAmount": "0.00",
                        "RealTotalCost": "-43.67",
                        "TotalCost": "-43.67",
                        "TransferPayAmount": "0.00",
                        "VoucherPayAmount": "0.00"
                    }
                ],
                "CashPayAmount": "-43.67",
                "GroupKey": "部门分类",
                "GroupValue": "财务部",
                "IncentivePayAmount": "0.00",
                "RealTotalCost": "-43.67",
                "TotalCost": "-43.67",
                "TransferPayAmount": "0.00",
                "VoucherPayAmount": "0.00"
            }
        ]
    }
}
```

**Example 5: 获取按计费模式汇总费用明细**

获取按计费模式汇总费用明细

Input: 

```
tccli billing DescribeBillSummaryForOrganization --cli-unfold-argument  \
    --Month 2023-04 \
    --GroupType payMode
```

Output: 
```
{
    "Response": {
        "Ready": 1,
        "RequestId": "9ddf63cd-89ce-4a0e-9332-7402926fe1a1",
        "SummaryDetail": [
            {
                "Business": [
                    {
                        "BusinessCode": "p_rav",
                        "BusinessCodeName": "实时音视频",
                        "CashPayAmount": "5661.16",
                        "IncentivePayAmount": "0.00",
                        "RealTotalCost": "5661.16",
                        "TotalCost": "24600.63",
                        "TransferPayAmount": "0.00",
                        "VoucherPayAmount": "0.00"
                    },
                    {
                        "BusinessCode": "p_cvm",
                        "BusinessCodeName": "云服务器CVM",
                        "CashPayAmount": "4780.18",
                        "IncentivePayAmount": "0.00",
                        "RealTotalCost": "5066.18",
                        "TotalCost": "13111.78",
                        "TransferPayAmount": "0.00",
                        "VoucherPayAmount": "286.00"
                    }
                ],
                "CashPayAmount": "10441.34",
                "GroupKey": "prePay",
                "GroupValue": "包年包月",
                "IncentivePayAmount": "0.00",
                "RealTotalCost": "10727.34",
                "TotalCost": "37712.41",
                "TransferPayAmount": "0.00",
                "VoucherPayAmount": "286.00"
            },
            {
                "Business": [
                    {
                        "BusinessCode": "p_edgeone",
                        "BusinessCodeName": "边缘安全加速平台",
                        "CashPayAmount": "1205.63",
                        "IncentivePayAmount": "0.00",
                        "RealTotalCost": "1205.63",
                        "TotalCost": "2706.77",
                        "TransferPayAmount": "0.00",
                        "VoucherPayAmount": "0.00"
                    },
                    {
                        "BusinessCode": "p_nat",
                        "BusinessCodeName": "NAT网关",
                        "CashPayAmount": "1145.13",
                        "IncentivePayAmount": "1.72",
                        "RealTotalCost": "1146.85",
                        "TotalCost": "1700.27",
                        "TransferPayAmount": "0.00",
                        "VoucherPayAmount": "0.00"
                    }
                ],
                "CashPayAmount": "2350.76",
                "GroupKey": "postPay",
                "GroupValue": "按量计费",
                "IncentivePayAmount": "1.72",
                "RealTotalCost": "2352.48",
                "TotalCost": "4407.04",
                "TransferPayAmount": "0.00",
                "VoucherPayAmount": "0.00"
            }
        ]
    }
}
```

