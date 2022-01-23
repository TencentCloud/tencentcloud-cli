**Example 1: 获取地址模板列表示例**



Input: 

```
tccli cfw DescribeAddrTemplateList --cli-unfold-argument  \
    --SearchValue xx \
    --By xx \
    --Limit 0 \
    --Order xx \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Data": [
            {
                "Uuid": "mb_123456",
                "Name": "数据库白名单",
                "Detail": "test",
                "IpString": "0.0.0.0",
                "InsertTime": "xxxxxx",
                "UpdateTime": "xxxxxx",
                "Type": 1,
                "RulesNum": 1
            }
        ],
        "NameList": [
            "xxxxxx"
        ],
        "RequestId": "18ab90ea-b199-42c8-90bc-e3fd08027625"
    }
}
```

