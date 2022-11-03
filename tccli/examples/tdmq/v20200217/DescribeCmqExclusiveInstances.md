**Example 1: 查询列表**



Input: 

```
tccli tdmq DescribeCmqExclusiveInstances --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "RequestId": "845c0ef7-60bb-46ed-8251-69e8525d07c7",
        "TotalCount": 2,
        "InstanceSet": [
            {
                "InstanceId": "instance-944b80eb",
                "InstanceName": "test1",
                "InstanceDescription": "cmq",
                "InstanceState": "Creating",
                "InstanceType": "basic",
                "CreatedTime": "0001-01-01T00:00:00Z"
            },
            {
                "InstanceId": "instance-b8787f12",
                "InstanceName": "assssaqw",
                "InstanceDescription": "asdsasadsa",
                "InstanceState": "Creating",
                "InstanceType": "basic",
                "CreatedTime": "0001-01-01T00:00:00Z"
            }
        ]
    }
}
```

