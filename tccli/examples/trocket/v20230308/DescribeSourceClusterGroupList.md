**Example 1: 查询源集群消费组列表**



Input: 

```
tccli trocket DescribeSourceClusterGroupList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --TaskId 02f6c31a-9707-4244-8dd3-35ad868ef92a
```

Output: 
```
{
    "Response": {
        "TotalCount": 10,
        "Groups": [
            {
                "GroupName": "Test",
                "Remark": "remark",
                "Imported": true,
                "Namespace": "",
                "ImportStatus": "Success"
            }
        ],
        "RequestId": "02f6c31a-9707-4244-8dd3-35ad868ef92a"
    }
}
```

