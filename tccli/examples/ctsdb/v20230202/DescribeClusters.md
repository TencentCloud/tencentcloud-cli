**Example 1: 查询实例列表**

查询实例列表

Input: 

```
tccli ctsdb DescribeClusters --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 10 \
    --Filters.0.Name cluster_id \
    --Filters.0.Op = \
    --Filters.0.Values ctsdbi-xxxxxxx \
    --Orders.0.Name created_at \
    --Orders.0.Type DESC
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Clusters": [
            {
                "AppID": 123456789,
                "ClusterID": "ctsdbi-xxxxxxx",
                "AccountID": "xxxxxx==",
                "Name": "测试实例",
                "Region": "guangzhou",
                "Zones": "guangzhou-3",
                "Networks": [
                    {
                        "VIP": "10.0.0.x",
                        "Port": 8086,
                        "VpcId": "332211",
                        "SubnetId": "55321"
                    }
                ],
                "Spec": {
                    "RequestUnit": 1,
                    "PayMode": 1,
                    "CpuLimit": 1,
                    "MemoryLimit": 4,
                    "DiskLimit": 100,
                    "Shards": 3,
                    "Replicas": 1
                },
                "Status": 1,
                "Period": {
                    "StartTime": "2020-09-22T00:00:00+00:00",
                    "EndTime": "2020-09-22T00:00:00+00:00"
                },
                "CreatedAt": "2020-09-22T00:00:00+00:00",
                "UpdatedAt": "2020-09-22T00:00:00+00:00",
                "Tenant": {},
                "Tags": [
                    {
                        "Key": "test",
                        "Value": "示例"
                    }
                ],
                "Security": [
                    "test"
                ]
            }
        ],
        "RequestId": "requestxxxxxxxxxx"
    }
}
```

