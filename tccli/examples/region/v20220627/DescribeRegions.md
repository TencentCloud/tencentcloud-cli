**Example 1: 查询产品支持的地域列表**

查询产品支持的地域列表

Input: 

```
tccli region DescribeRegions --cli-unfold-argument  \
    --Product cvm \
    --Scene 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 21,
        "RequestId": "2b41c59d-93c8-43e2-a2f0-6c5df9735d21",
        "RegionSet": [
            {
                "RegionIdMC": null,
                "LocationMC": null,
                "RegionState": "AVAILABLE",
                "RegionNameMC": null,
                "Region": "ap-guangzhou",
                "RegionTypeMC": null,
                "RegionName": "华南地区(广州)"
            },
            {
                "RegionIdMC": null,
                "LocationMC": null,
                "RegionState": "AVAILABLE",
                "RegionNameMC": null,
                "Region": "ap-shanghai",
                "RegionTypeMC": null,
                "RegionName": "华东地区(上海)"
            },
            {
                "RegionIdMC": null,
                "LocationMC": null,
                "RegionState": "AVAILABLE",
                "RegionNameMC": null,
                "Region": "ap-nanjing",
                "RegionTypeMC": null,
                "RegionName": "华东地区(南京)"
            },
            {
                "RegionIdMC": null,
                "LocationMC": null,
                "RegionState": "AVAILABLE",
                "RegionNameMC": null,
                "Region": "ap-beijing",
                "RegionTypeMC": null,
                "RegionName": "华北地区(北京)"
            },
            {
                "RegionIdMC": null,
                "LocationMC": null,
                "RegionState": "AVAILABLE",
                "RegionNameMC": null,
                "Region": "ap-chengdu",
                "RegionTypeMC": null,
                "RegionName": "西南地区(成都)"
            },
            {
                "RegionIdMC": null,
                "LocationMC": null,
                "RegionState": "AVAILABLE",
                "RegionNameMC": null,
                "Region": "ap-chongqing",
                "RegionTypeMC": null,
                "RegionName": "西南地区(重庆)"
            },
            {
                "RegionIdMC": null,
                "LocationMC": null,
                "RegionState": "AVAILABLE",
                "RegionNameMC": null,
                "Region": "ap-xian-ec",
                "RegionTypeMC": null,
                "RegionName": "西北地区(西安)"
            },
            {
                "RegionIdMC": null,
                "LocationMC": null,
                "RegionState": "AVAILABLE",
                "RegionNameMC": null,
                "Region": "ap-hongkong",
                "RegionTypeMC": null,
                "RegionName": "港澳台地区(中国香港)"
            },
            {
                "RegionIdMC": null,
                "LocationMC": null,
                "RegionState": "AVAILABLE",
                "RegionNameMC": null,
                "Region": "ap-guiyang",
                "RegionTypeMC": null,
                "RegionName": "西南地区(贵阳)"
            },
            {
                "RegionIdMC": null,
                "LocationMC": null,
                "RegionState": "AVAILABLE",
                "RegionNameMC": null,
                "Region": "ap-seoul",
                "RegionTypeMC": null,
                "RegionName": "亚太东北(首尔)"
            },
            {
                "RegionIdMC": null,
                "LocationMC": null,
                "RegionState": "AVAILABLE",
                "RegionNameMC": null,
                "Region": "ap-tokyo",
                "RegionTypeMC": null,
                "RegionName": "亚太东北(东京)"
            },
            {
                "RegionIdMC": null,
                "LocationMC": null,
                "RegionState": "AVAILABLE",
                "RegionNameMC": null,
                "Region": "ap-singapore",
                "RegionTypeMC": null,
                "RegionName": "亚太东南(新加坡)"
            },
            {
                "RegionIdMC": null,
                "LocationMC": null,
                "RegionState": "AVAILABLE",
                "RegionNameMC": null,
                "Region": "ap-bangkok",
                "RegionTypeMC": null,
                "RegionName": "亚太东南(曼谷)"
            },
            {
                "RegionIdMC": null,
                "LocationMC": null,
                "RegionState": "AVAILABLE",
                "RegionNameMC": null,
                "Region": "ap-jakarta",
                "RegionTypeMC": null,
                "RegionName": "亚太东南(雅加达)"
            },
            {
                "RegionIdMC": null,
                "LocationMC": null,
                "RegionState": "AVAILABLE",
                "RegionNameMC": null,
                "Region": "na-siliconvalley",
                "RegionTypeMC": null,
                "RegionName": "美国西部(硅谷)"
            },
            {
                "RegionIdMC": null,
                "LocationMC": null,
                "RegionState": "AVAILABLE",
                "RegionNameMC": null,
                "Region": "eu-frankfurt",
                "RegionTypeMC": null,
                "RegionName": "欧洲地区(法兰克福)"
            },
            {
                "RegionIdMC": null,
                "LocationMC": null,
                "RegionState": "AVAILABLE",
                "RegionNameMC": null,
                "Region": "ap-mumbai",
                "RegionTypeMC": null,
                "RegionName": "亚太南部(孟买)"
            },
            {
                "RegionIdMC": null,
                "LocationMC": null,
                "RegionState": "AVAILABLE",
                "RegionNameMC": null,
                "Region": "na-ashburn",
                "RegionTypeMC": null,
                "RegionName": "美国东部(弗吉尼亚)"
            },
            {
                "RegionIdMC": null,
                "LocationMC": null,
                "RegionState": "AVAILABLE",
                "RegionNameMC": null,
                "Region": "sa-saopaulo",
                "RegionTypeMC": null,
                "RegionName": "南美地区(圣保罗)"
            },
            {
                "RegionIdMC": null,
                "LocationMC": null,
                "RegionState": "AVAILABLE",
                "RegionNameMC": null,
                "Region": "na-toronto",
                "RegionTypeMC": null,
                "RegionName": "北美地区(多伦多)"
            }
        ]
    }
}
```

