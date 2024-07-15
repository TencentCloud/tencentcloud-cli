**Example 1: 查询可用区的Host和Host上部署的实例**



Input: 

```
tccli cdz DescribeCloudDedicatedZoneHosts --cli-unfold-argument  \
    --CloudDedicatedZoneID cdz-xxxxxxxx \
    --HostUuids 9e6b54d0-xxxx-xxxx-xxxx-xxxxxxxxxxxx \
    --InstanceIds ins-xxxxxxxx \
    --Offset 1 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "CloudDedicatedZoneHostsInfoSet": [
            {
                "HostUuid": "9e6b54d0-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                "InstancesInfo": [
                    "ins-xxxxxxxx"
                ]
            }
        ],
        "RequestId": "fbea6b85-00bc-4d47-ada9-fc06b3ece766"
    }
}
```

