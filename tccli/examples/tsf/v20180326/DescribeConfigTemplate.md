**Example 1: 导入配置模板**



Input: 

```
tccli tsf DescribeConfigTemplate --cli-unfold-argument  \
    --ConfigTemplateId dcfg_temp-evjrwqyb
```

Output: 
```
{
    "Response": {
        "RequestId": "0c34a61c-fd80-453e-8a52-0532d8e4e5b0",
        "Result": {
            "ConfigTemplateId": "dcfg_temp-evjrwqyb",
            "ConfigTemplateName": "下线检测系统",
            "ConfigTemplateDesc": "下线检测系统",
            "ConfigTemplateType": "customize",
            "ConfigTemplateValue": "dl_mysql_host: 10.16.0.10\ndl_mysql_port: 3306\ndl_mysql_dbname: fca\ndl_mysql_username: root\ndl_mysql_password: fca@2018\nredis_host: '10.16.0.9:6379'\nredis_database: 1\nredis_password: fca@2018\nredis_port: 6379\nSPRING_PROFILES_ACTIVE: pro",
            "CreateTime": "2019-05-05 18:24:43.0",
            "UpdateTime": null
        }
    }
}
```

