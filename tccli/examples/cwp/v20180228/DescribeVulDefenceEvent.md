**Example 1: 获取漏洞防御事件列表**



Input: 

```
tccli cwp DescribeVulDefenceEvent --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "Count": 0,
                "City": "xx",
                "CveId": "xx",
                "VulName": "xx",
                "EventType": 1,
                "Status": 0,
                "PublicIp": "xx",
                "Alias": "xx",
                "CreateTime": "xx",
                "Quuid": "xx",
                "MergeTime": "xx",
                "VulId": 1,
                "SourcePort": [
                    1
                ],
                "PrivateIp": "xx",
                "SourceIp": "xx",
                "Id": 0
            }
        ],
        "RequestId": "xx"
    }
}
```

