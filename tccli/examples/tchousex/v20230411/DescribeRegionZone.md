**Example 1: 地域示例**



Input: 

```
tccli tchousex DescribeRegionZone --cli-unfold-argument  \
    --InstanceType InstanceType
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "Name": "测试",
                "Desc": "测试",
                "Regions": [
                    {
                        "Name": "测试",
                        "Desc": "测试",
                        "RegionID": 0,
                        "Zones": [
                            {
                                "Name": "测试",
                                "Desc": "测试",
                                "ZoneID": 0
                            }
                        ],
                        "Count": 0
                    }
                ]
            }
        ],
        "Versions": [
            "测试"
        ],
        "ErrorMsg": "测试",
        "IsYunti": true,
        "RequestId": "测试"
    }
}
```

