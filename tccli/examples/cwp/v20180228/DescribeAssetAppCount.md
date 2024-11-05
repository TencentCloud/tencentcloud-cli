**Example 1: 获取所有软件应用数量**



Input: 

```
tccli cwp DescribeAssetAppCount --cli-unfold-argument  \
    --Name host1
```

Output: 
```
{
    "Response": {
        "Apps": [
            {
                "Key": "key1",
                "Value": 10,
                "Desc": "desc of key1",
                "NewCount": 0
            }
        ],
        "RequestId": "07a92740-5e54-4ea6-9320-c6fc3f3a1121"
    }
}
```

