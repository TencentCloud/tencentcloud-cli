**Example 1: 查询已开通代理的IDC集群**

查询一个已开通专线代理的IDC集群的代理状态信息。

Input: 

```
tccli thpc DescribeClusterDedicatedProxy --cli-unfold-argument  \
    --ClusterId hpc-12345678
```

Output: 
```
{
    "Response": {
        "Enabled": true,
        "EndPointId": "vpce-12345678",
        "EndPointVip": "10.0.0.1",
        "EndPointReady": true,
        "EndPointStatus": "ACTIVE",
        "LastKnownStatus": "ACTIVE",
        "EndPointServiceId": "vpcsvc-xxx",
        "VpcId": "vpc-aaaa1234",
        "SubnetId": "subnet-bbbb5678",
        "CreateTime": "2026-06-01 10:00:00",
        "LastSyncTime": "2026-06-11 14:00:00",
        "RealtimeQueryTime": "2026-06-11 14:56:39",
        "RequestId": "b2ac2379-6453-4eab-8f63-7ade00cb67b0"
    }
}
```

**Example 2: 查询未开通代理的IDC集群**

查询一个未开通专线代理的IDC集群。

Input: 

```
tccli thpc DescribeClusterDedicatedProxy --cli-unfold-argument  \
    --ClusterId hpc-87654321
```

Output: 
```
{
    "Response": {
        "Enabled": false,
        "EndPointReady": false,
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    }
}
```

