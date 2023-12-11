**Example 1: 获取实例列表**

获取某个用户下所有的集群列表信息

Input: 

```
tccli cdwdoris DescribeInstances --cli-unfold-argument  \
    --Limit 10 \
    --SearchInstanceName  \
    --SearchInstanceId  \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "InstancesList": [
            {
                "RegionId": 1,
                "AccessInfo": "xx",
                "Monitor": "xx",
                "Zone": "xx",
                "ClsLogSetId": "xx",
                "Version": "xx",
                "RenewFlag": true,
                "HA": "xx",
                "Status": "xx",
                "EnableXMLConfig": 0,
                "CosMoveFactor": 0,
                "VpcId": "xx",
                "Tags": [
                    {
                        "TagKey": "xx",
                        "TagValue": "xx"
                    }
                ],
                "InstanceId": "xx",
                "MasterSummary": {
                    "DiskDesc": "xx",
                    "Core": 4,
                    "DiskType": "xx",
                    "AttachCBSSpec": {
                        "DiskDesc": "xx",
                        "DiskSize": 0,
                        "DiskCount": 0,
                        "DiskType": "xx"
                    },
                    "Memory": 8,
                    "Disk": 1000,
                    "Spec": "xx",
                    "NodeSize": 2
                },
                "SubnetId": "xx",
                "HasClsTopic": true,
                "Eip": "xx",
                "Kind": "xx",
                "FlowMsg": "xx",
                "ClsTopicId": "xx",
                "Region": "xx",
                "PayMode": "xx",
                "StatusDesc": "xx",
                "InstanceName": "xx",
                "RegionDesc": "xx",
                "ZoneDesc": "xx",
                "CreateTime": "xx",
                "ExpireTime": "xx",
                "Id": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

