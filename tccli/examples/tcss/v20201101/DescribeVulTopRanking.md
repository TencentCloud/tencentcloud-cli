**Example 1: 查询漏洞Top排名列表**



Input: 

```
tccli tcss DescribeVulTopRanking --cli-unfold-argument  \
    --CategoryType SYSTEM
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Level": "xx",
                "AffectedImageCount": 0,
                "VulName": "xx",
                "PocID": "xx",
                "AffectedContainerCount": 0,
                "ID": 0
            }
        ],
        "RequestId": "xx"
    }
}
```

