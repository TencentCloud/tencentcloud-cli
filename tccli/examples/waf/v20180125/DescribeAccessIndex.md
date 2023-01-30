**Example 1: 访问日志索引配置信息**

访问日志索引配置信息

Input: 

```
tccli waf DescribeAccessIndex --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Status": true,
        "Rule": {
            "FullText": {
                "CaseSensitive": true,
                "Tokenizer": "!@#%^&*()-_=\"', <>/?|\\;:\n\t\r[]{}",
                "ContainZH": false
            },
            "KeyValue": {
                "CaseSensitive": false,
                "KeyValues": [
                    {
                        "Key": "method",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "",
                            "SqlFlag": true,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "schema",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "",
                            "SqlFlag": true,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "host",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "",
                            "SqlFlag": true,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "url",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "",
                            "SqlFlag": false,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "client",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "",
                            "SqlFlag": false,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "status",
                        "Value": {
                            "Type": "long",
                            "Tokenizer": "",
                            "SqlFlag": false,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "upstream_status",
                        "Value": {
                            "Type": "long",
                            "Tokenizer": "",
                            "SqlFlag": false,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "user_agent",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "",
                            "SqlFlag": true,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "x_forwarded_for",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "",
                            "SqlFlag": false,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "referer",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "",
                            "SqlFlag": false,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "domain",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "",
                            "SqlFlag": true,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "cookie",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "",
                            "SqlFlag": false,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "body",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "",
                            "SqlFlag": false,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "uuid",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "",
                            "SqlFlag": false,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "query",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "",
                            "SqlFlag": false,
                            "ContainZH": false
                        }
                    }
                ]
            }
        },
        "ModifyTime": "2021-06-18 16:02:20",
        "RequestId": "9b02bf9e-c89c-42c3-9ae1-685f968fa02d"
    }
}
```

