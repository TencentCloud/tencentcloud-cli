**Example 1: 查询账户下私有网络的资源占用情况**



Input: 

```
tccli bmvpc DescribeVpcResource --cli-unfold-argument  \
    --Offset 0 \
    --Limit 2 \
    --OrderField VpcId \
    --OrderDirection desc \
    --Filters.0.Name vpc-name \
    --Filters.0.Values yxvpc1
```

Output: 
```
{
    "Response": {
        "VpcResourceSet": [
            {
                "VpcId": "vpc-rqip228w",
                "VpcName": "yxvpc1",
                "CidrBlock": "10.10.0.0/16",
                "SubnetNum": 1,
                "NatNum": 0,
                "State": "available",
                "MonitorFlag": false,
                "CpmNum": 0,
                "LeaveIpNum": 65512,
                "LbNum": 0,
                "TrafficMirrorNum": 0,
                "EipNum": 0,
                "PlgwNum": 0,
                "PlvpNum": 0,
                "IsOld": false,
                "SslVpnGwNum": 0,
                "VpcPeerNum": 0,
                "IpsecVpnGwNum": 0,
                "CcnServiceNum": 1,
                "CreateTime": "2018-07-13 15:09:36",
                "Zone": "ap-guangzhoutest-blsh3-1"
            }
        ],
        "TotalCount": 1,
        "RequestId": "ecad1294-3131-42d1-b1e2-bbc358834d75"
    }
}
```

