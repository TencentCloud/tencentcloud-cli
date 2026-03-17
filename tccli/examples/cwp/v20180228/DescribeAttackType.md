**Example 1: 查询应用防护白名单攻击类型列表**



Input: 

```
tccli cwp DescribeAttackType --cli-unfold-argument  \
    --Filters.0.Name Keywords \
    --Filters.0.Values sda
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AttackTypeID": 18,
                "AttackTypeName": "JSTL任意文件包含",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 34,
                "AttackTypeName": "高危方法调用",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 33,
                "AttackTypeName": "WebShell 后门",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 31,
                "AttackTypeName": "IP/URL阻断",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 30,
                "AttackTypeName": "恶意反射调用",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 29,
                "AttackTypeName": "SQL注入",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 28,
                "AttackTypeName": "内存马注入",
                "Source": "memshell_inject"
            },
            {
                "AttackTypeID": 27,
                "AttackTypeName": "恶意Attach",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 26,
                "AttackTypeName": "恶意外链",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 25,
                "AttackTypeName": "引擎注入",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 24,
                "AttackTypeName": "XML实体注入",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 23,
                "AttackTypeName": "恶意DNS查询",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 22,
                "AttackTypeName": "JNI注入",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 21,
                "AttackTypeName": "恶意类加载",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 20,
                "AttackTypeName": "危险协议使用",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 19,
                "AttackTypeName": "线程注入",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 17,
                "AttackTypeName": "表达式注入",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 16,
                "AttackTypeName": "HTTP信息获取",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 15,
                "AttackTypeName": "命令执行",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 14,
                "AttackTypeName": "JNDI注入",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 13,
                "AttackTypeName": "恶意文件读写",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 12,
                "AttackTypeName": "任意文件删除",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 11,
                "AttackTypeName": "目录遍历",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 10,
                "AttackTypeName": "恶意文件上传",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 9,
                "AttackTypeName": "任意文件读取",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 36,
                "AttackTypeName": "XPath注入漏洞",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 37,
                "AttackTypeName": "URL 重定向漏洞",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 38,
                "AttackTypeName": "其他类型反序列化漏洞",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 39,
                "AttackTypeName": "JDBC漏洞",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 40,
                "AttackTypeName": "规则模式",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 41,
                "AttackTypeName": "扫描器检测",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 52,
                "AttackTypeName": "Spring 框架反射型文件下载漏洞 (CVE-2020-5421)",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 44,
                "AttackTypeName": "Apache Flink 任意文件读取漏洞 (CVE-2020-17519)",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 43,
                "AttackTypeName": "Openfire 身份认证绕过漏洞(CVE-2023-32315)",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 45,
                "AttackTypeName": "GeoServer Jiffle 远程代码执行漏洞(CVE-2022-24816)",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 46,
                "AttackTypeName": "OpenTSDB 命令注入漏洞（CVE-2020-35476）",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 47,
                "AttackTypeName": "Bitbucket Server 命令注入漏洞（CVE-2022-36804）",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 48,
                "AttackTypeName": "Atlassian Crowd和Atlassian Crowd Data Center 输入验证错误漏洞(CVE-2019-11580)",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 49,
                "AttackTypeName": "Apache Tomcat拒绝服务漏洞（CVE-2020-13935）",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 50,
                "AttackTypeName": "Atlassian Confluence Data Center and Server 访问控制漏洞(CVE-2023-22515)",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 51,
                "AttackTypeName": "Atlassian Confluence Data Center and  Server 权限绕过漏洞(CVE-2023-22518)",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 1,
                "AttackTypeName": "Log4shell漏洞",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 42,
                "AttackTypeName": "JetBrains TeamCity 安全漏洞",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 35,
                "AttackTypeName": "Springboot Actuator未授权访问漏洞",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 32,
                "AttackTypeName": "Tomcat AJP 任意文件读取/包含漏洞（CVE-2020-1938）",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 8,
                "AttackTypeName": "Apache Kafka Connect JNDI注入漏洞",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 7,
                "AttackTypeName": "Spring4Shell远程代码执行漏洞(CVE-2022-22965)",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 6,
                "AttackTypeName": "Apache RocketMQ远程代码执行漏洞（CVE-2023-33246）",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 5,
                "AttackTypeName": "Jenkins Remoting任意文件读取漏洞",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 4,
                "AttackTypeName": "Java反序列化漏洞",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 3,
                "AttackTypeName": "XStream反序列化漏洞",
                "Source": "rasp"
            },
            {
                "AttackTypeID": 2,
                "AttackTypeName": "FastJson反序列化漏洞",
                "Source": "rasp"
            }
        ],
        "RequestId": "21342534-5a16-40e1-8f59-60d2f378ee7d",
        "TotalCount": 52
    }
}
```

