**Example 1: 查询Dspm资产列表**



Input: 

```
tccli csip DescribeDspmAssets --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AssetSet": [
            {
                "AssetId": "cdb-c2thbt00",
                "AssetType": "cdb",
                "AccountCount": 0,
                "Name": "测试cdb",
                "PublicIp": "1.1.1.1:3306",
                "PrivateIp": "192.168.0.1:3306",
                "WanDomain": "gz-cdb-c2thbt00.sql.tencentcdb.com:3306",
                "Region": "ap-guangzhou",
                "VpcId": "vpc-c2thbt00",
                "VpcName": "default-vpc",
                "SubnetId": "subnet-c2thbt00",
                "SubnetName": "default-subnet",
                "Status": 0,
                "CreateTime": "2025-01-20 18:51:00"
            }
        ],
        "RequestId": "cf839eee-b651-4ff3-9b49-173f9f55733f"
    }
}
```

