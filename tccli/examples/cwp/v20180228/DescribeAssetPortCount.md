**Example 1: 获取所有端口数量**



Input: 

```
tccli cwp DescribeAssetPortCount --cli-unfold-argument  \
    --Port 1
```

Output: 
```
{
    "Response": {
        "Ports": [
            {
                "Value": 101,
                "Key": "value1",
                "Desc": "",
                "NewCount": 0
            }
        ],
        "RequestId": "24c9be55-c743-4a75-a5c7-2a2912341234"
    }
}
```

