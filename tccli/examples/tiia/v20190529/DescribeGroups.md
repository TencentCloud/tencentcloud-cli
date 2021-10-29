**Example 1: 调用成功示例**



Input: 

```
tccli tiia DescribeGroups --cli-unfold-argument  \
    --Offset 0 \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "Groups": [
            {
                "GroupType": 1,
                "MaxQps": 1,
                "UpdateTime": 1,
                "Brief": "xx",
                "GroupName": "xx",
                "PicCount": 1,
                "GroupId": "xx",
                "CreateTime": 1,
                "MaxCapacity": 1
            }
        ]
    }
}
```

