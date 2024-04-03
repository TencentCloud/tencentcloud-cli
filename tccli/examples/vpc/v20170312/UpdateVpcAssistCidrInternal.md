**Example 1: demo**



Input: 

```
tccli vpc UpdateVpcAssistCidrInternal --cli-unfold-argument  \
    --VpcCidrSet.0.Subnet 10.4.0.0 \
    --VpcCidrSet.0.VpcId 16769060 \
    --VpcCidrSet.0.OperationRouteToVbcFlag 1 \
    --VpcCidrSet.0.IntMask 16 \
    --VpcCidrSet.0.Owner 251197522 \
    --VpcCidrSet.0.UniqueVpcId vpc-7zayowkt
```

Output: 
```
{
    "Response": {
        "VpcCidrSet": [
            {
                "VpcId": 16769060,
                "UniqueVpcId": "vpc-7zayowkt",
                "VpcSubnet": "10.0.0.0",
                "VpgId": 53786,
                "ZoneVpgFlag": 0,
                "OldPublishVpgFlag": 1,
                "Owner": "251197522",
                "AssistType": 0,
                "Subnet": "10.4.0.0",
                "NewAfcFlag": 1,
                "Mask": "255.255.0.0",
                "CreateTime": "2021-05-17 19:55:20",
                "OwnedFlag": 0,
                "VpcIntMask": 16,
                "OldOperationRouteToVbcFlag": 1,
                "IntMask": 16,
                "OperationRouteToVbcFlag": 1,
                "VpcAssistCidrId": 22811
            }
        ],
        "RequestId": "0ad42d3d-cfee-4c4e-b01e-d0b4f3d9d871"
    }
}
```

**Example 2: 用于更新vpc的辅助CIDR**



Input: 

```
tccli vpc UpdateVpcAssistCidrInternal --cli-unfold-argument  \
    --VpcCidrSet.0.Subnet 172.16.0.0 \
    --VpcCidrSet.0.VpcId 78257 \
    --VpcCidrSet.0.OperationRouteToVbcFlag 1 \
    --VpcCidrSet.0.IntMask 20 \
    --VpcCidrSet.0.Owner 251198225 \
    --VpcCidrSet.0.UniqueVpcId vpc-fjknwrrj
```

Output: 
```
{
    "Response": {
        "VpcCidrSet": [
            {
                "VpcId": 78257,
                "UniqueVpcId": "vpc-fjknwrrj",
                "Owner": "251198225",
                "Subnet": "172.16.0.0",
                "IntMask": 20,
                "OperationRouteToVbcFlag": 1
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

