**Example 1: 查询治理中心命名空间列表**



Input: 

```
tccli tse DescribeGovernanceNamespaces --cli-unfold-argument  \
    --Name name \
    --Offset 1 \
    --Limit 1 \
    --InstanceId ins-id
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Content": [
            {
                "Name": "name",
                "Comment": "comment",
                "CreateTime": "2024-10-08 10:00:00",
                "ModifyTime": "2024-10-08 10:00:00",
                "TotalServiceCount": 0,
                "TotalHealthInstanceCount": 0,
                "TotalInstanceCount": 0,
                "Id": "id",
                "Editable": true
            }
        ],
        "RequestId": "req-id"
    }
}
```

