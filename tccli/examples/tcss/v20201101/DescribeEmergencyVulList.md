**Example 1: 查询应急漏洞列表**



Input: 

```
tccli tcss DescribeEmergencyVulList --cli-unfold-argument  \
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
                "Status": "xx",
                "CVEID": "xx",
                "DefenceScope": "xx",
                "Name": "xx",
                "Level": "xx",
                "CVSSV3Score": 0.0,
                "Tags": [
                    "xx"
                ],
                "DefenceStatus": "xx",
                "SubmitTime": "xx",
                "DefendedCount": 0,
                "PocID": "xx",
                "LatestFoundTime": "xx",
                "ID": 0,
                "DefenceHostCount": 0
            }
        ],
        "RequestId": "xx"
    }
}
```

