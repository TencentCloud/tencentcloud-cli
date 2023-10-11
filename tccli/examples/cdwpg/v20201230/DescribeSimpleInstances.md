**Example 1: 集群列表new**

集群列表

Input: 

```
tccli cdwpg DescribeSimpleInstances --cli-unfold-argument  \
    --SearchInstanceId abc \
    --SearchInstanceName abc \
    --Offset 0 \
    --Limit 0 \
    --SearchTags abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "InstancesList": [
            {
                "ID": 0,
                "InstanceId": "abc",
                "InstanceName": "abc",
                "Version": "abc",
                "Region": "abc",
                "RegionId": 0,
                "RegionDesc": "abc",
                "Zone": "abc",
                "ZoneId": 0,
                "ZoneDesc": "abc",
                "VpcId": "abc",
                "SubnetId": "abc",
                "CreateTime": "abc",
                "ExpireTime": "abc",
                "AccessInfo": "abc",
                "PayMode": "abc",
                "RenewFlag": true
            }
        ],
        "ErrorMsg": "abc",
        "RequestId": "abc"
    }
}
```

