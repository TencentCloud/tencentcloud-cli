**Example 1: 获取高危命令规则列表**



Input: 

```
tccli yunjing DescribeBashRules --cli-unfold-argument  \
    --Type 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 85,
        "List": [
            {
                "Id": 1,
                "Uuid": "",
                "Name": "vipw修改shadow文件",
                "Level": 1,
                "Rule": "^(vipw|\\/usr\\/sbin\\/vipw)\\s+-+s",
                "Decription": "通过vipw修改shadow文件, 例：vipw -s",
                "Operator": "admin",
                "IsGlobal": 0,
                "Status": 0,
                "CreateTime": "2019-08-12 00:00:00",
                "ModifyTime": "2019-08-12 00:00:00"
            }
        ],
        "RequestId": "b12a5e5a-9393-453f-a4d9-b42de0b2bcec"
    }
}
```

