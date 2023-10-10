**Example 1: 获取日志类型**



Input: 

```
tccli cwp DescribeLogType --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": "{\"logType\":{\"入侵检测\":[\"malware\",\"hostlogin\",\"bruteattack\",\"risk_dns\",\"bash\",\"privilege_escalation\",\"reverse_shell\"],\"基线管理\":[\"baseline\"],\"客户端相关\":[\"agent_offline\",\"agent_uninstall\"],\"漏洞管理\":[\"emergency_vul\",\"linux_app_vul\",\"windows_sys_vul\",\"Web-CMS_vul\",\"application_vul\"],\"资产指纹\":[\"asset_system\",\"asset_account\",\"asset_netstat\",\"asset_process\",\"asset_app\",\"asset_database\",\"asset_web_app\",\"asset_web_service\",\"asset_web_frame\",\"asset_web_location\",\"asset_jar\",\"asset_init_service\",\"asset_scheduled_task\",\"asset_env\",\"asset_core_module\"],\"高级防御\":[\"java_shell\",\"file_tamper\",\"attack_logs\",\"tamper_protect_exceptions\",\"tamper_protect_logs\"]}}",
        "RequestId": "cbff5b6e-c53c-4761-8c77-738143b6e8cd"
    }
}
```

