**Example 1: 查询集群信息**

查询集群信息

Input: 

```
tccli cdwpg DescribeInstanceInfo --cli-unfold-argument  \
    --InstanceId abc
```

Output: 
```
{
    "Response": {
        "SimpleInstanceInfo": {
            "ID": 0,
            "InstanceId": "abc",
            "InstanceName": "abc",
            "Version": "abc",
            "Region": "abc",
            "Zone": "abc",
            "UserVPCID": "abc",
            "UserSubnetID": "abc",
            "CreateTime": "abc",
            "ExpireTime": "abc",
            "AccessInfo": "abc",
            "RenewFlag": 0,
            "ChargeProperties": {
                "PayMode": 0,
                "RenewFlag": 0,
                "TimeSpan": 0,
                "TimeUnit": "abc",
                "ChargeType": "abc"
            },
            "Resources": [
                {
                    "SpecName": "abc",
                    "Count": 0,
                    "DiskSpec": {
                        "DiskType": "abc",
                        "DiskSize": 0,
                        "DiskCount": 0
                    },
                    "Type": "abc"
                }
            ],
            "Tags": [
                {
                    "TagKey": "abc",
                    "TagValue": "abc"
                }
            ],
            "Status": 0
        },
        "ErrorMsg": "abc",
        "RequestId": "abc"
    }
}
```

