**Example 1: 获取用户VSM列表**



Input: 

```
tccli cloudhsm DescribeVsms --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --SearchWord xxxxxxx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "VsmList": {
            "ResourceId": "xxxx",
            "ResourceName": "xxxxx",
            "Status": 1,
            "Vip": "1.2.3.4",
            "VpcId": "xxxxx",
            "SubnetId": "xxxxxx",
            "Model": "SJJ1528",
            "VsmType": 17,
            "RegionId": 1,
            "RegionName": "广州",
            "ZoneName": "广州三区",
            "ZoneId": 1,
            "ExpireTime": 1234567890,
            "SgList": [
                {
                    "SgId": "SgIdxxxxx",
                    "SgName": "SgNamexxxxxx"
                }
            ]
        },
        "RequestId": "6010cd3d-a85a-4e00-b37b-22606d017420"
    }
}
```

