**Example 1: 获取阻断白名单列表**



Input: 

```
tccli cwp DescribeBanWhiteList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 4,
        "WhiteList": [
            {
                "Id": "33",
                "SrcIp": "xx.xx.xx.xx",
                "ModifyTime": "2020-02-18 18:28:29",
                "CreateTime": "2020-02-18 18:28:29",
                "Remark": "532",
                "Uuid": "",
                "IsGlobal": false,
                "Quuid": "",
                "MachineIp": "",
                "MachineName": ""
            },
            {
                "Id": "34",
                "SrcIp": "xx.xx.xx.xx",
                "ModifyTime": "2020-03-08 23:27:09",
                "CreateTime": "2020-03-08 23:27:09",
                "Remark": "xxx",
                "Uuid": "",
                "IsGlobal": true,
                "Quuid": "",
                "MachineIp": "",
                "MachineName": ""
            },
            {
                "Id": "35",
                "SrcIp": "xx.xx.xx.xx",
                "ModifyTime": "2020-03-08 23:34:20",
                "CreateTime": "2020-03-08 23:34:20",
                "Remark": "whitelist_rule",
                "Uuid": "",
                "IsGlobal": false,
                "Quuid": "d42129e4-54d3-41af-944c-ec5cfa0ce942",
                "MachineIp": "10.104.135.28",
                "MachineName": ""
            },
            {
                "Id": "36",
                "SrcIp": "xx.xx.xx.xx",
                "ModifyTime": "2020-03-08 23:34:20",
                "CreateTime": "2020-03-08 23:34:20",
                "Remark": "whitelist_rule",
                "Uuid": "",
                "IsGlobal": false,
                "Quuid": "b86925b4-cc36-420e-80d4-5094cb2f094b",
                "MachineIp": "10.104.14.165",
                "MachineName": ""
            }
        ],
        "RequestId": "aad8005f-2bf2-8b79-cfde-b030576f886e"
    }
}
```

