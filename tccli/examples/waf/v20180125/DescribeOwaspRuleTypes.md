**Example 1: 查询规则引擎的规则类型列表**



Input: 

```
tccli waf DescribeOwaspRuleTypes --cli-unfold-argument  \
    --Domain owasp.saas3.testwaf.com
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Action": 0,
                "ActiveRule": 1056,
                "Classification": "XSS攻击",
                "Description": "跨站脚本 (XSS) 攻击是一种注入，其中恶意脚本被注入到其他受信任的网站中。 当攻击者使用 Web 应用程序将恶意代码（通常以浏览器端脚本的形式）发送给不同的最终用户时，就会发生 XSS 攻击。 允许这些攻击成功的缺陷非常普遍，并且发生在 Web 应用程序在其生成的输出中使用来自用户的输入而不对其进行验证或编码的任何地方。 攻击者可以使用 XSS 向毫无戒心的用户发送恶意脚本。 最终用户的浏览器无法知道该脚本不应受信任，并且会执行该脚本。 由于它认为脚本来自可信来源，因此恶意脚本可以访问浏览器保留并与该站点一起使用的任何 cookie、会话令牌或其他敏感信息。 这些脚本甚至可以重写 HTML 页面的内容。",
                "Level": 100,
                "Status": 1,
                "TotalRule": 1320,
                "TypeId": 10000000,
                "TypeName": "XSS攻击"
            }
        ],
        "RequestId": "239d0e9a-c7b1-48af-acda-7237c060362a",
        "Total": 1
    }
}
```

