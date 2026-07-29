**Example 1: 批量查询实例信息**

批量查询实例信息

Input: 

```
tccli dbbrain DescribeDBInstances --cli-unfold-argument  \
    --InstanceIds cdb-lvgh1oyv
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "ClusterId": "",
                "CreateTime": "2026-07-06 15:29:00",
                "DeadlineTime": "1970-01-03 00:00:00",
                "EngineVersion": "8.0",
                "InstanceId": "cdb-lvgh1oyv",
                "Product": "MySQL",
                "Region": "ap-guangzhou",
                "Status": 1
            }
        ],
        "RequestId": "dcdd3bd4-8ce8-49a0-82d6-c23482536608"
    }
}
```

