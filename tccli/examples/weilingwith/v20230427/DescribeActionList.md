**Example 1: 获取动作列表**

成功响应

Input: 

```
tccli weilingwith DescribeActionList --cli-unfold-argument  \
    --WorkspaceId 1016 \
    --PageNumber 1 \
    --PageSize 1 \
    --ApplicationToken baSTzPx0vZ6LPuv2EifNa5CqRBj9hoY0
```

Output: 
```
{
    "Response": {
        "RequestId": "1c116023-0562-4488-933e-84df17c7f08c",
        "Result": {
            "ActionDetailSet": [
                {
                    "ActionDesc": "lena测试控制开灯",
                    "ActionType": "deviceControl",
                    "CreateTime": "2023-05-15 16:29:17",
                    "Id": 22,
                    "LinkRuleSet": [],
                    "MsgContent": "x-json:[{\"model\":\"红灯(red)\",\"value\":\"10\",\"obj\":{\"name\":\"红灯\",\"type\":\"int\",\"modelName\":\"智能灯控模块\",\"modelId\":\"2000126\",\"define\":{\"type\":\"int\",\"min\":0,\"max\":255},\"options\":[]},\"type\":\"int\"},{\"model\":\"绿灯(green)\",\"value\":\"10\",\"type\":\"int\",\"obj\":{\"name\":\"绿灯\",\"type\":\"int\",\"modelName\":\"智能灯控模块\",\"modelId\":\"2000126\",\"define\":{\"type\":\"int\",\"min\":0,\"max\":255},\"options\":[]}}]",
                    "MsgType": "model",
                    "Name": "lena测试控制开灯",
                    "SinkConfig": "x-json:{\"nearbySearch\":{\"deviceType\":\"w0905001\",\"pid\":2000126,\"limit\":0,\"objectLevel\":0,\"scopeLevel\":\"\",\"scopeRadius\":\"\",\"deviceAssign\":\"deviceType\"}}",
                    "WID": ""
                }
            ],
            "PageNumber": 1,
            "PageSize": 1,
            "TotalPage": 158,
            "TotalRow": 158
        }
    }
}
```

