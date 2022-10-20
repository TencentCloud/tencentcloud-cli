**Example 1: 查询web应用漏洞列表**



Input: 

```
tccli tcss DescribeWebVulList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "List": [
            {
                "Category": "xx",
                "CVEID": "xx",
                "RegistryImageCount": 0,
                "DefenceScope": "xx",
                "Name": "xx",
                "Level": "xx",
                "CVSSV3Score": 0.0,
                "Tags": [
                    "xx"
                ],
                "FoundTime": "xx",
                "DefenceStatus": "xx",
                "DefendedCount": 0,
                "ContainerCount": 0,
                "PocID": "xx",
                "LocalImageCount": 0,
                "LatestFoundTime": "xx",
                "ID": 0,
                "DefenceHostCount": 0
            }
        ],
        "RequestId": "xx"
    }
}
```

