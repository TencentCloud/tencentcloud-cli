**Example 1: 查询物理机信息**



Input: 

```
tccli bm DescribeDevices --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --VpcId vpc-3c7b2102 \
    --DeviceClassCode PS001v1 \
    --Alias test \
    --VagueIp 88 \
    --DeadlineStartTime '2018-01-01 18:00:00' \
    --DeadlineEndTime '2018-12-01 18:00:00' \
    --AutoRenewFlag 1 \
    --Tags.0.TagKey testkey \
    --Tags.0.TagValues testval
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "DeviceInfoSet": [
            {
                "InstanceId": "tcpm-q0hcvsrn",
                "VpcId": "vpc-3c7b2102",
                "SubnetId": "subnet-et5bm4jl",
                "DeviceStatus": 4,
                "OperateStatus": 1,
                "OsTypeId": 6,
                "RaidId": 2,
                "Alias": "ami-test",
                "AppId": 251000873,
                "Zone": "ap-shanghai-bls-2",
                "WanIp": "",
                "LanIp": "10.188.1.2",
                "DeliverTime": "2017-09-28 01:11:11",
                "Deadline": "2018-10-01 00:00:00",
                "AutoRenewFlag": 1,
                "DeviceClassCode": "PS001v1",
                "CpmPayMode": 2,
                "DhcpIp": "100.81.128.24",
                "VpcName": "BMGZHW-206002",
                "SubnetName": "subnet0",
                "MaintainStatus": "Maintain",
                "MaintainMessage": "有厂商维保服务，可继续使用",
                "VpcCidrBlock": "10.188.0.0/16",
                "SubnetCidrBlock": "10.188.1.0/24",
                "IsLuckyDevice": 0,
                "Tags": [
                    {
                        "TagKey": "testval",
                        "TagValues": [
                            "____TIMI _____",
                            "testval"
                        ]
                    }
                ]
            },
            {
                "InstanceId": "tcpm-nxl2p7t7",
                "VpcId": "vpc-3c7b2102",
                "SubnetId": "subnet-et5bm4jl",
                "DeviceStatus": 4,
                "OperateStatus": 9,
                "OsTypeId": 50,
                "RaidId": 2,
                "Alias": "test用",
                "AppId": 251000873,
                "Zone": "ap-shanghai-bls-2",
                "WanIp": "",
                "LanIp": "10.188.1.6",
                "DeliverTime": "2018-02-08 17:26:01",
                "Deadline": "2018-10-01 00:00:00",
                "AutoRenewFlag": 1,
                "DeviceClassCode": "PS100v1",
                "CpmPayMode": 2,
                "DhcpIp": "100.81.128.22",
                "VpcName": "BMGZHW-206002",
                "MaintainStatus": "Maintain",
                "MaintainMessage": "有厂商维保服务，可继续使用",
                "SubnetName": "subnet0",
                "VpcCidrBlock": "10.188.0.0/16",
                "SubnetCidrBlock": "10.188.1.0/24",
                "IsLuckyDevice": 0,
                "Tags": [
                    {
                        "TagKey": "testval",
                        "TagValues": [
                            "testval"
                        ]
                    }
                ]
            }
        ],
        "RequestId": "7e733b67-48fb-4cbe-99c3-0eb6b81aa759"
    }
}
```

