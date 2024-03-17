**Example 1: 查询所有模板列表**

查询所有模板列表

Input: 

```
tccli tse DescribeAllConfigFileTemplates --cli-unfold-argument  \
    --InstanceId ins-fd191a86
```

Output: 
```
{
    "Response": {
        "ConfigFileTemplates": [
            {
                "Id": 0,
                "Name": "spring-cloud-gateway-braining",
                "Content": "{\n    \"rules\":[\n        {\n            \"conditions\":[\n                {\n                    \"key\":\"${http.query.uid}\",\n                    \"values\":[\"10000\"],\n                    \"operation\":\"EQUALS\"\n                }\n            ],\n            \"labels\":[\n                {\n                    \"key\":\"env\",\n                    \"value\":\"green\"\n                }\n            ]\n        }\n    ]\n}",
                "Format": "json",
                "Comment": "Spring Cloud Gateway  染色规则",
                "CreateTime": "",
                "CreateBy": "",
                "ModifyTime": "",
                "ModifyBy": ""
            }
        ],
        "RequestId": "jayhjxu-test-DescribeAllConfigFileTemplates--ssss",
        "TotalCount": 1
    }
}
```

