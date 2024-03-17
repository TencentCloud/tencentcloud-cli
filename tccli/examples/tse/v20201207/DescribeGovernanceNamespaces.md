**Example 1: 查询治理中心命名空间列表**



Input: 

```
tccli tse DescribeGovernanceNamespaces --cli-unfold-argument  \
    --Name abc \
    --Offset 1 \
    --Limit 1 \
    --InstanceId abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Content": [
            {
                "Name": "abc",
                "Comment": "abc",
                "CreateTime": "abc",
                "ModifyTime": "abc",
                "TotalServiceCount": 0,
                "TotalHealthInstanceCount": 0,
                "TotalInstanceCount": 0,
                "Id": "abc",
                "Editable": true
            }
        ],
        "RequestId": "abc"
    }
}
```

