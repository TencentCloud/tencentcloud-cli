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
                "Value": 0,
                "Key": "xx",
                "Desc": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

