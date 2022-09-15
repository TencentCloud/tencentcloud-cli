**Example 1: demo**



Input: 

```
tccli vpc DescribeVpgListDetailInternal --cli-unfold-argument  \
    --Owner 251197522 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "Total": 2,
        "GetVpgListDetailResult": [
            {
                "VbcId": 0,
                "VpcId": 16769060,
                "UniqueVpcId": "vpc-7zayowkt",
                "PublishDockerCidrFlag": 0,
                "ECMPVpgFlag": 0,
                "VpcDefaultFlag": 0,
                "VpgId": 53786,
                "PublishVbcRouteInNoneIdcSubnetFlag": 1,
                "VpcName": "cissytest",
                "Owner": "251197522",
                "UniqueNatId": "",
                "VpgIp": "9.96.75.194",
                "DnatNum": 0,
                "CasFlag": 0,
                "NatId": 0,
                "RealVpcId": 0,
                "FlowDetailsUpdateTime": "",
                "VpcIntMask": 16,
                "VpcMask": "255.255.0.0",
                "ZoneId": 0,
                "UniqueVpgId": "dcg-5q9vlvpn",
                "VbcDcFlag": 0,
                "SrcNAPTNum": 0,
                "DestNAPTNum": 0,
                "VbcRouteTableType": 0,
                "UniqVbcId": "",
                "NatType": 0,
                "VpcSubnet": "10.0.0.0",
                "ZoneVpgFlag": 0,
                "PublishVbcVpcCidrFlag": 1,
                "BgpFlag": 0,
                "PublishVbcVpcCommunityFlag": 0,
                "BgpVTwoFlag": 0,
                "CreateTime": "2021-12-29 11:50:49",
                "Name": "tsssss",
                "RealUniqVpcId": "",
                "NewAfcFlag": 1,
                "FlowDetailsFlag": 0,
                "VbcFlag": 0,
                "PublishPublicServiceSubnetFlag": 0,
                "BgpVTwoSyncFlag": 0,
                "LocalZoneVpgFlag": 0,
                "SnatNum": 0
            }
        ],
        "RequestId": "c8a814ac-2ed5-49a2-8170-5641eab8e75f"
    }
}
```

