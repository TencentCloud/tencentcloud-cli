**Example 1: 查看漏洞列表**

查看漏洞列表

Input: 

```
tccli cws DescribeVuls --cli-unfold-argument  \
    --Filters.0.Name Name \
    --Filters.0.Values SQL
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "TotalCount": 10,
        "Vuls": [
            {
                "CreatedAt": "2018-03-24T15:38:31+08:00",
                "Describe": "SQL注入漏洞是一种可能被攻击者通过经过精心构造的请求数据来修改后台SQL查询语句的一种安全威胁。当Web应用程序未对用户输入的数据进行任何处理（如危险字符过滤或者语句过滤），而直接作为SQL语句执行时，SQL注入就发生了。<br/><br/>SQL注入漏洞是目前互联网最常见也是影响非常广泛的漏洞。从2007年下半年开始，很多网站被篡改。攻击者利用SQL注入漏洞修改了用于生成动态网页的数据库中的文本，从而注入了恶意的HTML script标签。这样的攻击在2008年第一季度开始加速传播，并且持续影响有漏洞的Web程序。",
                "From": "OWASP:<a target=_blank href=\"https://www.owasp.org/index.php/SQL_Injection\">SQL Injection</a>    WASC:<a target=_blank href=http://projects.webappsec.org/SQL-Injection>SQL Injection</a>    CVE:不适用    CWE:<a target=_blank href=http://cwe.mitre.org/data/definitions/89.html>89</a>",
                "Harm": "数据泄漏-SQL注入漏洞可导致如下后果：<br/>1.机密数据被窃取<br/>2.核心业务数据被篡改<br/>3.网页被篡改<br/>4.数据库所在服务器被攻击变为傀儡主机，甚至企业网被入侵。",
                "Html": "<a target=_blank href=\"http://demo.aisec.cn:80/demo/aisec/ajax_link.php?t=0.2553907226758148&id=1-0\">http://demo.aisec.cn:80/demo/aisec/ajax_link.php?t=0.2553907226758148&id=1-0</a>\n<br><br>[Database Version:MYSQL]: <a target=_blank href=\"http://demo.aisec.cn:80/demo/aisec/ajax_link.php?t=0.2553907226758148&id=1-ROW_COUNT%28%29-%28-ROW_COUNT%28%29%29\">http://demo.aisec.cn:80/demo/aisec/ajax_link.php?t=0.2553907226758148&id=1-ROW_COUNT%28%29-%28-ROW_COUNT%28%29%29</a>\n<br><br>[Inject SELECT Statement:Success]: <a target=_blank href=\"http://demo.aisec.cn:80/demo/aisec/ajax_link.php?t=0.2553907226758148&id=1-%28%09select%090%09%29\">http://demo.aisec.cn:80/demo/aisec/ajax_link.php?t=0.2553907226758148&id=1-%28%09select%090%09%29</a>",
                "Id": 13,
                "Level": "high",
                "Name": "SQL Injection",
                "Nickname": "数据泄漏-SQL注入漏洞",
                "Parameter": "id",
                "SiteId": 1,
                "Solution": "如下一些方法能够防止注入攻击：<br/>1.在网页代码中需要对用户输入的数据进行严格过滤。<br/>2.使用预处理执行SQL语句，对所有传入SQL语句中的变量做绑定。<br/>3.部署Web应用防火墙<br/>4.对数据库操作进行监控<br/>",
                "TaskId": 949057,
                "UpdatedAt": "2018-03-24T15:38:31+08:00",
                "Url": "http://demo.aisec.cn:80/demo/aisec/ajax_link.php?t=0.2553907226758148&id=1-0"
            }
        ]
    }
}
```

