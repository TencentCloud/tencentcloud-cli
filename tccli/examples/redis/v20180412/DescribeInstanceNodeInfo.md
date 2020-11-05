**Example 1: Sample request**



Input: 

```
tccli redis DescribeInstanceNodeInfo --cli-unfold-argument  \
    --InstanceId crs-asdasdas
```

Output: 
```
{
    "code": 0,
    "msg": "xxx",
    "data": {
        "ProxyCount": 10,
        "RedisCount": 10,
        "Proxy": [
            {
                "NodeId": "6abb7c308ed3d65930599d6f3d978971864cec77"
            }
        ],
        "Redis": [
            {
                "ClusterId": 0,
                "NodeId": "0f2ce0f969c4f43bc338bc1d6f60597d654bb3e4",
                "NodeRole": "slave"
            }
        ]
    }
}
```

