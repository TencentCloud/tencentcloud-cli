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
                "Name": "name",
                "Desc": "desc",
                "Regions": [
                    {
                        "Name": "name",
                        "Desc": "desc",
                        "RegionId": 0,
                        "Zones": [
                            {
                                "Name": "str",
                                "Desc": "str",
                                "ZoneId": 0,
                                "Encrypt": 0
                            }
                        ],
                        "Count": 0,
                        "IsInternationalSite": 1,
                        "Bucket": "str"
                    }
                ]
            }
        ],
        "FrontEndRules": [
            {
                "ID": 0,
                "Name": "str",
                "Rule": "str"
            }
        ],
        "AvailableWhiteListNames": [
            "str"
        ],
        "RequestId": "str"
    }
}
```

