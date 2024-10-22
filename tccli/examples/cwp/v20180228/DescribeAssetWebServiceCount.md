**Example 1: 获取所有Web服务数量**



Input: 

```
tccli cwp DescribeAssetWebServiceCount --cli-unfold-argument  \
    --Name host1
```

Output: 
```
{
    "Response": {
        "WebServices": [
            {
                "Key": "service 1",
                "Value": 10,
                "Desc": "web service 1",
                "NewCount": 0
            }
        ],
        "RequestId": "07a92740-5e54-4ea6-9320-c6fc3f3a1121"
    }
}
```

