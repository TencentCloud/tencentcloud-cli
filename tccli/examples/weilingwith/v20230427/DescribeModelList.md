**Example 1: 物模型列表返回示例**

物模型列表

Input: 

```
tccli weilingwith DescribeModelList --cli-unfold-argument  \
    --WorkspaceId 1016 \
    --PageNumber 1 \
    --PageSize 1 \
    --ApplicationToken YzenL5LdGoxQM5gqJfCCoMDeGqUSsY78
```

Output: 
```
{
    "Response": {
        "RequestId": "934fc559-1b2c-42b4-9bb7-b21dad005d90",
        "Result": {
            "PageNumber": 1,
            "PageSize": 1,
            "Set": [
                {
                    "DeviceType": "w0404024",
                    "DeviceTypeName": "空调温控器",
                    "ModelId": "2000055",
                    "ModelName": "边缘温控器",
                    "ModelParams": "x-json:{\"properties\":[{\"required\":false,\"name\":\"当前温度\",\"id\":\"temperature\",\"mode\":\"rw\",\"desc\":\"\",\"define\":{\"type\":\"double\",\"min\":-30,\"max\":55,\"unit\":\"°C\"},\"order\":1681354602280},{\"required\":false,\"name\":\"设定温度\",\"id\":\"setTemperature\",\"mode\":\"rw\",\"desc\":\"\",\"define\":{\"type\":\"double\",\"min\":16,\"max\":35,\"unit\":\"°C\"},\"order\":1681354625728},{\"required\":false,\"name\":\"运行模式\",\"id\":\"mode\",\"mode\":\"rw\",\"desc\":\"\",\"define\":{\"type\":\"enum\",\"mapping\":{\"0\":\"关闭\",\"1\":\"制冷\",\"2\":\"制热\",\"3\":\"送风\"}},\"order\":1681354654730},{\"required\":false,\"name\":\"风速\",\"id\":\"setWind\",\"mode\":\"rw\",\"desc\":\"\",\"define\":{\"type\":\"enum\",\"mapping\":{\"0\":\"自动\",\"1\":\"1档\",\"2\":\"2档\",\"3\":\"3档\",\"4\":\"4档\",\"5\":\"5档\"}},\"order\":1684390032099,\"level\":1,\"key\":\"properties\",\"parentId\":\"setWind\",\"value\":[],\"type\":\"枚举型\"}],\"services\":[{\"required\":false,\"name\":\"控制\",\"id\":\"control\",\"mode\":\"rw\",\"desc\":\"\",\"define\":{},\"callType\":\"async\",\"inputData\":[{\"required\":false,\"name\":\"设定温度\",\"id\":\"setTemperature\",\"desc\":\"\",\"mode\":\"rw\",\"define\":{\"type\":\"double\"},\"order\":1684292612782},{\"required\":false,\"name\":\"设定运行模式\",\"id\":\"mode\",\"desc\":\"\",\"mode\":\"rw\",\"define\":{\"type\":\"enum\",\"mapping\":{\"0\":\"关闭\",\"1\":\"制冷\",\"2\":\"制热\",\"3\":\"送风\"}},\"order\":1684292898776},{\"required\":false,\"name\":\"设定风速\",\"id\":\"setWind\",\"desc\":\"\",\"mode\":\"rw\",\"define\":{\"type\":\"enum\",\"mapping\":{\"1\":\"1档\",\"2\":\"2档\",\"3\":\"3档\",\"4\":\"4档\",\"5\":\"5档\"}},\"order\":1684292933365}],\"outputData\":[{\"required\":false,\"name\":\"是否成功\",\"id\":\"success\",\"desc\":\"\",\"mode\":\"rw\",\"define\":{\"type\":\"bool\",\"mapping\":{\"0\":\"失败\",\"1\":\"成功\",\"false\":\"失败\",\"true\":\"成功\"}},\"order\":1684292612782},{\"required\":false,\"name\":\"响应码\",\"id\":\"code\",\"desc\":\"\",\"mode\":\"rw\",\"define\":{\"type\":\"int\"},\"order\":1684292665854},{\"required\":false,\"name\":\"错误消息\",\"id\":\"errmsg\",\"desc\":\"\",\"mode\":\"rw\",\"define\":{\"type\":\"string\",\"min\":0,\"max\":9999999},\"order\":1684292770509}],\"level\":1,\"key\":\"services\",\"parentId\":\"control\",\"value1\":[{\"required\":false,\"name\":\"设定温度\",\"id\":\"setTemperature\",\"desc\":\"/\",\"mode\":\"rw\",\"define\":{\"type\":\"double\"},\"order\":1682596793666,\"type\":\"双精度浮点数\",\"key\":\"services\",\"parentId\":\"control\",\"value\":[],\"level\":2}],\"value2\":[{\"required\":false,\"name\":\"是否成功\",\"id\":\"success\",\"desc\":\"/\",\"mode\":\"rw\",\"define\":{\"type\":\"bool\",\"mapping\":{\"0\":\"失败\",\"1\":\"成功\",\"false\":\"失败\",\"true\":\"成功\"}},\"order\":1682596861463,\"type\":\"布尔型\",\"key\":\"services\",\"parentId\":\"control\",\"value\":[],\"level\":2}],\"value\":[{\"required\":false,\"name\":\"设定温度\",\"id\":\"setTemperature\",\"desc\":\"/\",\"mode\":\"rw\",\"define\":{\"type\":\"double\"},\"order\":1682596793666,\"type\":\"双精度浮点数\",\"key\":\"services\",\"parentId\":\"control\",\"value\":[],\"level\":2},{\"required\":false,\"name\":\"是否成功\",\"id\":\"success\",\"desc\":\"/\",\"mode\":\"rw\",\"define\":{\"type\":\"bool\",\"mapping\":{\"0\":\"失败\",\"1\":\"成功\",\"false\":\"失败\",\"true\":\"成功\"}},\"order\":1682596861463,\"type\":\"布尔型\",\"key\":\"services\",\"parentId\":\"control\",\"value\":[],\"level\":2}],\"type\":\"/\"}],\"events\":[{\"required\":false,\"name\":\"高温告警\",\"id\":\"highTemperature\",\"mode\":\"rw\",\"desc\":\"\",\"define\":{},\"properties\":[{\"required\":false,\"name\":\"告警类型\",\"id\":\"eventType\",\"desc\":\"\",\"mode\":\"rw\",\"define\":{\"type\":\"int\"},\"order\":1684378396844},{\"required\":false,\"name\":\"告警时间\",\"id\":\"eventTs\",\"desc\":\"\",\"mode\":\"rw\",\"define\":{\"type\":\"long\"},\"order\":1684378416811},{\"required\":false,\"name\":\"描述\",\"id\":\"describe\",\"desc\":\"\",\"mode\":\"rw\",\"define\":{\"type\":\"string\",\"min\":0,\"max\":100},\"order\":1684378433361},{\"required\":false,\"name\":\"告警等级\",\"id\":\"alarmLevel\",\"desc\":\"\",\"mode\":\"rw\",\"define\":{\"type\":\"int\"},\"order\":1684378459333}],\"type\":\"notify\"},{\"required\":false,\"name\":\"低温告警\",\"id\":\"lowTemperature\",\"mode\":\"rw\",\"desc\":\"\",\"define\":{},\"properties\":[{\"required\":false,\"name\":\"告警类型\",\"id\":\"eventType\",\"desc\":\"\",\"mode\":\"rw\",\"define\":{\"type\":\"int\"},\"order\":1684381625535},{\"required\":false,\"name\":\"告警时间\",\"id\":\"eventTs\",\"desc\":\"\",\"mode\":\"rw\",\"define\":{\"type\":\"long\"},\"order\":1684381625535},{\"required\":false,\"name\":\"描述\",\"id\":\"describe\",\"desc\":\"\",\"mode\":\"rw\",\"define\":{\"type\":\"string\",\"min\":0,\"max\":100},\"order\":1684381625535},{\"required\":false,\"name\":\"告警等级\",\"id\":\"alarmLevel\",\"desc\":\"\",\"mode\":\"rw\",\"define\":{\"type\":\"int\"},\"order\":1684381625535}],\"type\":\"notify\",\"level\":1,\"key\":\"events\",\"parentId\":\"lowTemperature\",\"value\":[{\"required\":false,\"name\":\"告警类型\",\"id\":\"eventType\",\"desc\":\"/\",\"mode\":\"rw\",\"define\":{\"type\":\"int\"},\"order\":1684378396844,\"type\":\"整数型\",\"key\":\"events\",\"parentId\":\"lowTemperature\",\"value\":[],\"level\":2},{\"required\":false,\"name\":\"告警时间\",\"id\":\"eventTs\",\"desc\":\"/\",\"mode\":\"rw\",\"define\":{\"type\":\"long\"},\"order\":1684378416811,\"type\":\"64位长整数\",\"key\":\"events\",\"parentId\":\"lowTemperature\",\"value\":[],\"level\":2},{\"required\":false,\"name\":\"描述\",\"id\":\"describe\",\"desc\":\"/\",\"mode\":\"rw\",\"define\":{\"type\":\"string\",\"min\":0,\"max\":100},\"order\":1684378433361,\"type\":\"字符串\",\"key\":\"events\",\"parentId\":\"lowTemperature\",\"value\":[],\"level\":2},{\"required\":false,\"name\":\"告警等级\",\"id\":\"alarmLevel\",\"desc\":\"/\",\"mode\":\"rw\",\"define\":{\"type\":\"int\",\"min\":\"\",\"max\":\"\"},\"order\":1684378459333,\"type\":\"整数型\",\"key\":\"events\",\"parentId\":\"lowTemperature\",\"value\":[],\"level\":2}]}]}",
                    "ModelType": 1,
                    "RelatedProduct": [
                        {
                            "Id": 2000055,
                            "Name": "边缘温控器"
                        }
                    ],
                    "WorkspaceId": 1016
                }
            ],
            "TotalPage": 156,
            "TotalRow": 156
        }
    }
}
```

