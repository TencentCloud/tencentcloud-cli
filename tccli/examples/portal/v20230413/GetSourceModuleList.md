**Example 1: 查询现有引用记录中链接所属的所有模块和id的对应关系**

野鹤关联页面查询-引用记录-模块栏

Input: 

```
tccli portal GetSourceModuleList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ModuleList": [
            {
                "SourceModuleName": "解决方案",
                "SourceModuleType": 10
            },
            {
                "SourceModuleName": "产品介绍页",
                "SourceModuleType": 20
            },
            {
                "SourceModuleName": "客户案例",
                "SourceModuleType": 30
            },
            {
                "SourceModuleName": "控制台",
                "SourceModuleType": 40
            },
            {
                "SourceModuleName": "文档中心",
                "SourceModuleType": 50
            },
            {
                "SourceModuleName": "私有云文档",
                "SourceModuleType": 60
            },
            {
                "SourceModuleName": "购买页",
                "SourceModuleType": 70
            },
            {
                "SourceModuleName": "活动运营",
                "SourceModuleType": 80
            },
            {
                "SourceModuleName": "开发者社区",
                "SourceModuleType": 100
            },
            {
                "SourceModuleName": "课堂",
                "SourceModuleType": 110
            },
            {
                "SourceModuleName": "其他",
                "SourceModuleType": 120
            }
        ],
        "RequestId": "88110dd9-8bbf-470f-b2e6-48edf52d9cc9"
    }
}
```

