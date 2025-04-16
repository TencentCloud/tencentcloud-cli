**Example 1: 查询源集群消费组列表**



Input: 

```
tccli trocket DescribeSourceClusterGroupList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --TaskId abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 10,
        "Groups": [
            {
                "GroupName": "Test",
                "Remark": "abc",
                "Imported": true,
                "Namespace": "",
                "ImportStatus": "Success"
            }
        ],
        "RequestId": "abc"
    }
}
```

