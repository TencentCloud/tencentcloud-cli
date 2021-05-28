**Example 1: 获取VSM属性**

获取VSM属性

Input: 

```
tccli cloudhsm DescribeVsmAttributes --cli-unfold-argument  \
    --ResourceId xxxxxxxxxxxx
```

Output: 
```
{
    "Response": {
        "RenewFlag": 1,
        "SubnetName": "xx",
        "VsmType": 17,
        "Status": 1,
        "VpcId": "xx",
        "SgList": [
            {
                "OutBound": [
                    {
                        "Proto": "xx",
                        "Ip": "xx",
                        "Id": "xx",
                        "Action": "xx",
                        "AddressModule": "xx",
                        "ServiceModule": "xx",
                        "Port": "xx",
                        "Desc": "xx"
                    }
                ],
                "InBound": [
                    {
                        "Proto": "xx",
                        "Ip": "xx",
                        "Id": "xx",
                        "Action": "xx",
                        "AddressModule": "xx",
                        "ServiceModule": "xx",
                        "Port": "xx",
                        "Desc": "xx"
                    }
                ],
                "SgName": "xx",
                "Version": 0,
                "SgId": "xx",
                "CreateTime": "xx",
                "SgRemark": "xx"
            }
        ],
        "Tags": [
            {
                "TagKey": "xx",
                "TagValue": "xx"
            }
        ],
        "ResourceId": "xx",
        "RegionId": 1,
        "VpcName": "xx",
        "SubnetId": "xx",
        "ResourceName": "xx",
        "Expired": true,
        "RegionName": "xx",
        "SubnetCidrBlock": "xx",
        "ZoneId": 1,
        "RequestId": "xx",
        "Model": "xx",
        "VpcCidrBlock": "xx",
        "ExpireTime": 1234567890,
        "Vip": "xx",
        "RemainSeconds": 0,
        "ZoneName": "xx",
        "Manufacturer": "xxx"
    }
}
```

