**Example 1: 获取拨测点组**

获取拨测点组


Input: 

```
tccli cat DescribeNodeGroups --cli-unfold-argument  \
    --RegionID 1 \
    --NetServiceID 99
```

Output: 
```
{
    "Response": {
        "DistrictList": [
            {
                "ID": "0",
                "Name": "全部"
            },
            {
                "ID": "1100100",
                "Name": "黑龙江"
            }
        ],
        "NetServiceList": [
            {
                "ID": "0",
                "Name": "全部"
            },
            {
                "ID": "99",
                "Name": "其他"
            }
        ],
        "NodeList": [
            {
                "ID": "1102700",
                "Content": "黑龙江",
                "Children": [
                    {
                        "ID": "1102701",
                        "Content": "哈尔滨市",
                        "Children": [
                            {
                                "ID": "11537",
                                "Content": "黑龙江-哈尔滨市-广电宽带[LM]"
                            }
                        ]
                    }
                ]
            }
        ],
        "RequestId": "fyy3-g7ujmxbouxshy3plmkmhlnmdbfh"
    }
}
```

**Example 2: 获取定时任务拨测点组**

获取定时任务中网络质量任务类型，PC类任务的可用性拨测点组

Input: 

```
tccli cat DescribeNodeGroups --cli-unfold-argument  \
    --NodeGroupType 1 \
    --IPType 0 \
    --NodeType 1 \
    --TaskType 5 \
    --ProbeType 0
```

Output: 
```
{
    "Response": {
        "DistrictList": [],
        "NetServiceList": [],
        "NodeList": [
            {
                "ID": "PC",
                "Content": "PC",
                "Children": [
                    {
                        "ID": "125",
                        "Content": "国内区域可用性探测",
                        "Children": [
                            {
                                "ID": "12136",
                                "Content": "广东-深圳市[IDC]"
                            }
                        ]
                    },
                    {
                        "ID": "126",
                        "Content": "国内十大城市",
                        "Children": [
                            {
                                "ID": "12136",
                                "Content": "广东-深圳市[IDC]"
                            }
                        ]
                    },
                    {
                        "ID": "127",
                        "Content": "国内主要城市运营商",
                        "Children": [
                            {
                                "ID": "12058",
                                "Content": "广东-广州市-中国移动[IDC]"
                            }
                        ]
                    },
                    {
                        "ID": "141",
                        "Content": "海外主要城市",
                        "Children": [
                            {
                                "ID": "12170",
                                "Content": "美国-弗吉尼亚州[IDC]"
                            }
                        ]
                    },
                    {
                        "ID": "142",
                        "Content": "港澳台主要城市",
                        "Children": [
                            {
                                "ID": "12181",
                                "Content": "香港-香港特区[IDC]"
                            }
                        ]
                    }
                ]
            }
        ],
        "RequestId": "3ea82ed9-5901-4c69-b5e2-c4c84c9538e5"
    }
}
```

**Example 3: 获取即时拨测拨测点组**

获取即时拨测任务中网络质量任务类型，PC类任务的精选拨测点组

Input: 

```
tccli cat DescribeNodeGroups --cli-unfold-argument  \
    --NodeGroupType 0 \
    --TaskCategory 1 \
    --IPType 0 \
    --NodeType 1 2 \
    --TaskType 5 \
    --ProbeType 1
```

Output: 
```
{
    "Response": {
        "DistrictList": [],
        "NetServiceList": [
            {
                "ID": "0",
                "Name": "全部"
            }
        ],
        "NodeList": [
            {
                "ID": "IDC",
                "Content": "IDC",
                "Children": [
                    {
                        "ID": "560",
                        "Content": "境内主要城市运营商",
                        "Children": [
                            {
                                "ID": "10000",
                                "Content": "北京-北京市-中国电信[IDC]"
                            }
                        ]
                    }
                ]
            },
            {
                "ID": "LastMile",
                "Content": "LastMile",
                "Children": [
                    {
                        "ID": "27",
                        "Content": "省会城市-电信(Last Mile)",
                        "Children": [
                            {
                                "ID": "10103",
                                "Content": "北京-北京市-中国电信[LM]"
                            }
                        ]
                    }
                ]
            }
        ],
        "RequestId": "248cfe54-6cb6-46c7-b73d-9c78108add00"
    }
}
```

