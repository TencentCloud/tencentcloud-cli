**Example 1: 接口测试**

接口测试

Input: 

```
tccli csip DescribeDbAssetInfo --cli-unfold-argument  \
    --AssetId cdb-nbq22l65
```

Output: 
```
{
    "Response": {
        "Data": {
            "AssetId": "cdb-nbq22l65",
            "AssetName": "cdb379810",
            "AssetType": "MYSQL",
            "CFWProtectLevel": 1,
            "CFWStatus": 1,
            "PrivateIp": "192.168.1.11:3306",
            "PublicIp": "1.1.1.1",
            "Region": "ap-guangzhou",
            "Tag": [
                {
                    "Name": "andy",
                    "Value": "1.214"
                }
            ],
            "VpcId": "vpc-ds7fl5xn",
            "VpcName": "illnggao-01"
        },
        "RequestId": "d5a9e4b1-7007-4b6d-a35b-54ebfd16f8fc"
    }
}
```

