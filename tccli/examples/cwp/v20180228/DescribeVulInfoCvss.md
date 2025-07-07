**Example 1: 漏洞详情，带CVSS版本**

漏洞详情，带CVSS版本

Input: 

```
tccli cwp DescribeVulInfoCvss --cli-unfold-argument  \
    --VulId 100441
```

Output: 
```
{
    "Response": {
        "CveId": "1",
        "CvssScore": 1,
        "Description": "ad",
        "Reference": "fs",
        "VulName": "漏洞1",
        "CveInfo": "AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N",
        "CvssScoreFloat": 9.9,
        "VulType": 1,
        "VulLevel": 2,
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "VulId": 100441,
        "RepairPlan": "13412",
        "CVSS": "AV:L/AC:L/Au:N/C:N/I:P/A:N",
        "Labels": "tag1,tag2",
        "DefenseAttackCount": 1,
        "SuccessFixCount": 1,
        "FixSwitch": 0,
        "PublicDate": "2020-12-30:00:00:00"
    }
}
```

**Example 2: 漏洞防御容器视角漏洞详情**

漏洞防御容器视角漏洞详情

Input: 

```
tccli cwp DescribeVulInfoCvss --cli-unfold-argument  \
    --VulId 396620 \
    --Source tcss
```

Output: 
```
{
    "Response": {
        "CVSS": "AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H",
        "CveId": "CVE-2023-25194",
        "CveInfo": "",
        "CvssScore": 9,
        "CvssScoreFloat": 8.8,
        "DefenseAttackCount": 0,
        "Description": "Kafka 是 Apache 软件基金会的一种分布式的、基于发布/订阅的消息系统，可以处理消费者在网站中的所有动作流数据。Kafka Connect 是一种工具，用于在 Apache Kafka 和其他数据系统之间以可扩展且可靠的方式传输数据。Kafka 2.3.0 至 3.3.2 版本中，具有 Kafka Connect worker 访问权限且可以创建/修改 Connect 的攻击者可通过将 Connect 的任意 Kafka 客户端的 sasl.jaas.config 属性设置为 com.sun.security.auth.module.JndiLoginModule（此操作可通过 producer.override.sasl.jaas.config 、consumer.override.sasl.jaas.config 或 admin.override.sasl.jaas.config 属性完成），进而可将 Connect 的属性user.provider.url设置为攻击者可控的 LDAP 服务器地址，并通过 Connect 反序列化可控的 LDAP 响应远程执行恶意代码或造成拒绝服务。",
        "FixSwitch": 0,
        "Labels": "必修漏洞,远程利用",
        "PublicDate": "2023-02-08 00:00:00",
        "Reference": "https://kafka.apache.org/cve-list,https://lists.apache.org/thread/vy1c7fqcdqvq5grcqp6q5jyyb302khyz",
        "RepairPlan": "目前 Apache 官方已发布此漏洞修复版本，建议用户尽快升级至 Apache Kafka3.4 及以上版本。参考链接: https://github.com/apache/kafka/releases/tag/3.4.0。暂时无法升级的用户可通过验证Kafka Connect连接器配置，仅允许受信任的JNDI配置来缓解此漏洞。",
        "RequestId": "02e1ac7f-5011-4677-8bab-45c5151908d2",
        "SuccessFixCount": 0,
        "SupportDefence": 1,
        "VulId": 102518,
        "VulLevel": 3,
        "VulName": "Apache Kafka Connect 远程代码执行漏洞(CVE-2023-25194)",
        "VulType": 2
    }
}
```

