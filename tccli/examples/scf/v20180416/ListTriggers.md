**Example 1: 获取函数触发器列表**

获取函数触发器列表

Input: 

```
tccli scf ListTriggers --cli-unfold-argument  \
    --FunctionName function-demo \
    --Limit 2 \
    --Order ASC
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Triggers": [
            {
                "Enable": 1,
                "Qualifier": "$DEFAULT",
                "TriggerName": "hulrzrbh9f",
                "Type": "http",
                "TriggerDesc": "{\"AuthType\":\"NONE\",\"NetConfig\":{\"EnableIntranet\":true,\"IntranetUrl\":\"https://1258888888-hulrzrbh9f.in.ap-chongqing.tencentscf.com\",\"IntranetHTTPUrl\":\"http://1258888888-hulrzrbh9f.in.ap-chongqing.tencentscf.com\",\"ExtranetUrl\":\"\",\"ExtranetHTTPUrl\":\"\",\"WssIntranetUrl\":\"\",\"WsIntranetUrl\":\"\",\"WssExtranetUrl\":\"\",\"WsExtranetUrl\":\"\",\"EnableExtranet\":false}}",
                "AvailableStatus": "Available",
                "CustomArgument": "custom",
                "Description": "Some Description",
                "AddTime": "2020-09-22 00:00:00",
                "ModTime": "2020-09-22 00:00:00",
                "ResourceId": "qcs::scf:cq:uin/888888:function/function-demo/hulrzrbh9f",
                "BindStatus": "on",
                "TriggerAttribute": "single"
            }
        ],
        "RequestId": "52dd00b1-7197-4a11-97f5-2a67f9f49273"
    }
}
```

