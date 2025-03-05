**Example 1: 示例**



Input: 

```
tccli cdwpg DescribeInstanceNodes --cli-unfold-argument  \
    --InstanceId cdwpg-xx
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "",
        "InstanceNodes": [
            {
                "NodeIp": "9.0.45.12",
                "NodeType": "cn",
                "NodeId": 0
            }
        ],
        "RequestId": "xdx"
    }
}
```

