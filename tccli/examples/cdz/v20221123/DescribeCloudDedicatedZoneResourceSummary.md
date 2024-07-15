**Example 1: 查询专属可用区资源水位**



Input: 

```
tccli cdz DescribeCloudDedicatedZoneResourceSummary --cli-unfold-argument  \
    --CdzId cdz-mgk971xw
```

Output: 
```
{
    "Response": {
        "ResourceSummarySet": [
            {
                "ProductName": "云服务器",
                "SubProductName": "标准型S5",
                "Statistics": [
                    {
                        "Item": "CPU",
                        "Unit": "核",
                        "Total": "41996",
                        "Usage": "32875",
                        "UsageRate": "78.28%",
                        "Remain": "9121",
                        "RemainRate": "21.72%",
                        "ThisMondayUsageRate": "78.33%",
                        "ThisMondayUsageGrowthRate": "-0.05%",
                        "LastMondayUsageGrowthRate": "-4.41%"
                    },
                    {
                        "Item": "内存",
                        "Unit": "GB",
                        "Total": "135520",
                        "Usage": "101202",
                        "UsageRate": "74.68%",
                        "Remain": "34318",
                        "RemainRate": "25.32%",
                        "ThisMondayUsageRate": "74.72%",
                        "ThisMondayUsageGrowthRate": "-0.05%",
                        "LastMondayUsageGrowthRate": "-6.19%"
                    }
                ]
            },
            {
                "ProductName": "云硬盘",
                "SubProductName": "SSD云硬盘",
                "Statistics": [
                    {
                        "Item": "磁盘",
                        "Unit": "TB",
                        "Total": "64",
                        "Usage": "53.34",
                        "UsageRate": "83.34%",
                        "Remain": "10.66",
                        "RemainRate": "16.66%",
                        "ThisMondayUsageRate": "83.34%",
                        "ThisMondayUsageGrowthRate": "0.00%",
                        "LastMondayUsageGrowthRate": "4.58%"
                    }
                ]
            },
            {
                "ProductName": "云硬盘",
                "SubProductName": "高性能云硬盘",
                "Statistics": [
                    {
                        "Item": "磁盘",
                        "Unit": "TB",
                        "Total": "1392",
                        "Usage": "1157.32",
                        "UsageRate": "83.14%",
                        "Remain": "234.68",
                        "RemainRate": "16.86%",
                        "ThisMondayUsageRate": "82.03%",
                        "ThisMondayUsageGrowthRate": "1.11%",
                        "LastMondayUsageGrowthRate": "6.08%"
                    }
                ]
            },
            {
                "ProductName": "云数据库 MySQL",
                "SubProductName": "云数据库 MySQL",
                "Statistics": [
                    {
                        "Item": "内存",
                        "Unit": "GB",
                        "Total": "3600",
                        "Usage": "2031",
                        "UsageRate": "56.42%",
                        "Remain": "1569",
                        "RemainRate": "43.58%",
                        "ThisMondayUsageRate": "0.00%",
                        "ThisMondayUsageGrowthRate": "56.42%",
                        "LastMondayUsageGrowthRate": "-56.42%"
                    },
                    {
                        "Item": "磁盘",
                        "Unit": "TB",
                        "Total": "180",
                        "Usage": "82.12",
                        "UsageRate": "45.62%",
                        "Remain": "97.88",
                        "RemainRate": "54.38%",
                        "ThisMondayUsageRate": "0.00%",
                        "ThisMondayUsageGrowthRate": "45.62%",
                        "LastMondayUsageGrowthRate": "-45.62%"
                    }
                ]
            },
            {
                "ProductName": "云数据库 PostgreSQL",
                "SubProductName": "云数据库 PostgreSQL",
                "Statistics": [
                    {
                        "Item": "内存",
                        "Unit": "GB",
                        "Total": "22320",
                        "Usage": "14559",
                        "UsageRate": "65.23%",
                        "Remain": "7761",
                        "RemainRate": "34.77%",
                        "ThisMondayUsageRate": "65.23%",
                        "ThisMondayUsageGrowthRate": "0.00%",
                        "LastMondayUsageGrowthRate": "0.50%"
                    },
                    {
                        "Item": "磁盘",
                        "Unit": "TB",
                        "Total": "470",
                        "Usage": "304.68",
                        "UsageRate": "64.83%",
                        "Remain": "165.32",
                        "RemainRate": "35.17%",
                        "ThisMondayUsageRate": "64.83%",
                        "ThisMondayUsageGrowthRate": "0.00%",
                        "LastMondayUsageGrowthRate": "0.31%"
                    }
                ]
            },
            {
                "ProductName": "云数据库 Redis",
                "SubProductName": "云数据库 Redis",
                "Statistics": [
                    {
                        "Item": "内存",
                        "Unit": "GB",
                        "Total": "2400",
                        "Usage": "0",
                        "UsageRate": "0.00%",
                        "Remain": "2400",
                        "RemainRate": "100.00%",
                        "ThisMondayUsageRate": "0.00%",
                        "ThisMondayUsageGrowthRate": "0.00%",
                        "LastMondayUsageGrowthRate": "0.00%"
                    }
                ]
            }
        ],
        "RequestId": "0b2b5dda-8245-4a5a-b0ac-cbf2e7e47bca"
    }
}
```

