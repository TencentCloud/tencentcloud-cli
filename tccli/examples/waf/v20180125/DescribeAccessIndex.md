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
            "FullText": null,
            "KeyValue": {
                "CaseSensitive": false,
                "KeyValues": [
                    {
                        "Key": "bot_action",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "token",
                            "SqlFlag": true,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "bot_ai",
                        "Value": {
                            "Type": "long",
                            "Tokenizer": "token",
                            "SqlFlag": true,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "bot_label",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "token",
                            "SqlFlag": true,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "bot_module",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "token",
                            "SqlFlag": true,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "bot_scene_id",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "token",
                            "SqlFlag": false,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "bot_score",
                        "Value": {
                            "Type": "long",
                            "Tokenizer": "token",
                            "SqlFlag": false,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "bot_stat",
                        "Value": {
                            "Type": "long",
                            "Tokenizer": "token",
                            "SqlFlag": true,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "bot_ti_tags",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "token",
                            "SqlFlag": false,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "bot_token",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "token",
                            "SqlFlag": true,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "bot_ua",
                        "Value": {
                            "Type": "long",
                            "Tokenizer": "token",
                            "SqlFlag": false,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "bytes_sent",
                        "Value": {
                            "Type": "long",
                            "Tokenizer": "token",
                            "SqlFlag": true,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "client",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "token",
                            "SqlFlag": true,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "cookie",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "token",
                            "SqlFlag": false,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "domain",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "token",
                            "SqlFlag": true,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "headers",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "token",
                            "SqlFlag": false,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "host",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "token",
                            "SqlFlag": true,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "instance",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "token",
                            "SqlFlag": false,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "ipinfo_city",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "token",
                            "SqlFlag": true,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "ipinfo_isp",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "token",
                            "SqlFlag": true,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "ipinfo_nation",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "token",
                            "SqlFlag": true,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "ipinfo_province",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "token",
                            "SqlFlag": true,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "ipinfo_state",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "token",
                            "SqlFlag": true,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "method",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "token",
                            "SqlFlag": true,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "query",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "token",
                            "SqlFlag": false,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "referer",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "token",
                            "SqlFlag": false,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "request_time",
                        "Value": {
                            "Type": "double",
                            "Tokenizer": "token",
                            "SqlFlag": true,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "schema",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "token",
                            "SqlFlag": true,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "sec_chain",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "token",
                            "SqlFlag": false,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "status",
                        "Value": {
                            "Type": "long",
                            "Tokenizer": "token",
                            "SqlFlag": true,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "ua_goodbot",
                        "Value": {
                            "Type": "long",
                            "Tokenizer": "token",
                            "SqlFlag": true,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "ua_type",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "token",
                            "SqlFlag": true,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "upstream",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "token",
                            "SqlFlag": true,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "upstream_connect_time",
                        "Value": {
                            "Type": "double",
                            "Tokenizer": "token",
                            "SqlFlag": true,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "upstream_response_time",
                        "Value": {
                            "Type": "double",
                            "Tokenizer": "token",
                            "SqlFlag": true,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "upstream_status",
                        "Value": {
                            "Type": "long",
                            "Tokenizer": "token",
                            "SqlFlag": true,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "url",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "token",
                            "SqlFlag": true,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "user_agent",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "token",
                            "SqlFlag": true,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "uuid",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "token",
                            "SqlFlag": false,
                            "ContainZH": false
                        }
                    },
                    {
                        "Key": "x_forwarded_for",
                        "Value": {
                            "Type": "text",
                            "Tokenizer": "token",
                            "SqlFlag": false,
                            "ContainZH": false
                        }
                    }
                ]
            },
            "Tag": null
        },
        "ModifyTime": "2024-10-24 22:15:00",
        "RequestId": "5ccd823d-ede6-4f21-b520-0db96a19f5f1"
    }
}
```

