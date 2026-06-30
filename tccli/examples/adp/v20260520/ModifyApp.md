**Example 1: ModifyApp**



Input: 

```
tccli adp ModifyApp --cli-unfold-argument  \
    --AppId 2060280711767285184 \
    --SharedKbIdList 2047150542445725376 \
    --UpdateMask.Paths SharedKbIdList
```

Output: 
```
{
    "Response": {
        "AppId": "2060280711767285184",
        "UpdateTime": "1780577116",
        "RequestId": "cbc62228-8e38-407b-a4fd-0362beda69e4"
    }
}
```

