**Example 1: 示例**



Input: 

```
tccli cwp DescribeScreenHostInvasion --cli-unfold-argument  \
    --Quuid "xxx"
```

Output: 
```
{
    "Response": {
        "DefendAttackLog": [
            {
                "DstIp": "xx",
                "Uuid": "xx",
                "VulType": "xx",
                "SrcPort": 1,
                "HttpMethod": "xx",
                "Quuid": "xx",
                "CreatedTime": "xx",
                "DstPort": 1,
                "Id": 1,
                "SrcIp": "xx"
            }
        ],
        "Vul": [
            {
                "Category": 1,
                "Name": "xx",
                "Level": 1,
                "VulId": 1,
                "LastTime": "xx",
                "Id": 1,
                "Uuid": "xx"
            }
        ],
        "InvasionEvents": [
            {
                "Uuid": "xx",
                "Level": 1,
                "EventType": 1,
                "Content": "xx",
                "CreatedTime": "xx",
                "LevelZh": "xx",
                "Id": 1
            }
        ],
        "Baseline": [
            {
                "Uuid": "xx",
                "Level": 1,
                "LastScanTime": "xx",
                "BaselineFailCount": 1,
                "CategoryId": 1,
                "Name": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

