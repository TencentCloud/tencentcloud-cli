**Example 1: 修改解析记录状态**



Input: 

```
tccli privatedns ModifyRecordsStatus --cli-unfold-argument  \
    --ZoneId zone-mao3y9jo \
    --RecordIds 1 2 3 \
    --Status enabled
```

Output: 
```
{
    "Response": {
        "RequestId": "660006f4-8531-46f0-a2ba-05daf4e7932e",
        "ZoneId": "zone-mao3y9jo",
        "RecordIds": [
            1,
            2,
            3
        ],
        "Status": "enabled"
    }
}
```

