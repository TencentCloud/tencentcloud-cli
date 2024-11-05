**Example 1: 示例**



Input: 

```
tccli cwp DescribeScreenHostInvasion --cli-unfold-argument  \
    --Quuid "1c26308c-5493-4eaf-a817-112ec25f499e"
```

Output: 
```
{
    "Response": {
        "DefendAttackLog": [
            {
                "DstIp": "10.1.1.15",
                "Uuid": "1c26308c-5493-4eaf-a817-112ec25f499e",
                "VulType": "web",
                "SrcPort": 1,
                "HttpMethod": "POST",
                "Quuid": "1c26308c-5493-4eaf-a817-112ec25f499e",
                "CreatedTime": " 2019-12-25 11:57:15",
                "DstPort": 1,
                "Id": 1,
                "SrcIp": "10.1.1.14"
            }
        ],
        "Vul": [
            {
                "Category": 1,
                "Name": "name",
                "Level": 1,
                "VulId": 1,
                "LastTime": " 2019-12-25 11:57:15",
                "Id": 1,
                "Uuid": "1c26308c-5493-4eaf-a817-112ec25f499e"
            }
        ],
        "InvasionEvents": [
            {
                "Uuid": "1c26308c-5493-4eaf-a817-112ec25f499e",
                "Level": 1,
                "EventType": 1,
                "Content": "content",
                "CreatedTime": " 2019-12-25 11:57:15",
                "LevelZh": "level",
                "Id": 1
            }
        ],
        "Baseline": [
            {
                "Uuid": "1c26308c-5493-4eaf-a817-112ec25f499e",
                "Level": 1,
                "LastScanTime": " 2019-12-25 11:57:15",
                "BaselineFailCount": 1,
                "CategoryId": 1,
                "Name": "name"
            }
        ],
        "RequestId": "1c26308c-1af3-4eaf-a817-112ec25f4dfa"
    }
}
```

