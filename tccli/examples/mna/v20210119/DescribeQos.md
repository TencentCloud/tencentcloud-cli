**Example 1: 获取Qos加速状态**



Input: 

```
tccli mna DescribeQos --cli-unfold-argument  \
    --SessionId abcdefg
```

Output: 
```
{
    "Response": {
        "Status": 1,
        "SrcPublicIpv4": "114.114.114.114",
        "DestIpv4": [
            "8.8.8.8",
            "8.8.8.9"
        ],
        "Duration": 1790,
        "QosMenu": "T100K",
        "RequestId": "xx"
    }
}
```

