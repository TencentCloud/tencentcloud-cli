**Example 1: 查询数据多写**



Input: 

```
tccli monitor DescribeRemoteWrites --cli-unfold-argument  \
    --InstanceId prom-abcd
```

Output: 
```
{
    "Response": {
        "RemoteWrites": [
            {
                "Destination": "multipe-1"
            }
        ],
        "Count": 1,
        "RequestId": "bfa18d10-fe18-4f0e-b7e8-18857f951655"
    }
}
```

