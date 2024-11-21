**Example 1: DescribeSourceAsset-查询全部资产信息**

DescribeSourceAsset-查询全部资产信息

Input: 

```
tccli cfw DescribeSourceAsset --cli-unfold-argument  \
    --ChooseType 0 \
    --FuzzySearch ins \
    --InsType 1 \
    --Limit 10 \
    --Offset 0 \
    --Zone ap-chengdu
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AppId": "1300448055",
                "Region": "ap-chengdu",
                "RegionKey": "AP-CHENGDU",
                "VpcId": "vpc-n7k5rwjg",
                "SubnetId": "subnet-oq7vudkb",
                "InstanceId": "eni-2npbqunq",
                "InstanceName": "eth1",
                "InsType": 5,
                "PublicIp": "148.70.225.68",
                "PrivateIp": "10.27.0.20,10.27.0.21,10.27.0.22,10.27.0.23,10.27.0.24,10.27.0.25,10.27.0.26,10.27.0.27,10.27.0.28,10.27.0.8",
                "PortNum": "1",
                "LeakNum": "1",
                "VPCName": "vpc1",
                "InsSource": "1",
                "ResourcePath": [
                    "/全部资产/测试环境/",
                    "/全部资产/测试环境/DMZ隔离区/"
                ],
                "Server": [
                    "dns"
                ]
            }
        ],
        "RequestId": "c6d441d3-1871-4913-ac41-b552324fa895",
        "Total": 53,
        "ZoneList": [
            {
                "Zone": "ap-guangzhou",
                "ZoneEng": "广州"
            },
            {
                "Zone": "ap-beijing",
                "ZoneEng": "北京"
            },
            {
                "Zone": "ap-singapore",
                "ZoneEng": "新加坡"
            },
            {
                "Zone": "ap-chengdu",
                "ZoneEng": "成都"
            },
            {
                "Zone": "ap-shanghai",
                "ZoneEng": "上海"
            },
            {
                "Zone": "ap-nanjing",
                "ZoneEng": "南京"
            },
            {
                "Zone": "ap-hongkong",
                "ZoneEng": "中国香港"
            },
            {
                "Zone": "ap-wuhan-ec",
                "ZoneEng": "武汉EC"
            },
            {
                "Zone": "ap-chongqing",
                "ZoneEng": "重庆"
            }
        ]
    }
}
```

