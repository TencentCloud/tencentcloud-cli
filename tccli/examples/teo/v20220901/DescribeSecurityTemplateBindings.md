**Example 1: 查询策略模板的绑定关系**

此方法会输出策略模板的全部绑定关系，包括：
1）已经生效的绑定关系，标注的 “Status” 为 “online”；
2）正在绑定的绑定关系，标注的 “Status” 为 “pending”。
注意：一个域名可能在绑定关系列表中，出现多次，同时标记为多个状态。

例如：查询 example.com 站点（zone ID 为 zone-fdsjjkfsda）下，策略模板 "生产环境策略" （SecurityTemplate ID 为 temp-fjsoelx）的绑定关系，可以参考以下示例进行查询。


注意：输出示例中包含正在绑定 和绑定失败的绑定关系，策略模板已对该二域名生效。其中，abc.example.com 已绑定至入参指定的策略模板，策略正常生效，因此该绑定关系展示为 online 状态；xyz.example.com 正在被重新绑定至其他策略模板，但是尚未完成绑定，当前策略模板仍然生效，因此同时出现在已经生效和正在绑定的绑定关系列表中。


Input: 

```
tccli teo DescribeSecurityTemplateBindings --cli-unfold-argument  \
    --ZoneId zone-fdsjjkfsda \
    --TemplateId temp-fjsoelx
```

Output: 
```
{
    "Response": {
        "SecurityTemplate": [
            {
                "TemplateId": "temp-fjsoelx",
                "TemplateScope": [
                    {
                        "ZoneId": "zone-fdsjjkfsda",
                        "EntityStatus": [
                            {
                                "Entity": "abc.example.com",
                                "Status": "online",
                                "Message": ""
                            },
                            {
                                "Entity": "xyz.example.com",
                                "Status": "online",
                                "Message": ""
                            },
                            {
                                "Entity": "xyz.example.com",
                                "Status": "pending",
                                "Message": ""
                            }
                        ]
                    }
                ]
            }
        ],
        "RequestId": "17d437bc-13a9-49bb-a6ac"
    }
}
```

