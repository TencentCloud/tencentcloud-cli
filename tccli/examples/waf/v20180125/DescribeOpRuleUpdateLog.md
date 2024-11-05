**Example 1: 查询示例**



Input: 

```
tccli waf DescribeOpRuleUpdateLog --cli-unfold-argument  \
    --Offset 1 \
    --Limit 20 \
    --Order asc \
    --Lang cn
```

Output: 
```
{
    "Response": {
        "RequestId": "48636a66-6b11-49c6-6603-b8f0c1428516",
        "Total": 8,
        "List": [
            {
                "Id": "1",
                "LogVersion": "1",
                "Status": 1,
                "Detail": "['1. 新增规则010000004， 防护XXX','2. 修改010000005， 优化正则表达式，减少误报']",
                "Language": "cn",
                "CreateTime": "2020-09-22T00:00:00+00:00",
                "ModifyTime": "2021-11-22T16:16:52+08:00"
            },
            {
                "Id": 33,
                "Status": 1,
                "LogVersion": "1",
                "CreateTime": "2021-11-22T16:28:09+08:00",
                "ModifyTime": "2021-11-22T16:28:09+08:00",
                "Detail": "['1. 新增规则010000004， 防护XXX','2. 修改010000005， 优化正则表达式，减少误报','3. 修改010000006， 修改类型']",
                "Language": "cn"
            }
        ]
    }
}
```

