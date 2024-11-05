**Example 1: 获取所有Web应用数量**



Input: 

```
tccli cwp DescribeAssetWebAppCount --cli-unfold-argument  \
    --Name host1
```

Output: 
```
{
    "Response": {
        "WebApps": [
            {
                "Key": "php",
                "Value": 1,
                "Desc": "php v1",
                "NewCount": 0
            }
        ],
        "RequestId": "07a92740-5e54-4ea6-9320-c6fc3f3a1121"
    }
}
```

