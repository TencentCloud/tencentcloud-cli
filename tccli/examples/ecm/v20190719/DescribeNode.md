**Example 1: 查看地域列表**

查看地域列表

Input: 

```
tccli ecm DescribeNode --cli-unfold-argument  \
    --Filters.0.Name InstanceFamily \
    --Filters.0.Values SN3ne
```

Output: 
```
{
    "Response": {
        "RequestId": "187c16d5-1f53-4e88-b684-077f0c7123b2",
        "NodeSet": [
            {
                "ZoneInfo": {
                    "ZoneId": 480001,
                    "ZoneName": "郑州一区",
                    "Zone": "ap-zhengzhou-ecm-1"
                },
                "Country": {
                    "CountryId": "china",
                    "CountryName": "中国"
                },
                "Area": {
                    "AreaId": "china-central",
                    "AreaName": "华中"
                },
                "Province": {
                    "ProvinceId": "china-central-henan",
                    "ProvinceName": "河南"
                },
                "City": {
                    "CityId": "china-central-henan-zhengzhou",
                    "CityName": "郑州"
                },
                "RegionInfo": {
                    "RegionId": 48,
                    "Region": "ap-zhengzhou-ecm",
                    "RegionName": "郑州"
                },
                "ISPSet": [
                    {
                        "ISPId": "CMCC",
                        "ISPName": "移动"
                    },
                    {
                        "ISPId": "CUCC",
                        "ISPName": "联通"
                    },
                    {
                        "ISPId": "CTCC",
                        "ISPName": "电信"
                    },
                    {
                        "ISPId": "CTCC;CUCC;CMCC",
                        "ISPName": "三网"
                    }
                ],
                "ISPNum": 3
            },
            {
                "ZoneInfo": {
                    "ZoneId": 490001,
                    "ZoneName": "青岛一区",
                    "Zone": "ap-qingdao-ecm-1"
                },
                "Country": {
                    "CountryId": "china",
                    "CountryName": "中国"
                },
                "Area": {
                    "AreaId": "china-east",
                    "AreaName": "华东"
                },
                "Province": {
                    "ProvinceId": "china-east-shandong",
                    "ProvinceName": "山东"
                },
                "City": {
                    "CityId": "china-east-shandong-qingdao",
                    "CityName": "青岛"
                },
                "RegionInfo": {
                    "RegionId": 49,
                    "Region": "ap-qingdao-ecm",
                    "RegionName": "青岛"
                },
                "ISPSet": [
                    {
                        "ISPId": "CMCC",
                        "ISPName": "移动"
                    },
                    {
                        "ISPId": "CUCC",
                        "ISPName": "联通"
                    },
                    {
                        "ISPId": "CTCC",
                        "ISPName": "电信"
                    },
                    {
                        "ISPId": "CTCC;CUCC;CMCC",
                        "ISPName": "三网"
                    }
                ],
                "ISPNum": 3
            },
            {
                "ZoneInfo": {
                    "ZoneId": 10110001,
                    "ZoneName": "杭州一区",
                    "Zone": "ap-hangzhou-ecm-1"
                },
                "Country": {
                    "CountryId": "china",
                    "CountryName": "中国"
                },
                "Area": {
                    "AreaId": "china-east",
                    "AreaName": "华东"
                },
                "Province": {
                    "ProvinceId": "china-east-zhejiang",
                    "ProvinceName": "浙江"
                },
                "City": {
                    "CityId": "china-east-zhejiang-hangzhou",
                    "CityName": "杭州"
                },
                "RegionInfo": {
                    "RegionId": 1011,
                    "Region": "ap-hangzhou-ecm",
                    "RegionName": "杭州"
                },
                "ISPSet": [
                    {
                        "ISPId": "CMCC",
                        "ISPName": "移动"
                    },
                    {
                        "ISPId": "CUCC",
                        "ISPName": "联通"
                    },
                    {
                        "ISPId": "CTCC",
                        "ISPName": "电信"
                    },
                    {
                        "ISPId": "CTCC;CUCC;CMCC",
                        "ISPName": "三网"
                    }
                ],
                "ISPNum": 3
            },
            {
                "ZoneInfo": {
                    "ZoneId": 10120001,
                    "ZoneName": "南京一区",
                    "Zone": "ap-nanjing-ecm2-1"
                },
                "Country": {
                    "CountryId": "china",
                    "CountryName": "中国"
                },
                "Area": {
                    "AreaId": "china-east",
                    "AreaName": "华东"
                },
                "Province": {
                    "ProvinceId": "china-east-jiangsu",
                    "ProvinceName": "江苏"
                },
                "City": {
                    "CityId": "china-east-jiangsu-nanjing",
                    "CityName": "南京"
                },
                "RegionInfo": {
                    "RegionId": 1012,
                    "Region": "ap-nanjing-ecm2",
                    "RegionName": "南京2"
                },
                "ISPSet": [
                    {
                        "ISPId": "CMCC",
                        "ISPName": "移动"
                    },
                    {
                        "ISPId": "CUCC",
                        "ISPName": "联通"
                    },
                    {
                        "ISPId": "CTCC",
                        "ISPName": "电信"
                    },
                    {
                        "ISPId": "CTCC;CUCC;CMCC",
                        "ISPName": "三网"
                    }
                ],
                "ISPNum": 3
            },
            {
                "ZoneInfo": {
                    "ZoneId": 10130001,
                    "ZoneName": "济南一区",
                    "Zone": "ap-jinan-ecm-1"
                },
                "Country": {
                    "CountryId": "china",
                    "CountryName": "中国"
                },
                "Area": {
                    "AreaId": "china-east",
                    "AreaName": "华东"
                },
                "Province": {
                    "ProvinceId": "china-east-shandong",
                    "ProvinceName": "山东"
                },
                "City": {
                    "CityId": "china-east-shandong-jinan",
                    "CityName": "济南"
                },
                "RegionInfo": {
                    "RegionId": 1013,
                    "Region": "ap-jinan-ecm",
                    "RegionName": "济南"
                },
                "ISPSet": [
                    {
                        "ISPId": "CMCC",
                        "ISPName": "移动"
                    },
                    {
                        "ISPId": "CUCC",
                        "ISPName": "联通"
                    },
                    {
                        "ISPId": "CTCC",
                        "ISPName": "电信"
                    },
                    {
                        "ISPId": "CTCC;CUCC;CMCC",
                        "ISPName": "三网"
                    }
                ],
                "ISPNum": 3
            },
            {
                "ZoneInfo": {
                    "ZoneId": 10140001,
                    "ZoneName": "石家庄一区",
                    "Zone": "ap-shijiazhuang-ecm-1"
                },
                "Country": {
                    "CountryId": "china",
                    "CountryName": "中国"
                },
                "Area": {
                    "AreaId": "china-north",
                    "AreaName": "华北"
                },
                "Province": {
                    "ProvinceId": "china-north-hebei",
                    "ProvinceName": "河北"
                },
                "City": {
                    "CityId": "china-north-hebei-shijiazhuang",
                    "CityName": "石家庄"
                },
                "RegionInfo": {
                    "RegionId": 1014,
                    "Region": "ap-shijiazhuang-ecm",
                    "RegionName": "石家庄"
                },
                "ISPSet": [
                    {
                        "ISPId": "CMCC",
                        "ISPName": "移动"
                    },
                    {
                        "ISPId": "CUCC",
                        "ISPName": "联通"
                    },
                    {
                        "ISPId": "CTCC",
                        "ISPName": "电信"
                    },
                    {
                        "ISPId": "CTCC;CUCC;CMCC",
                        "ISPName": "三网"
                    }
                ],
                "ISPNum": 3
            },
            {
                "ZoneInfo": {
                    "ZoneId": 10150001,
                    "ZoneName": "北京三区（电信）",
                    "Zone": "ap-beijing-ecm-ct-1"
                },
                "Country": {
                    "CountryId": "china",
                    "CountryName": "中国"
                },
                "Area": {
                    "AreaId": "china-north",
                    "AreaName": "华北"
                },
                "Province": {
                    "ProvinceId": "china-north-beijing",
                    "ProvinceName": "北京"
                },
                "City": {
                    "CityId": "china-north-beijing-beijing",
                    "CityName": "北京"
                },
                "RegionInfo": {
                    "RegionId": 1015,
                    "Region": "ap-beijing-ecm-ct",
                    "RegionName": "北京电信"
                },
                "ISPSet": [
                    {
                        "ISPId": "CTCC",
                        "ISPName": "电信"
                    }
                ],
                "ISPNum": 1
            },
            {
                "ZoneInfo": {
                    "ZoneId": 10160001,
                    "ZoneName": "北京四区（联通）",
                    "Zone": "ap-beijing-ecm-cu-1"
                },
                "Country": {
                    "CountryId": "china",
                    "CountryName": "中国"
                },
                "Area": {
                    "AreaId": "china-north",
                    "AreaName": "华北"
                },
                "Province": {
                    "ProvinceId": "china-north-beijing",
                    "ProvinceName": "北京"
                },
                "City": {
                    "CityId": "china-north-beijing-beijing",
                    "CityName": "北京"
                },
                "RegionInfo": {
                    "RegionId": 1016,
                    "Region": "ap-beijing-ecm-cu",
                    "RegionName": "北京联通"
                },
                "ISPSet": [
                    {
                        "ISPId": "CUCC",
                        "ISPName": "联通"
                    }
                ],
                "ISPNum": 1
            },
            {
                "ZoneInfo": {
                    "ZoneId": 10170001,
                    "ZoneName": "北京一区（移动）",
                    "Zone": "ap-beijing-ecm-cm-1"
                },
                "Country": {
                    "CountryId": "china",
                    "CountryName": "中国"
                },
                "Area": {
                    "AreaId": "china-north",
                    "AreaName": "华北"
                },
                "Province": {
                    "ProvinceId": "china-north-beijing",
                    "ProvinceName": "北京"
                },
                "City": {
                    "CityId": "china-north-beijing-beijing",
                    "CityName": "北京"
                },
                "RegionInfo": {
                    "RegionId": 1017,
                    "Region": "ap-beijing-ecm-cm",
                    "RegionName": "北京移动"
                },
                "ISPSet": [
                    {
                        "ISPId": "CMCC",
                        "ISPName": "移动"
                    }
                ],
                "ISPNum": 1
            },
            {
                "ZoneInfo": {
                    "ZoneId": 10180001,
                    "ZoneName": "西安一区",
                    "Zone": "ap-xian-ecm-1"
                },
                "Country": {
                    "CountryId": "china",
                    "CountryName": "中国"
                },
                "Area": {
                    "AreaId": "china-northwest",
                    "AreaName": "西北"
                },
                "Province": {
                    "ProvinceId": "china-northwest-shanxi",
                    "ProvinceName": "陕西"
                },
                "City": {
                    "CityId": "china-northwest-shanxi-xian",
                    "CityName": "西安"
                },
                "RegionInfo": {
                    "RegionId": 1018,
                    "Region": "ap-xian-ecm",
                    "RegionName": "西安"
                },
                "ISPSet": [
                    {
                        "ISPId": "CMCC",
                        "ISPName": "移动"
                    },
                    {
                        "ISPId": "CUCC",
                        "ISPName": "联通"
                    },
                    {
                        "ISPId": "CTCC",
                        "ISPName": "电信"
                    },
                    {
                        "ISPId": "CTCC;CUCC;CMCC",
                        "ISPName": "三网"
                    }
                ],
                "ISPNum": 3
            },
            {
                "ZoneInfo": {
                    "ZoneId": 10200001,
                    "ZoneName": "上海二区（联通）",
                    "Zone": "ap-shanghai-ecm-cu-1"
                },
                "Country": {
                    "CountryId": "china",
                    "CountryName": "中国"
                },
                "Area": {
                    "AreaId": "china-east",
                    "AreaName": "华东"
                },
                "Province": {
                    "ProvinceId": "china-east-shanghai",
                    "ProvinceName": "上海"
                },
                "City": {
                    "CityId": "china-east-shanghai-shanghai",
                    "CityName": "上海"
                },
                "RegionInfo": {
                    "RegionId": 1020,
                    "Region": "ap-shanghai-ecm-cu",
                    "RegionName": "上海联通"
                },
                "ISPSet": [
                    {
                        "ISPId": "CUCC",
                        "ISPName": "联通"
                    }
                ],
                "ISPNum": 1
            },
            {
                "ZoneInfo": {
                    "ZoneId": 10210001,
                    "ZoneName": "上海一区（移动）",
                    "Zone": "ap-shanghai-ecm-cm-1"
                },
                "Country": {
                    "CountryId": "china",
                    "CountryName": "中国"
                },
                "Area": {
                    "AreaId": "china-east",
                    "AreaName": "华东"
                },
                "Province": {
                    "ProvinceId": "china-east-shanghai",
                    "ProvinceName": "上海"
                },
                "City": {
                    "CityId": "china-east-shanghai-shanghai",
                    "CityName": "上海"
                },
                "RegionInfo": {
                    "RegionId": 1021,
                    "Region": "ap-shanghai-ecm-cm",
                    "RegionName": "上海移动"
                },
                "ISPSet": [
                    {
                        "ISPId": "CMCC",
                        "ISPName": "移动"
                    }
                ],
                "ISPNum": 1
            },
            {
                "ZoneInfo": {
                    "ZoneId": 10220001,
                    "ZoneName": "广州一区（电信）",
                    "Zone": "ap-guangzhou-ecm-ct-1"
                },
                "Country": {
                    "CountryId": "china",
                    "CountryName": "中国"
                },
                "Area": {
                    "AreaId": "china-south",
                    "AreaName": "华南"
                },
                "Province": {
                    "ProvinceId": "china-south-guangdong",
                    "ProvinceName": "广东"
                },
                "City": {
                    "CityId": "china-south-guangdong-guangzhou",
                    "CityName": "广州"
                },
                "RegionInfo": {
                    "RegionId": 1022,
                    "Region": "ap-guangzhou-ecm-ct",
                    "RegionName": "广州电信"
                },
                "ISPSet": [
                    {
                        "ISPId": "CTCC",
                        "ISPName": "电信"
                    }
                ],
                "ISPNum": 1
            },
            {
                "ZoneInfo": {
                    "ZoneId": 10230001,
                    "ZoneName": "广州四区（联通）",
                    "Zone": "ap-guangzhou-ecm-cu-1"
                },
                "Country": {
                    "CountryId": "china",
                    "CountryName": "中国"
                },
                "Area": {
                    "AreaId": "china-south",
                    "AreaName": "华南"
                },
                "Province": {
                    "ProvinceId": "china-south-guangdong",
                    "ProvinceName": "广东"
                },
                "City": {
                    "CityId": "china-south-guangdong-guangzhou",
                    "CityName": "广州"
                },
                "RegionInfo": {
                    "RegionId": 1023,
                    "Region": "ap-guangzhou-ecm-cu",
                    "RegionName": "广州联通"
                },
                "ISPSet": [
                    {
                        "ISPId": "CUCC",
                        "ISPName": "联通"
                    }
                ],
                "ISPNum": 1
            },
            {
                "ZoneInfo": {
                    "ZoneId": 10250001,
                    "ZoneName": "深圳一区（电信）",
                    "Zone": "ap-shenzhen-ecm-ct-1"
                },
                "Country": {
                    "CountryId": "china",
                    "CountryName": "中国"
                },
                "Area": {
                    "AreaId": "china-south",
                    "AreaName": "华南"
                },
                "Province": {
                    "ProvinceId": "china-south-guangdong",
                    "ProvinceName": "广东"
                },
                "City": {
                    "CityId": "china-south-guangdong-shenzhen",
                    "CityName": "深圳"
                },
                "RegionInfo": {
                    "RegionId": 1025,
                    "Region": "ap-shenzhen-ecm-ct",
                    "RegionName": "深圳电信"
                },
                "ISPSet": [
                    {
                        "ISPId": "CTCC",
                        "ISPName": "电信"
                    }
                ],
                "ISPNum": 1
            },
            {
                "ZoneInfo": {
                    "ZoneId": 10260001,
                    "ZoneName": "深圳四区（联通）",
                    "Zone": "ap-shenzhen-ecm-cu-1"
                },
                "Country": {
                    "CountryId": "china",
                    "CountryName": "中国"
                },
                "Area": {
                    "AreaId": "china-south",
                    "AreaName": "华南"
                },
                "Province": {
                    "ProvinceId": "china-south-guangdong",
                    "ProvinceName": "广东"
                },
                "City": {
                    "CityId": "china-south-guangdong-shenzhen",
                    "CityName": "深圳"
                },
                "RegionInfo": {
                    "RegionId": 1026,
                    "Region": "ap-shenzhen-ecm-cu",
                    "RegionName": "深圳联通"
                },
                "ISPSet": [
                    {
                        "ISPId": "CUCC",
                        "ISPName": "联通"
                    }
                ],
                "ISPNum": 1
            },
            {
                "ZoneInfo": {
                    "ZoneId": 10270001,
                    "ZoneName": "深圳二区（移动）",
                    "Zone": "ap-shenzhen-ecm-cm-1"
                },
                "Country": {
                    "CountryId": "china",
                    "CountryName": "中国"
                },
                "Area": {
                    "AreaId": "china-south",
                    "AreaName": "华南"
                },
                "Province": {
                    "ProvinceId": "china-south-guangdong",
                    "ProvinceName": "广东"
                },
                "City": {
                    "CityId": "china-south-guangdong-shenzhen",
                    "CityName": "深圳"
                },
                "RegionInfo": {
                    "RegionId": 1027,
                    "Region": "ap-shenzhen-ecm-cm",
                    "RegionName": "深圳移动"
                },
                "ISPSet": [
                    {
                        "ISPId": "CMCC",
                        "ISPName": "移动"
                    }
                ],
                "ISPNum": 1
            },
            {
                "ZoneInfo": {
                    "ZoneId": 10280001,
                    "ZoneName": "成都一区（电信）",
                    "Zone": "ap-chengdu-ecm-ct-1"
                },
                "Country": {
                    "CountryId": "china",
                    "CountryName": "中国"
                },
                "Area": {
                    "AreaId": "china-southwest",
                    "AreaName": "西南"
                },
                "Province": {
                    "ProvinceId": "china-southwest-sichuan",
                    "ProvinceName": "四川"
                },
                "City": {
                    "CityId": "china-southwest-sichuan-chengdu",
                    "CityName": "成都"
                },
                "RegionInfo": {
                    "RegionId": 1028,
                    "Region": "ap-chengdu-ecm-ct",
                    "RegionName": "成都电信"
                },
                "ISPSet": [
                    {
                        "ISPId": "CTCC",
                        "ISPName": "电信"
                    }
                ],
                "ISPNum": 1
            },
            {
                "ZoneInfo": {
                    "ZoneId": 10290001,
                    "ZoneName": "成都五区（联通）",
                    "Zone": "ap-chengdu-ecm-cu-1"
                },
                "Country": {
                    "CountryId": "china",
                    "CountryName": "中国"
                },
                "Area": {
                    "AreaId": "china-southwest",
                    "AreaName": "西南"
                },
                "Province": {
                    "ProvinceId": "china-southwest-sichuan",
                    "ProvinceName": "四川"
                },
                "City": {
                    "CityId": "china-southwest-sichuan-chengdu",
                    "CityName": "成都"
                },
                "RegionInfo": {
                    "RegionId": 1029,
                    "Region": "ap-chengdu-ecm-cu",
                    "RegionName": "成都联通2"
                },
                "ISPSet": [
                    {
                        "ISPId": "CUCC",
                        "ISPName": "联通"
                    }
                ],
                "ISPNum": 1
            },
            {
                "ZoneInfo": {
                    "ZoneId": 10300001,
                    "ZoneName": "成都二区（移动）",
                    "Zone": "ap-chengdu-ecm-cm-1"
                },
                "Country": {
                    "CountryId": "china",
                    "CountryName": "中国"
                },
                "Area": {
                    "AreaId": "china-southwest",
                    "AreaName": "西南"
                },
                "Province": {
                    "ProvinceId": "china-southwest-sichuan",
                    "ProvinceName": "四川"
                },
                "City": {
                    "CityId": "china-southwest-sichuan-chengdu",
                    "CityName": "成都"
                },
                "RegionInfo": {
                    "RegionId": 1030,
                    "Region": "ap-chengdu-ecm-cm",
                    "RegionName": "成都移动"
                },
                "ISPSet": [
                    {
                        "ISPId": "CMCC",
                        "ISPName": "移动"
                    }
                ],
                "ISPNum": 1
            },
            {
                "ZoneInfo": {
                    "ZoneId": 10310001,
                    "ZoneName": "武汉一区",
                    "Zone": "ap-wuhan-ecm-1"
                },
                "Country": {
                    "CountryId": "china",
                    "CountryName": "中国"
                },
                "Area": {
                    "AreaId": "china-central",
                    "AreaName": "华中"
                },
                "Province": {
                    "ProvinceId": "china-central-hubei",
                    "ProvinceName": "湖北"
                },
                "City": {
                    "CityId": "china-central-hubei-wuhan",
                    "CityName": "武汉"
                },
                "RegionInfo": {
                    "RegionId": 1031,
                    "Region": "ap-wuhan-ecm",
                    "RegionName": "武汉"
                },
                "ISPSet": [
                    {
                        "ISPId": "CMCC",
                        "ISPName": "移动"
                    },
                    {
                        "ISPId": "CUCC",
                        "ISPName": "联通"
                    },
                    {
                        "ISPId": "CTCC",
                        "ISPName": "电信"
                    },
                    {
                        "ISPId": "CTCC;CUCC;CMCC",
                        "ISPName": "三网"
                    }
                ],
                "ISPNum": 3
            },
            {
                "ZoneInfo": {
                    "ZoneId": 10320001,
                    "ZoneName": "北京五区（联通）",
                    "Zone": "ap-beijing-ecm-cu2-1"
                },
                "Country": {
                    "CountryId": "china",
                    "CountryName": "中国"
                },
                "Area": {
                    "AreaId": "china-north",
                    "AreaName": "华北"
                },
                "Province": {
                    "ProvinceId": "china-north-beijing",
                    "ProvinceName": "北京"
                },
                "City": {
                    "CityId": "china-north-beijing-beijing",
                    "CityName": "北京"
                },
                "RegionInfo": {
                    "RegionId": 1032,
                    "Region": "ap-beijing-ecm-cu2",
                    "RegionName": "北京联通2"
                },
                "ISPSet": [
                    {
                        "ISPId": "CUCC",
                        "ISPName": "联通"
                    }
                ],
                "ISPNum": 1
            },
            {
                "ZoneInfo": {
                    "ZoneId": 10330001,
                    "ZoneName": "北京二区（移动）",
                    "Zone": "ap-beijing-ecm-cm2-1"
                },
                "Country": {
                    "CountryId": "china",
                    "CountryName": "中国"
                },
                "Area": {
                    "AreaId": "china-north",
                    "AreaName": "华北"
                },
                "Province": {
                    "ProvinceId": "china-north-beijing",
                    "ProvinceName": "北京"
                },
                "City": {
                    "CityId": "china-north-beijing-beijing",
                    "CityName": "北京"
                },
                "RegionInfo": {
                    "RegionId": 1033,
                    "Region": "ap-beijing-ecm-cm2",
                    "RegionName": "北京移动2"
                },
                "ISPSet": [
                    {
                        "ISPId": "CMCC",
                        "ISPName": "移动"
                    }
                ],
                "ISPNum": 1
            },
            {
                "ZoneInfo": {
                    "ZoneId": 10340001,
                    "ZoneName": "广州二区（电信）",
                    "Zone": "ap-guangzhou-ecm-ct2-1"
                },
                "Country": {
                    "CountryId": "china",
                    "CountryName": "中国"
                },
                "Area": {
                    "AreaId": "china-south",
                    "AreaName": "华南"
                },
                "Province": {
                    "ProvinceId": "china-south-guangdong",
                    "ProvinceName": "广东"
                },
                "City": {
                    "CityId": "china-south-guangdong-guangzhou",
                    "CityName": "广州"
                },
                "RegionInfo": {
                    "RegionId": 1034,
                    "Region": "ap-guangzhou-ecm-ct2",
                    "RegionName": "广州电信2"
                },
                "ISPSet": [
                    {
                        "ISPId": "CTCC",
                        "ISPName": "电信"
                    }
                ],
                "ISPNum": 1
            },
            {
                "ZoneInfo": {
                    "ZoneId": 10350001,
                    "ZoneName": "成都四区（电信）",
                    "Zone": "ap-chengdu-ecm-ct2-1"
                },
                "Country": {
                    "CountryId": "china",
                    "CountryName": "中国"
                },
                "Area": {
                    "AreaId": "china-southwest",
                    "AreaName": "西南"
                },
                "Province": {
                    "ProvinceId": "china-southwest-sichuan",
                    "ProvinceName": "四川"
                },
                "City": {
                    "CityId": "china-southwest-sichuan-chengdu",
                    "CityName": "成都"
                },
                "RegionInfo": {
                    "RegionId": 1035,
                    "Region": "ap-chengdu-ecm-ct2",
                    "RegionName": "成都电信2"
                },
                "ISPSet": [
                    {
                        "ISPId": "CTCC",
                        "ISPName": "电信"
                    }
                ],
                "ISPNum": 1
            },
            {
                "ZoneInfo": {
                    "ZoneId": 10360001,
                    "ZoneName": "成都三区（移动）",
                    "Zone": "ap-chengdu-ecm-cm2-1"
                },
                "Country": {
                    "CountryId": "china",
                    "CountryName": "中国"
                },
                "Area": {
                    "AreaId": "china-southwest",
                    "AreaName": "西南"
                },
                "Province": {
                    "ProvinceId": "china-southwest-sichuan",
                    "ProvinceName": "四川"
                },
                "City": {
                    "CityId": "china-southwest-sichuan-chengdu",
                    "CityName": "成都"
                },
                "RegionInfo": {
                    "RegionId": 1036,
                    "Region": "ap-chengdu-ecm-cm2",
                    "RegionName": "成都移动2"
                },
                "ISPSet": [
                    {
                        "ISPId": "CMCC",
                        "ISPName": "移动"
                    }
                ],
                "ISPNum": 1
            },
            {
                "ZoneInfo": {
                    "ZoneId": 10370001,
                    "ZoneName": "深圳三区（移动）",
                    "Zone": "ap-shenzhen-ecm-cm2-1"
                },
                "Country": {
                    "CountryId": "china",
                    "CountryName": "中国"
                },
                "Area": {
                    "AreaId": "china-south",
                    "AreaName": "华南"
                },
                "Province": {
                    "ProvinceId": "china-south-guangdong",
                    "ProvinceName": "广东"
                },
                "City": {
                    "CityId": "china-south-guangdong-shenzhen",
                    "CityName": "深圳"
                },
                "RegionInfo": {
                    "RegionId": 1037,
                    "Region": "ap-shenzhen-ecm-cm2",
                    "RegionName": "深圳移动"
                },
                "ISPSet": [
                    {
                        "ISPId": "CMCC",
                        "ISPName": "移动"
                    }
                ],
                "ISPNum": 1
            },
            {
                "ZoneInfo": {
                    "ZoneId": 10380001,
                    "ZoneName": "东莞一区（联通）",
                    "Zone": "ap-dongguan-ecm-cu-1"
                },
                "Country": {
                    "CountryId": "china",
                    "CountryName": "中国"
                },
                "Area": {
                    "AreaId": "china-south",
                    "AreaName": "华南"
                },
                "Province": {
                    "ProvinceId": "china-south-guangdong",
                    "ProvinceName": "广东"
                },
                "City": {
                    "CityId": "china-south-guangdong-dongguan",
                    "CityName": "东莞"
                },
                "RegionInfo": {
                    "RegionId": 1038,
                    "Region": "ap-dongguan-ecm-cu",
                    "RegionName": "东莞联通"
                },
                "ISPSet": [
                    {
                        "ISPId": "CUCC",
                        "ISPName": "联通"
                    }
                ],
                "ISPNum": 1
            }
        ],
        "TotalCount": 28
    }
}
```

