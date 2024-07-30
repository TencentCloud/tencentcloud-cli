**Example 1: 购买页获取地域及可用区列表**

购买页获取地域及可用区列表、内核版本、网络规则等

Input: 

```
tccli cdwdoris DescribeRegionZone --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "Name": "abc",
                "Desc": "abc",
                "Regions": [
                    {
                        "Name": "abc",
                        "Desc": "abc",
                        "RegionId": 0,
                        "Zones": [
                            {
                                "Name": "abc",
                                "Desc": "abc",
                                "ZoneId": 0,
                                "Encrypt": 0
                            }
                        ],
                        "Count": 0,
                        "IsInternationalSite": 1,
                        "Bucket": "abc"
                    }
                ]
            }
        ],
        "Versions": [
            "abc"
        ],
        "VpcRule": "abc",
        "RequestId": "abc"
    }
}
```

