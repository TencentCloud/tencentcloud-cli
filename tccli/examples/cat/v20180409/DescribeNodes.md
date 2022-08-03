**Example 1: 获取拨测节点**



Input: 

```
tccli cat DescribeNodes --cli-unfold-argument  \
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
                "IPType": 0,
                "TaskTypes": [
                    1,
                    2
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

