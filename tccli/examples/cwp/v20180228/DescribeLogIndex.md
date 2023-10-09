**Example 1: 示例**



Input: 

```
tccli cwp DescribeLogIndex --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ModifyTime": "2022-07-04 15:05:18",
        "RequestId": "f2e256a6-e51e-4d9f-8d73-c81290a248ab",
        "Rule": {
            "FullText": {
                "CaseSensitive": false,
                "ContainZH": true,
                "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\"
            },
            "KeyValue": {
                "CaseSensitive": false,
                "KeyValues": [
                    {
                        "Key": "password_due_days",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "long",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "file_exist",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "login_time",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "path_md5",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "proc_tree",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "domain",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "src_ip",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "is_risk_area",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "rule",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "path_count",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "long",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "file_modify_time",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "long",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "file_access_time",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "long",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "plugin_count",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "long",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "parent_proc_group",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "sid",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "long",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "is_emergency",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "param",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "appid",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "long",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "src_port",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "long",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "bwtype",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "long",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "platform",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "cpu_info",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "http_referer",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "parent_process_name",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "command",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "pid",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "euid",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "long",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "recover_time",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "is_root",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "disable_time",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "http_host",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "event_type",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "virus_name",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "ip",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "proto",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "log_path",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "loader_class_name",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "vul_type",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "find_time",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "config_path",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "http_head",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "last_login_ip",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "service_type",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "id",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "long",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "full_path",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "is_deleted",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "parent_proc_path",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "host_ip",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "type",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "password_change_type",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "version",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "http_cgi",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "status",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "rule_name",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "core_version",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "class_name",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "path",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "home_path",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "process_count",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "long",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "package_name",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "disk_size",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "long",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "uuid",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "category_name",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "rule_level",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "argv",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "password_lock_days",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "long",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "data_path",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "boot_time",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "long",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "install_path",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "vul_category",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "reference",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "pstree",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "descript",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "host_name",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "desc",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "install_time",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "long",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "dst_port",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "long",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "parent_proc_name",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "process_exe",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "cve_id",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "os_type",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "long",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "last_login_time",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "long",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "tty",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "exe",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "http_param",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "level",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "count",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "long",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "event_detail",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "cpu_size",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "long",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "http_user_agent",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "event_status",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "process_argv",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "password_status",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "error_log_path",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "super_class_name",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "src_machine_name",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "user_name",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "recover_type",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "filesize",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "long",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "process_name",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "exception_message",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "memory_size",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "long",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "virtual_path",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "quuid",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "modify_time",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "hostip",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "interfaces",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "user",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "hostname",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "os_info",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "update_time",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "long",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "plugin_path",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "cycle",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "http_method",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "parent_proc_user",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "os_name",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "location",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "exception",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "last_login_terminal",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "proc_file_privilege",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "query_time",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "merge_time",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "start_time",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "long",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "offline_time",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "fix",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "username",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "is_risk_user",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "class_file",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "size",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "long",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "root_path",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "url",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "is_manual_recover",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "target",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "group_name",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "value",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "banned",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "md5",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "access_count",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "long",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "uid",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "long",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "file_type",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "login_type",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "is_risk_time",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "gid",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "long",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "has_recovered",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "lang",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "shell",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "password_warn_days",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "long",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "permission",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "file_create_time",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "long",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "cmd_line",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "event_count",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "long",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "http_content",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "create_time",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "bash_cmd",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "password_change_time",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "port",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "uninstall_time",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "exec_time",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "file_path",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "user_group",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "ppid",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "instance_id",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "bin_path",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "cls_event_type",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "dst_ip",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "remark",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "is_risk_src_ip",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "recent_found_time",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "name",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "egid",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "long",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    },
                    {
                        "Key": "float_ip",
                        "Value": {
                            "Tokenizer": "@&()='\",;:<>[]{}/ \\n\\t\\r\\",
                            "Type": "text",
                            "SqlFlag": true,
                            "ContainZH": true
                        }
                    }
                ]
            },
            "Tag": {
                "CaseSensitive": false,
                "KeyValues": null
            }
        },
        "Status": true
    }
}
```

