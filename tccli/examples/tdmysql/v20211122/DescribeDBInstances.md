**Example 1: 查询实例列表**



Input: 

```
tccli tdmysql DescribeDBInstances --cli-unfold-argument  \
    --Filters.0.Name Status \
    --Filters.0.Values creating running \
    --Filters.1.Name VpcId \
    --Filters.1.Values vpc-asdfifff \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Instances": [
            {
                "ComputeNodeNum": 2,
                "Region": "ap-guangzhou",
                "Zone": "ap-guangzhou-1",
                "CreateVersion": "RELEASE_R080D001",
                "InitParams": [
                    {
                        "Value": "lower_case_table_names",
                        "Param": "0"
                    }
                ],
                "Status": "running",
                "StatusDesc": "运行中",
                "InstanceId": "tdsql3-f3475547",
                "StorageNodeNum": 3,
                "ResourceTags": [
                    {
                        "TagKey": "tag-key",
                        "TagValue": "tag-value"
                    }
                ],
                "InstanceName": "tdsql3-f3475547",
                "Cpu": 4,
                "VpcId": "vpc-o7ssr1vx",
                "Mem": 8,
                "Vip": "172.16.113.202",
                "SubnetId": "subnet-s21doiba",
                "Vport": 6008,
                "Disk": 200,
                "CreateTime": "2006-01-02 15:04:05"
            }
        ],
        "RequestId": "a93d2900-ef72-11eb-ab93-0716f253da76",
        "TotalCount": 100
    }
}
```

