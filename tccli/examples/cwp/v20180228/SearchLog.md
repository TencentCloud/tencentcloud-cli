**Example 1: 示例**



Input: 

```
tccli cwp SearchLog --cli-unfold-argument  \
    --Sort desc \
    --Count 20 \
    --QueryString status: "异常登录" AND public_ip_addresses: (1* OR 2*) AND NOT hostip: (10.128.200.* OR 10.129.24.212) AND NOT src_ip: (10.128.128.7 OR 192.144.182.173) \
    --StartTime 1656641065449 \
    --EndTime 1656641965449
```

Output: 
```
{
    "Response": {
        "Analysis": false,
        "Context": "content",
        "Count": 2,
        "Data": [
            {
                "Content": "{\"create_time\":\"2022-07-01 10:00:27 +0800 CST\",\"hostip\":\"10.0.0.6\",\"level\":\"中危\",\"modify_time\":\"2022-07-01 10:17:05 +0800 CST\",\"remark\":\"\",\"uuid\":\"13bb1e16-9a7a-434d-9686-4328f72c97d7\",\"is_emergency\":\"False\",\"reference\":\"https://www.phpmyadmin.net/security/PMASA-2016-20/\",\"path\":\"/var/www/html/phpmyadmin\",\"fix\":\"1、建议升级到官方最新版本，官网地址：https://www.phpmyadmin.net\",\"cve_id\":\"CVE-2016-5704\",\"cls_event_type\":\"Web-CMS_vul\",\"appid\":\"1256299843\",\"name\":\"phpMyAdmin 4.6.x 表结构页面存在XSS漏洞\",\"id\":\"771\",\"vul_category\":\"Web-CMS漏洞\",\"descript\":\"漏洞文件路径: /var/www/html/phpmyadmin/templates/table/structure/display_table_stats.phtml\",\"event_status\":\"modify\",\"status\":\"待处理\"}",
                "FileName": "file***",
                "Source": "",
                "TimeStamp": 1656641946000
            },
            {
                "Content": "{\"create_time\":\"2022-07-01 10:00:27 +0800 CST\",\"hostip\":\"10.0.0.6\",\"level\":\"高危\",\"modify_time\":\"2022-07-01 10:17:05 +0800 CST\",\"remark\":\"\",\"uuid\":\"13bb1e16-9a7a-434d-9686-4328f72c97d7\",\"is_emergency\":\"False\",\"reference\":\"https://httpd.apache.org/security/vulnerabilities_24.html\",\"path\":\"\",\"fix\":\"升级至2.4.6-90及以上版本或 2.4.39及以上版本\",\"cve_id\":\"CVE-2019-0217\",\"cls_event_type\":\"application_vul\",\"appid\":\"1256299843\",\"name\":\"Apache HTTP Server mod_auth_digest 条件竞争漏洞\",\"id\":\"767\",\"vul_category\":\"应用漏洞\",\"descript\":\"Apache HTTP Server 启用了 mod_auth_digest 模块，且Apache HTTP Server 版本为：2.4.37-47.module_el8.6.0+1111+ce6f4ceb.1。\",\"event_status\":\"modify\",\"status\":\"待处理\"}",
                "FileName": "file***",
                "Source": "",
                "TimeStamp": 1656641946000
            }
        ],
        "ListOver": true,
        "RequestId": "e6bb2f6d-10b3-40fd-b3a4-630dbdf477c3"
    }
}
```

