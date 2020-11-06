**Example 1: 查询设备所在机架**



Input: 

```
tccli bm DescribeDevicePosition --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --VpcId vpc-3c7b2102 \
    --SubnetId subnet-6igdzaix
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "DevicePositionInfoSet": [
            {
                "InstanceId": "tcpm-ewqcmo3n",
                "Zone": "ap-shanghai-bls-2",
                "VpcId": "vpc-3c7b2102",
                "SubnetId": "subnet-6igdzaix",
                "LanIp": "10.88.99.2",
                "Alias": "TMI-vpc跨az购买",
                "RckName": "0302-G03",
                "PosCode": 3,
                "SwitchName": "0302-G01-01/0302-G02-01",
                "DeliverTime": "2018-08-07 18:41:09",
                "Deadline": "2100-01-01 00:00:00"
            }
        ],
        "RequestId": "e324c7c7-7a6f-41e8-a629-f29f4bbe908c"
    }
}
```

