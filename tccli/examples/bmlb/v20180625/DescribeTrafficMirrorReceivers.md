**Example 1: 获取指定流量镜像实例的接收机信息**



Input: 

```
tccli bmlb DescribeTrafficMirrorReceivers --cli-unfold-argument  \
    --TrafficMirrorId bmtm-lmep0eit
```

Output: 
```
{
    "Response": {
        "ReceiverSet": [
            {
                "InstanceId": "cpm-2nb0vrdg",
                "Port": 5555,
                "Weight": 10,
                "TrafficMirrorId": "bmtm-0kqtrblv",
                "Alias": "os测试",
                "LanIp": "10.77.0.14",
                "SubnetId": "subnet-db11iptc",
                "SubnetName": "test",
                "SubnetCidrBlock": "10.77.0.0/24",
                "VpcId": "vpc-ndg53v71",
                "VpcName": "test",
                "VpcCidrBlock": "10.77.0.0/16",
                "HealthStatus": "--"
            }
        ],
        "TotalCount": 1,
        "RequestId": "9a50068d-802c-4617-bc8b-ac21579bdb21"
    }
}
```

