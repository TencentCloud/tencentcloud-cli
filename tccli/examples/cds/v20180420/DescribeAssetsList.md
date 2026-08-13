**Example 1: 查看当前的资产**



Input: 

```
tccli cds DescribeAssetsList --cli-unfold-argument  \
    --Limit 4 \
    --Permission -1 \
    --AliveStatus 1
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AddTime": 1783668764,
                "AddType": 2,
                "AgentOn": 0,
                "Aid": 354,
                "AliveStatus": 1,
                "AssetGroupId": 30,
                "AssetGroups": [
                    {
                        "Id": 30,
                        "Name": "测试分组"
                    }
                ],
                "AssetSubnetId": "subnet-490b608i",
                "AssetsAddType": 4,
                "AssetsIp": "1.1.1.1",
                "AssetsName": "11.1.1.1",
                "AssetsPort": 11,
                "AssetsType": "MySQL",
                "AssetsVersion": "",
                "AuditScope": "REGION",
                "Available": "PROXY_OFF",
                "BidirectionAllow": 1,
                "BidirectionDelivery": 0,
                "BidirectionMaxLine": 99,
                "BidirectionMaxStorage": 16,
                "BidirectionOn": 0,
                "CasbOn": 0,
                "CdbErrorMsg": "",
                "CdbOn": 0,
                "DbCharset": "UTF-8",
                "DbPlatform": "64",
                "GroupId": "",
                "GroupName": "测试分组",
                "InstanceGroupId": "",
                "InstanceId": "",
                "InstanceName": "",
                "IsNewCloudAudit": false,
                "OsPolicy": "linux",
                "Permission": 0,
                "RegionId": "ap-guangzhou",
                "RoStatus": "",
                "Status": 1,
                "TrafficMirrorOn": 0,
                "UpdateTime": 1783674156,
                "UploadPem": 0,
                "VpcId": "vpc-4gy7nrkb"
            }
        ],
        "TotalCount": 7,
        "RequestId": "59b1f5e9-99ef-4f54-92f9-bd9aedfc4e34"
    }
}
```

