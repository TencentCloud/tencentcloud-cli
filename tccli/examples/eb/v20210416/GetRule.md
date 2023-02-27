**Example 1: 获取规则详情**

获取规则详情

Input: 

```
tccli eb GetRule --cli-unfold-argument  \
    --EventBusId eb-l65vlc2 \
    --RuleId rule-qr2wsqqy
```

Output: 
```
{
    "Response": {
        "AddTime": "2021-04-29T20:01:27+08:00",
        "Description": "",
        "Enable": true,
        "EventBusId": "eb-l65vlc2u",
        "EventPattern": "{\"data\":{\"prefix\":[\"1\",\"2\"]}}",
        "ModTime": "2021-04-29T20:01:28+08:00",
        "RequestId": "9babdbaf-85d9-4d79-8eb7-14fd989cf99a",
        "RuleId": "rule-qr2wsqqy",
        "RuleName": "test",
        "Status": "Active"
    }
}
```

