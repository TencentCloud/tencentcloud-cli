**Example 1: 查询资产组全部资产信息**



Input: 

```
tccli cfw DescribeSourceAsset --cli-unfold-argument  \
    --InsType  \
    --Zone  \
    --ChooseType 0 \
    --FuzzySearch  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AppId": "",
                "Region": "ap-guangzhou",
                "RegionKey": "",
                "VpcId": "vpc-3kdn8tfl",
                "SubnetId": "subnet-jovl8il2",
                "InstanceId": "crs-jkbfbllz",
                "InstanceName": "test-ipv6",
                "InsType": 7,
                "PublicIp": "",
                "PrivateIp": "10.11.77.14",
                "PortNum": "",
                "LeakNum": "",
                "VPCName": "",
                "InsSource": "",
                "ResourcePath": [],
                "Server": null
            },
            {
                "AppId": "",
                "Region": "ap-guangzhou",
                "RegionKey": "",
                "VpcId": "vpc-12wu4ke9",
                "SubnetId": "subnet-6jm69l78",
                "InstanceId": "eni-180aej3b",
                "InstanceName": "111",
                "InsType": 5,
                "PublicIp": "",
                "PrivateIp": "192.168.0.3",
                "PortNum": "",
                "LeakNum": "",
                "VPCName": "",
                "InsSource": "",
                "ResourcePath": [],
                "Server": null
            },
            {
                "AppId": "",
                "Region": "ap-beijing",
                "RegionKey": "",
                "VpcId": "vpc-0lucogis",
                "SubnetId": "subnet-r10fryfv",
                "InstanceId": "eni-1njhyq4g",
                "InstanceName": "test",
                "InsType": 5,
                "PublicIp": "",
                "PrivateIp": "10.111.0.15",
                "PortNum": "",
                "LeakNum": "",
                "VPCName": "",
                "InsSource": "",
                "ResourcePath": [],
                "Server": null
            },
            {
                "AppId": "",
                "Region": "ap-singapore",
                "RegionKey": "",
                "VpcId": "vpc-bozc3uj5",
                "SubnetId": "subnet-48hj9yiu",
                "InstanceId": "eni-2f35far7",
                "InstanceName": "未命名",
                "InsType": 5,
                "PublicIp": "",
                "PrivateIp": "10.1.0.21,10.1.0.22,10.1.0.23,10.1.0.24,10.1.0.25,10.1.0.26,10.1.0.27,10.1.0.28,10.1.0.29",
                "PortNum": "",
                "LeakNum": "",
                "VPCName": "",
                "InsSource": "",
                "ResourcePath": [],
                "Server": null
            },
            {
                "AppId": "",
                "Region": "ap-chengdu",
                "RegionKey": "",
                "VpcId": "vpc-n7k5rwjg",
                "SubnetId": "subnet-oq7vudkb",
                "InstanceId": "eni-2npbqunq",
                "InstanceName": "eth1",
                "InsType": 5,
                "PublicIp": "148.70.225.68",
                "PrivateIp": "10.27.0.20,10.27.0.21,10.27.0.22,10.27.0.23,10.27.0.24,10.27.0.25,10.27.0.26,10.27.0.27,10.27.0.28,10.27.0.8",
                "PortNum": "",
                "LeakNum": "",
                "VPCName": "",
                "InsSource": "",
                "ResourcePath": [],
                "Server": null
            },
            {
                "AppId": "",
                "Region": "ap-singapore",
                "RegionKey": "",
                "VpcId": "vpc-n6s7a21j",
                "SubnetId": "subnet-c4434w3y",
                "InstanceId": "eni-3fcx9q39",
                "InstanceName": "未命名",
                "InsType": 5,
                "PublicIp": "",
                "PrivateIp": "172.22.32.10,172.22.32.11,172.22.32.12,172.22.32.14,172.22.32.15,172.22.32.16,172.22.32.17,172.22.32.2,172.22.32.29,172.22.32.3,172.22.32.36,172.22.32.4,172.22.32.41,172.22.32.47,172.22.32.48,172.22.32.5,172.22.32.6,172.22.32.7,172.22.32.8,172.22.32.9",
                "PortNum": "",
                "LeakNum": "",
                "VPCName": "",
                "InsSource": "",
                "ResourcePath": [],
                "Server": null
            },
            {
                "AppId": "",
                "Region": "ap-singapore",
                "RegionKey": "",
                "VpcId": "vpc-n6s7a21j",
                "SubnetId": "subnet-c4434w3y",
                "InstanceId": "eni-42al7ni7",
                "InstanceName": "未命名",
                "InsType": 5,
                "PublicIp": "",
                "PrivateIp": "172.22.32.18,172.22.32.19,172.22.32.21,172.22.32.22,172.22.32.23,172.22.32.24,172.22.32.25,172.22.32.26,172.22.32.27,172.22.32.30,172.22.32.31,172.22.32.33,172.22.32.34,172.22.32.35,172.22.32.37,172.22.32.38,172.22.32.39,172.22.32.40,172.22.32.42,172.22.32.44",
                "PortNum": "",
                "LeakNum": "",
                "VPCName": "",
                "InsSource": "",
                "ResourcePath": [],
                "Server": null
            },
            {
                "AppId": "",
                "Region": "ap-shanghai",
                "RegionKey": "",
                "VpcId": "vpc-d0t6wgo2",
                "SubnetId": "subnet-jy2eionr",
                "InstanceId": "eni-4ueypjdw",
                "InstanceName": "未命名",
                "InsType": 5,
                "PublicIp": "",
                "PrivateIp": "10.8.1.4",
                "PortNum": "",
                "LeakNum": "",
                "VPCName": "",
                "InsSource": "",
                "ResourcePath": [],
                "Server": null
            },
            {
                "AppId": "",
                "Region": "ap-shanghai",
                "RegionKey": "",
                "VpcId": "vpc-8f0zu2cu",
                "SubnetId": "subnet-fiq757rz",
                "InstanceId": "eni-6afui5ze",
                "InstanceName": "fw出口",
                "InsType": 5,
                "PublicIp": "",
                "PrivateIp": "10.0.2.9",
                "PortNum": "",
                "LeakNum": "",
                "VPCName": "",
                "InsSource": "",
                "ResourcePath": [],
                "Server": null
            },
            {
                "AppId": "",
                "Region": "ap-guangzhou",
                "RegionKey": "",
                "VpcId": "vpc-39sc6ru5",
                "SubnetId": "subnet-5bxkdvys",
                "InstanceId": "eni-6gxftgkh",
                "InstanceName": "引流卡",
                "InsType": 5,
                "PublicIp": "",
                "PrivateIp": "10.116.101.27",
                "PortNum": "",
                "LeakNum": "",
                "VPCName": "",
                "InsSource": "",
                "ResourcePath": [],
                "Server": null
            }
        ],
        "RequestId": "4b2b9cd7-a96a-44e2-8e97-ccd67869efa0",
        "Total": 48,
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

