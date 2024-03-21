**Example 1: 批量检查白名单**



Input: 

```
tccli account BatchCheckWhitelist --cli-unfold-argument  \
    --WhitelistKeyList xxxx xxxx \
    --WhitelistUinList 1234567 12345678
```

Output: 
```
{
    "Response": {
        "MatchedWhitelist": [
            {
                "WhitelistKey": "testKey",
                "WhitelistUinList": [
                    "1234567",
                    "12345678"
                ]
            },
            {
                "WhitelistKey": "xxxx",
                "WhitelistUinList": [
                    "1234567",
                    "12345678"
                ]
            }
        ],
        "RequestId": "913ee0a9-dbf0-43ae-99ef-c093be729fce"
    }
}
```

