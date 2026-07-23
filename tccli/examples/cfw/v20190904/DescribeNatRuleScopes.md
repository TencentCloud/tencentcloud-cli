**Example 1: 查询NAT规则生效范围列表**

查询NAT规则可选择的生效范围列表

Input: 

```
tccli cfw DescribeNatRuleScopes --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "62a5e0b2-f701-4c36-9075-66da225533d7",
        "ScopeItems": [
            {
                "Scope": "ALL",
                "ScopeDesc": "全局规则"
            },
            {
                "Scope": "ap-shanghai",
                "ScopeDesc": "上海地域"
            },
            {
                "Scope": "ap-guangzhou",
                "ScopeDesc": "广州地域"
            },
            {
                "Scope": "ap-beijing",
                "ScopeDesc": "北京地域"
            },
            {
                "Scope": "cfwnat-84d3440f",
                "ScopeDesc": "[autotest][勿删]自动化测试"
            },
            {
                "Scope": "cfwnat-01debc37",
                "ScopeDesc": "111"
            },
            {
                "Scope": "cfwnat-49f38b8b",
                "ScopeDesc": "测试接入"
            },
            {
                "Scope": "cfwnat-7e170f6b",
                "ScopeDesc": "test"
            }
        ],
        "Total": 8
    }
}
```

