**Example 1: 获取控制台及购买页的地域和可用区成功示例**



Input: 

```
tccli emr DescribeRegionAndZoneSaleInfo --cli-unfold-argument  \
    --PageName consolePage
```

Output: 
```
{
    "Response": {
        "RequestId": "af919b67-d7ef-4310-ba37-486119c72db3",
        "SaleConf": [
            {
                "ClusterNumber": 7,
                "EnableSale": false,
                "Group": "South China",
                "Name": "Guangzhou",
                "RegionApCode": "ap-guangzhou",
                "RegionId": 1,
                "Status": "STANDARD",
                "ZoneInfo": [
                    {
                        "ApCode": "ap-guangzhou-2",
                        "EnableSale": false,
                        "Name": "Guangzhou Zone 2",
                        "Status": "STANDARD",
                        "ZoneId": 100002
                    },
                    {
                        "ApCode": "ap-guangzhou-3",
                        "EnableSale": false,
                        "Name": "Guangzhou Zone 3",
                        "Status": "STANDARD",
                        "ZoneId": 100003
                    },
                    {
                        "ApCode": "ap-guangzhou-4",
                        "EnableSale": false,
                        "Name": "Guangzhou Zone 4",
                        "Status": "STANDARD",
                        "ZoneId": 100004
                    }
                ]
            },
            {
                "ClusterNumber": 7,
                "EnableSale": false,
                "Group": "South China",
                "Name": "",
                "RegionApCode": "ap-shenzhen-fsi",
                "RegionId": 11,
                "Status": "STANDARD",
                "ZoneInfo": [
                    {
                        "ApCode": "ap-shenzhen-fsi-1",
                        "EnableSale": false,
                        "Name": "",
                        "Status": "STANDARD",
                        "ZoneId": 110001
                    },
                    {
                        "ApCode": "ap-shenzhen-fsi-2",
                        "EnableSale": false,
                        "Name": "",
                        "Status": "STANDARD",
                        "ZoneId": 110002
                    }
                ]
            },
            {
                "ClusterNumber": 7,
                "EnableSale": false,
                "Group": "Western U.S.",
                "Name": "",
                "RegionApCode": "na-siliconvalley",
                "RegionId": 15,
                "Status": "STANDARD",
                "ZoneInfo": [
                    {
                        "ApCode": "na-siliconvalley-1",
                        "EnableSale": false,
                        "Name": "",
                        "Status": "STANDARD",
                        "ZoneId": 150001
                    },
                    {
                        "ApCode": "na-siliconvalley-2",
                        "EnableSale": false,
                        "Name": "",
                        "Status": "STANDARD",
                        "ZoneId": 150002
                    }
                ]
            },
            {
                "ClusterNumber": 7,
                "EnableSale": false,
                "Group": "Southwest China",
                "Name": "",
                "RegionApCode": "ap-chengdu",
                "RegionId": 16,
                "Status": "STANDARD",
                "ZoneInfo": [
                    {
                        "ApCode": "ap-chengdu-1",
                        "EnableSale": false,
                        "Name": "",
                        "Status": "STANDARD",
                        "ZoneId": 160001
                    },
                    {
                        "ApCode": "ap-chengdu-2",
                        "EnableSale": false,
                        "Name": "",
                        "Status": "STANDARD",
                        "ZoneId": 160002
                    }
                ]
            },
            {
                "ClusterNumber": 7,
                "EnableSale": false,
                "Group": "Southwest China",
                "Name": "",
                "RegionApCode": "ap-chongqing",
                "RegionId": 19,
                "Status": "STANDARD",
                "ZoneInfo": [
                    {
                        "ApCode": "ap-chongqing-1",
                        "EnableSale": false,
                        "Name": "",
                        "Status": "STANDARD",
                        "ZoneId": 190001
                    }
                ]
            },
            {
                "ClusterNumber": 7,
                "EnableSale": false,
                "Group": "South Asia",
                "Name": "",
                "RegionApCode": "ap-mumbai",
                "RegionId": 21,
                "Status": "STANDARD",
                "ZoneInfo": [
                    {
                        "ApCode": "ap-mumbai-1",
                        "EnableSale": false,
                        "Name": "",
                        "Status": "STANDARD",
                        "ZoneId": 210001
                    },
                    {
                        "ApCode": "ap-mumbai-2",
                        "EnableSale": false,
                        "Name": "",
                        "Status": "STANDARD",
                        "ZoneId": 210002
                    }
                ]
            },
            {
                "ClusterNumber": 7,
                "EnableSale": false,
                "Group": "Europe",
                "Name": "",
                "RegionApCode": "eu-moscow",
                "RegionId": 24,
                "Status": "STANDARD",
                "ZoneInfo": [
                    {
                        "ApCode": "eu-moscow-1",
                        "EnableSale": false,
                        "Name": "",
                        "Status": "STANDARD",
                        "ZoneId": 240001
                    }
                ]
            },
            {
                "ClusterNumber": 7,
                "EnableSale": false,
                "Group": "East China",
                "Name": "",
                "RegionApCode": "ap-nanjing",
                "RegionId": 33,
                "Status": "STANDARD",
                "ZoneInfo": [
                    {
                        "ApCode": "ap-nanjing-1",
                        "EnableSale": false,
                        "Name": "",
                        "Status": "STANDARD",
                        "ZoneId": 330001
                    }
                ]
            },
            {
                "ClusterNumber": 7,
                "EnableSale": false,
                "Group": "East China",
                "Name": "Shanghai",
                "RegionApCode": "ap-shanghai",
                "RegionId": 4,
                "Status": "STANDARD",
                "ZoneInfo": [
                    {
                        "ApCode": "ap-shanghai-2",
                        "EnableSale": false,
                        "Name": "Shanghai Zone 2",
                        "Status": "STANDARD",
                        "ZoneId": 200002
                    },
                    {
                        "ApCode": "ap-shanghai-3",
                        "EnableSale": false,
                        "Name": "Shanghai Zone 3",
                        "Status": "STANDARD",
                        "ZoneId": 200003
                    },
                    {
                        "ApCode": "ap-shanghai-4",
                        "EnableSale": false,
                        "Name": "Shanghai Zone 4",
                        "Status": "STANDARD",
                        "ZoneId": 200004
                    }
                ]
            },
            {
                "ClusterNumber": 7,
                "EnableSale": false,
                "Group": "North China",
                "Name": "",
                "RegionApCode": "ap-beijing-fsi",
                "RegionId": 46,
                "Status": "STANDARD",
                "ZoneInfo": [
                    {
                        "ApCode": "ap-beijing-fsi-1",
                        "EnableSale": false,
                        "Name": "",
                        "Status": "STANDARD",
                        "ZoneId": 460001
                    }
                ]
            },
            {
                "ClusterNumber": 7,
                "EnableSale": false,
                "Group": "Hong/Kong/Macao/Taiw",
                "Name": "",
                "RegionApCode": "ap-hongkong",
                "RegionId": 5,
                "Status": "STANDARD",
                "ZoneInfo": [
                    {
                        "ApCode": "ap-hongkong-1",
                        "EnableSale": false,
                        "Name": "",
                        "Status": "STANDARD",
                        "ZoneId": 300001
                    },
                    {
                        "ApCode": "ap-hongkong-2",
                        "EnableSale": false,
                        "Name": "",
                        "Status": "STANDARD",
                        "ZoneId": 300002
                    }
                ]
            },
            {
                "ClusterNumber": 7,
                "EnableSale": false,
                "Group": "East China",
                "Name": "",
                "RegionApCode": "ap-shanghai-fsi",
                "RegionId": 7,
                "Status": "STANDARD",
                "ZoneInfo": [
                    {
                        "ApCode": "ap-shanghai-fsi-1",
                        "EnableSale": false,
                        "Name": "",
                        "Status": "STANDARD",
                        "ZoneId": 700001
                    },
                    {
                        "ApCode": "ap-shanghai-fsi-2",
                        "EnableSale": false,
                        "Name": "",
                        "Status": "STANDARD",
                        "ZoneId": 700002
                    },
                    {
                        "ApCode": "ap-shanghai-fsi-3",
                        "EnableSale": false,
                        "Name": "",
                        "Status": "STANDARD",
                        "ZoneId": 700003
                    }
                ]
            },
            {
                "ClusterNumber": 7,
                "EnableSale": false,
                "Group": "North China",
                "Name": "",
                "RegionApCode": "ap-beijing",
                "RegionId": 8,
                "Status": "STANDARD",
                "ZoneInfo": [
                    {
                        "ApCode": "ap-beijing-2",
                        "EnableSale": false,
                        "Name": "",
                        "Status": "STANDARD",
                        "ZoneId": 800002
                    },
                    {
                        "ApCode": "ap-beijing-3",
                        "EnableSale": false,
                        "Name": "",
                        "Status": "STANDARD",
                        "ZoneId": 800003
                    },
                    {
                        "ApCode": "ap-beijing-4",
                        "EnableSale": false,
                        "Name": "",
                        "Status": "STANDARD",
                        "ZoneId": 800004
                    },
                    {
                        "ApCode": "ap-beijing-5",
                        "EnableSale": false,
                        "Name": "",
                        "Status": "STANDARD",
                        "ZoneId": 800005
                    }
                ]
            },
            {
                "ClusterNumber": 7,
                "EnableSale": false,
                "Group": "Southeast Asia",
                "Name": "",
                "RegionApCode": "ap-singapore",
                "RegionId": 9,
                "Status": "STANDARD",
                "ZoneInfo": [
                    {
                        "ApCode": "ap-singapore-1",
                        "EnableSale": false,
                        "Name": "",
                        "Status": "STANDARD",
                        "ZoneId": 900001
                    }
                ]
            }
        ]
    }
}
```

