**Example 1: 集群列表new**

集群列表

Input: 

```
tccli cdwpg DescribeSimpleInstances --cli-unfold-argument  \
    --SearchInstanceId dabc \
    --SearchInstanceName dabc \
    --Offset 0 \
    --Limit 0 \
    --SearchTags dabc
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "InstancesList": [
            {
                "ID": 0,
                "InstanceId": "dabc",
                "InstanceName": "dabc",
                "Version": "dabc",
                "Region": "dabc",
                "RegionId": 0,
                "RegionDesc": "adbc",
                "Zone": "abdc",
                "ZoneId": 0,
                "ZoneDesc": "abdc",
                "VpcId": "abdc",
                "SubnetId": "abdc",
                "CreateTime": "abdc",
                "ExpireTime": "abdc",
                "AccessInfo": "adbc",
                "PayMode": "abdc",
                "RenewFlag": true
            }
        ],
        "ErrorMsg": "",
        "RequestId": "abcdd"
    }
}
```

