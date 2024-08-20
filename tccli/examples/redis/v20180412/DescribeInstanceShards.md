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
                "ShardName": "abc",
                "ShardId": "abc",
                "Role": 0,
                "Keys": 0,
                "Slots": "abc",
                "Storage": 0,
                "StorageSlope": 0,
                "Runid": "abc",
                "RunId": "abc",
                "Connected": 0
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

