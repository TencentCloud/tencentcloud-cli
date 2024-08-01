**Example 1: 获取各地域列表**

集群列表页上显示地域信息及各个地域的集群总数

Input: 

```
tccli cdwdoris DescribeAreaRegion --cli-unfold-argument ```

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
        "FrontEndRules": [
            {
                "ID": 0,
                "Name": "abc",
                "Rule": "abc"
            }
        ],
        "AvailableWhiteListNames": [
            "abc"
        ],
        "RequestId": "abc"
    }
}
```

