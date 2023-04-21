**Example 1: 获取拨测节点**

获取拨测节点

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
                "City": "北京",
                "Code": "10001",
                "Name": "123",
                "District": "1223",
                "NetService": "中国电信",
                "Location": 0,
                "Type": 1,
                "IPType": 0,
                "TaskTypes": [
                    1,
                    2
                ],
                "CodeType": ""
            }
        ],
        "RequestId": "123"
    }
}
```

