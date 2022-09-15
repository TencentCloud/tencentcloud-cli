**Example 1: 添加endpoint**



Input: 

```
tccli vpc CreateEndPointInternal --cli-unfold-argument  \
    --AddEndPointSet.0.ServiceType 1 \
    --AddEndPointSet.0.VpcId 1 \
    --AddEndPointSet.0.Name test \
    --AddEndPointSet.0.ServiceVip 1.1.1.1 \
    --AddEndPointSet.0.Owner 123123 \
    --AddEndPointSet.0.SubnetId 123123
```

Output: 
```
{
    "Response": {
        "AddEndPointResult": [
            {
                "ServiceVpcId": 0,
                "UniqueServiceVpcId": "vpc_0",
                "VpcId": 16769060,
                "Name": "testt",
                "UniqueVpcId": "vpc-7zayowkt",
                "Vip": "10.0.0.4",
                "ServiceType": 1,
                "Owner": "251197522",
                "ServiceVip": "10.0.0.17",
                "State": 0,
                "UniqueSubnetId": "subnet-1ufvulum",
                "UniqueEndPointId": "vpce-d2cthiv2",
                "CreateTime": "0000-00-00 00:00:00",
                "EndPointId": 1141,
                "SubnetId": 2007467,
                "UniqueEndPointServiceId": "",
                "EndPointServiceId": 0
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

