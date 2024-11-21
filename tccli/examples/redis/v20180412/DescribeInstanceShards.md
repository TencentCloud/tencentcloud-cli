**Example 1: 请求示例**

获取集群版实例分片信息

Input: 

```
tccli redis DescribeInstanceShards --cli-unfold-argument  \
    --InstanceId crs-7pon**** \
    --FilterSlave True
```

Output: 
```
{
    "Response": {
        "InstanceShards": [
            {
                "Connected": 1,
                "Keys": 0,
                "Role": 0,
                "RunId": "562cbff8e8a393e2d3d7166f764125a37f5cXXX",
                "Runid": "562cbff8e8a393e2d3d7166f764125a37f5cXXX",
                "ShardId": "1",
                "ShardName": "crs-kp52mXXX-001-01",
                "Slots": "[\"0-16383\"]",
                "Storage": 36795120,
                "StorageSlope": 0
            }
        ],
        "RequestId": "06be2b8b-23f4-473f-b0f8-423552ff7XXX",
        "TotalCount": 1
    }
}
```

