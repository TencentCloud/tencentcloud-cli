**Example 1: 通过只读实例查询只读组**



Input: 

```
tccli sqlserver DescribeReadOnlyGroupByReadOnlyInstance --cli-unfold-argument  \
    --InstanceId mssqlro-91masbl1
```

Output: 
```
{
    "Response": {
        "IsOfflineDelay": 1,
        "MasterInstanceId": "mssql-6f4ddx2f",
        "MasterRegionId": "ap-guangzhou",
        "MinReadOnlyInGroup": 1,
        "ReadOnlyGroupId": "mssqlrg-552tyamb",
        "ReadOnlyGroupName": "再次尝试一次创建2个副本",
        "ReadOnlyMaxDelayTime": 11,
        "RegionId": "ap-guangzhou",
        "RequestId": "798db80b-869b-4a39-a39a-72c52d5bdca4",
        "SubnetId": "subnet-gdy95gfs",
        "Vip": "10.100.0.44",
        "VpcId": "vpc-3xq2t5al",
        "Vport": 1433,
        "ZoneId": "ap-guangzhou-2"
    }
}
```

