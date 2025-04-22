**Example 1: 检测失败示例**

查询检测结果，结果失败

Input: 

```
tccli ioa DescribeDLPFileDetectResult --cli-unfold-argument  \
    --QueryID 207d7f0d-fe43-4483-a6bb-470321e60bbc
```

Output: 
```
{
    "Response": {
        "Data": {
            "FileMd5": "aabba408088b6aea1601fe6823cef111",
            "FileName": "商务合同.docx",
            "Status": "检测失败:detect failed: open /data/services/pcmgr_enterprise/data/tmp/dlp_file/aabba408088b6aea1601fe6823cef111/%E5%95%86%E5%8A%A1%E5%90%88%E5%90%8C.docx: no such file or directory"
        },
        "RequestId": "778917dd-0258-4072-814a-10f62bb5d55b"
    }
}
```

**Example 2: 检测成功示例**

查询检测结果，结果成功

Input: 

```
tccli ioa DescribeDLPFileDetectResult --cli-unfold-argument  \
    --QueryID 81f73e3b-f42e-4c15-8ef5-2ca670e9446b
```

Output: 
```
{
    "Response": {
        "Data": {
            "DetectResult": "{\"Path\":\"/data/services/pcmgr_enterprise/data/tmp/dlp_file/e8bcc9bb7ef5765cb7ce79831ede2039/YOGA%20BOOK%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97.pdf\",\"Type\":\".pdf\",\"Size\":802831,\"State\":2,\"Md5\":\"e8bcc9bb7ef5765cb7ce79831ede2039\",\"Result\":{\"FileName\":\"YOGA%20BOOK%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97.pdf\",\"FileContent\":\"{\\\"FileAbstract\\\":\\\"YOGA BOOK with Windows®\\\\n用户指南\\\\nLenovo YB1-X91F\\\\nLenovo YB1-X91L\\\\nLenovo YB1-X91X\\\\n \\\\n \\\\n \\\\n \\\\n \\\\n \\\\n \\\\n \\\\n \\\\n \\\\n \\\\n \\\\n \\\\n \\\\n \\\\n入门指南\\\\n在使用本用户指南及其支持的产品之\\\"}\",\"HitRuleId\":[\"364313\"],\"HitRuleCategoryId\":[\"29198\"],\"HitLevel\":[\"S2\"],\"HitRuleDesc\":\"364313(通讯信息)\",\"HitContent\":\"[{\\\"RuleId\\\":\\\"364313\\\",\\\"Hits\\\":[{\\\"LibraryId\\\":\\\"5148\\\",\\\"Attribute\\\":\\\"doc.Content\\\",\\\"String\\\":\\\"电话\\\",\\\"Content\\\":\\\" Internet  \\\\u003e  移动电话。\\\\n2. 点按移动网络的名称。\\\\n\\\"},{\\\"LibraryId\\\":\\\"5347\\\",\\\"Attribute\\\":\\\"doc.Content\\\",\\\"String\\\":\\\"邮箱\\\",\\\"Content\\\":\\\"有电子邮件帐户，可直接登录到电子邮箱。如果没有，您需要创建一个电子邮\\\"},{\\\"LibraryId\\\":\\\"5305\\\",\\\"Attribute\\\":\\\"doc.Content\\\",\\\"String\\\":\\\"地址\\\",\\\"Content\\\":\\\"名称，输入连接名称、服务器名称或地址、用户名和密码，然后点按保存以连\\\"},{\\\"LibraryId\\\":\\\"45\\\",\\\"Attribute\\\":\\\"doc.Type\\\",\\\"String\\\":\\\".pdf\\\",\\\"Content\\\":\\\".pdf\\\"}]}]\"},\"EngineConfigVersion\":\"1744627119\"}",
            "FileMd5": "e8bcc9bb7ef5765cb7ce79831ede2039",
            "FileName": "YOGA BOOK用户指南.pdf",
            "Status": "检测成功"
        },
        "RequestId": "5bc117a2-410a-42f9-98ea-e54b4f275f8c"
    }
}
```

