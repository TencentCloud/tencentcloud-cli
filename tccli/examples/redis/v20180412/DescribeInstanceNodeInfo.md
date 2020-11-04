**Example 1: 请求示例**



Input: 

```
tccli redis DescribeInstanceNodeInfo --cli-unfold-argument  \
    --InstanceId crs-asdasdas
```

Output: 
```
{
    "Response": {
        "RequestId": "121d5b40-d2b8-11e9-8c40-ef686158cbd6",
        "ProxyCount": 10,
        "RedisCount": 10,
        "TendisCount": 5,
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
        ],
        "Tendis": [
            {
                "NodeId": "54dc6b83093359783abd2f0b07da61d3",
                "NodeRole": "master"
            }
        ]
    }
}
```

