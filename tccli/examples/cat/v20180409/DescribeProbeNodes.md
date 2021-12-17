**Example 1: 查询拨测节点**



Input: 

```
tccli cat DescribeProbeNodes --cli-unfold-argument  \
    --NodeType 1
```

Output: 
```
{
    "Response": {
        "NodeSet": [
            {
                "City": "xx",
                "Code": "xx",
                "Name": "xx",
                "District": "xx",
                "NetService": "xx",
                "Location": 0,
                "Type": 1,
                "IPType": 0
            }
        ],
        "RequestId": "xx"
    }
}
```

