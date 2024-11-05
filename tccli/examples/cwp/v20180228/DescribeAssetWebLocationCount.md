**Example 1: 获取所有Web站点数量**



Input: 

```
tccli cwp DescribeAssetWebLocationCount --cli-unfold-argument  \
    --Name host1
```

Output: 
```
{
    "Response": {
        "WebLocations": [
            {
                "Key": "key1",
                "Value": 1,
                "Desc": "desc of key1",
                "NewCount": 1
            }
        ],
        "RequestId": "07a92740-5e54-4ea6-9320-c6fc3f3a1121"
    }
}
```

