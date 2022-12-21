**Example 1: 描述实例信息**

根据实例ID查询某个实例的具体信息

Input: 

```
tccli cdwch DescribeInstance --cli-unfold-argument  \
    --InstanceId cdwch-12345678
```

Output: 
```
{
    "Response": {
        "InstanceInfo": {
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
                "Memory": 8,
                "Disk": 1000,
                "Spec": "xx",
                "NodeSize": 2
            },
            "SubnetId": "xx",
            "HasClsTopic": true,
            "Eip": "xx",
            "FlowMsg": "xx",
            "ClsTopicId": "xx",
            "Region": "xx",
            "PayMode": "xx",
            "StatusDesc": "xx",
            "InstanceName": "xx",
            "RegionDesc": "xx",
            "CommonSummary": {
                "DiskDesc": "xx",
                "Core": 2,
                "DiskType": "xx",
                "Memory": 4,
                "Disk": 500,
                "Spec": "xx",
                "NodeSize": 1
            },
            "ZoneDesc": "xx",
            "CreateTime": "xx",
            "ExpireTime": "xx",
            "Id": 1
        },
        "RequestId": "xx"
    }
}
```

