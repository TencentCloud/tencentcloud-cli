**Example 1: 查询集群信息**

查询集群信息

Input: 

```
tccli cdwpg DescribeInstanceInfo --cli-unfold-argument  \
    --InstanceId cdwpg-abc
```

Output: 
```
{
    "Response": {
        "SimpleInstanceInfo": {
            "ID": 0,
            "InstanceId": "cdwpg-abc",
            "InstanceName": "test-abc",
            "Version": "3.16.4.8",
            "Region": "ap-beijing",
            "Zone": "ap-beijing-6",
            "UserVPCID": "abdc",
            "UserSubnetID": "abdc",
            "CreateTime": "2012-12-12 12:12:12",
            "ExpireTime": "2012-12-12 13:12:12",
            "AccessInfo": "--",
            "RenewFlag": 0,
            "ChargeProperties": {
                "PayMode": 0,
                "RenewFlag": 0,
                "TimeSpan": 0,
                "TimeUnit": "--",
                "ChargeType": "--"
            },
            "Resources": [
                {
                    "SpecName": "s4",
                    "Count": 0,
                    "DiskSpec": {
                        "DiskType": "local",
                        "DiskSize": 0,
                        "DiskCount": 0
                    },
                    "Type": "dn"
                }
            ],
            "Tags": [
                {
                    "TagKey": "gd",
                    "TagValue": "fd"
                }
            ],
            "Status": 0
        },
        "ErrorMsg": "",
        "RequestId": "abcss"
    }
}
```

