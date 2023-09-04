**Example 1: 联动详情**

成功响应

Input: 

```
tccli weilingwith DescribeRuleDetail --cli-unfold-argument  \
    --WorkspaceId 1016 \
    --Id 29 \
    --ApplicationToken baSTzPx0vZ6LPuv2EifNa5CqRBj9hoY0
```

Output: 
```
{
    "Response": {
        "RequestId": "6e77c453-636c-43db-97d8-aa7fac74f37b",
        "Result": {
            "ActionInfoSet": [
                {
                    "ApplyDevice": "",
                    "CreateTime": "2023-05-23 14:38:13",
                    "Desc": "事件范围内同一建筑",
                    "Id": 71,
                    "MsgContent": "x-json:",
                    "MsgType": "origin",
                    "Name": "事件范围内同一建筑",
                    "SinkConfig": "x-json:{\"nearbySearch\":{\"deviceType\":\"w0201001\",\"pid\":0,\"limit\":2,\"objectLevel\":9,\"scopeLevel\":\"6\",\"scopeRadius\":\"100\",\"deviceAssign\":\"deviceType\"}}",
                    "Type": "nearbyDevices"
                }
            ],
            "BeginDate": "",
            "EndDate": "",
            "EventInfoSet": [
                {
                    "Condition": "x-json:[{\"type\":\"objmodel\",\"attr\":\"properties.idtest\",\"oper\":\"=\",\"val\":\"348\",\"obj\":{\"id\":\"idtest\",\"name\":\"idtest\",\"type\":\"int\",\"modelName\":\"网关设备_直连类型\",\"modelId\":\"2000085\",\"define\":{\"type\":\"int\"}},\"valType\":0,\"otherObj\":\"\"}]",
                    "Id": 36,
                    "Name": "具体设备",
                    "Type": "device"
                }
            ],
            "EventRule": "36",
            "RuleDesc": "联动同一建筑",
            "RuleId": 29,
            "RuleName": "联动同一建筑332",
            "Status": 0,
            "ValidPeriod": "x-json:",
            "ValidType": 1
        }
    }
}
```

