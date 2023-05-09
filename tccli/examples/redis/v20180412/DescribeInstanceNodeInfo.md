**Example 1: 请求示例**

查询节点信息

Input: 

```
tccli redis DescribeInstanceNodeInfo --cli-unfold-argument  \
    --InstanceId crs-asdasdas
```

Output: 
```
{
    "Response": {
        "ProxyCount": 0,
        "Proxy": [
            {
                "NodeId": "abc",
                "ZoneId": 0
            }
        ],
        "RedisCount": 0,
        "Redis": [
            {
                "NodeId": "abc",
                "NodeRole": "abc",
                "ClusterId": 0,
                "ZoneId": 0
            }
        ],
        "TendisCount": 0,
        "Tendis": [
            {
                "NodeId": "abc",
                "NodeRole": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

