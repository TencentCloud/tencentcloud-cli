**Example 1: 查询复制组信息**

查询实例对应的复制组信息

Input: 

```
tccli redis DescribeReplicationGroupInstance --cli-unfold-argument  \
    --InstanceId crs-a7oxxxxx
```

Output: 
```
{
    "Response": {
        "AppId": 251237400,
        "GroupId": "crs-rpl-oxsincth",
        "GroupName": "test",
        "InstanceRole": "rw",
        "RegionId": 1,
        "RequestId": "02ef9326-3db7-47ab-8f65-c6d1a772f71c"
    }
}
```

