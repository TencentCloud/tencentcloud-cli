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
                "Uuid": "d4cc302e-09e5-436f-b99b-5ab9c9070323",
                "IsGlobal": false,
                "Quuid": "d4cc302e-09e5-436f-b99b-5ab9c9070323",
                "MachineIp": "1.1.1.1",
                "MachineName": "name******"
            }
        ],
        "RequestId": "aad8005f-2bf2-8b79-cfde-b030576f886e"
    }
}
```

