**Example 1: 查询EIP列表**



Input: 

```
tccli bmeip DescribeEips --cli-unfold-argument  \
    --SearchKey xx \
    --Status 0 \
    --VpcId xx \
    --ExclusiveTag 0 \
    --BindTypes 0 \
    --AclId xx \
    --EipIds eip-lcwonw3s \
    --PayMode xx \
    --Eips xx \
    --Limit 0 \
    --OrderField xx \
    --Offset 0 \
    --BindAcl 0 \
    --Order 0 \
    --InstanceIds xx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "EipSet": [
            {
                "EipId": "eip-lcwonw3s",
                "EipName": "",
                "Eip": "211.159.194.102",
                "IspId": 5,
                "Status": 2,
                "Arrears": 0,
                "InstanceId": "cpm-9p045zd4",
                "InstanceAlias": "dandan_os测试_ubuntu16.04",
                "FreeAt": "2018-10-25 15:15:32",
                "CreatedAt": "2018-10-25 15:15:18",
                "UpdatedAt": "2018-10-25 16:00:09",
                "FreeSecond": 0,
                "Type": 0,
                "PayMode": "flow",
                "Bandwidth": 512,
                "LatestPayMode": "flow",
                "LatestBandwidth": 512,
                "VpcName": "HEISHI_VPC_勿删",
                "NatId": -1,
                "NatUid": "",
                "VpcIp": "",
                "VpcId": "vpc-bjh0qd20",
                "Exclusive": 0,
                "VpcCidr": "10.1.0.0/16",
                "AclId": "",
                "AclName": "",
                "HInstanceId": "",
                "HInstanceAlias": ""
            }
        ],
        "RequestId": "51369791-7ffa-42b1-9a0e-f21b88d7d68a"
    }
}
```

