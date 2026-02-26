**Example 1: 成功示例**

成功示例

Input: 

```
tccli apm DescribeApmSQLInjectionDetail --cli-unfold-argument  \
    --StartTime 1735206217 \
    --EndTime 1735207117 \
    --OrderBy.Key startTime \
    --OrderBy.Value desc \
    --Filters.0.Type = \
    --Filters.0.Key attack.symbol \
    --Filters.0.Value 1 \
    --Filters.1.Type = \
    --Filters.1.Key process.serviceName \
    --Filters.1.Value springboot-service \
    --Filters.2.Type = \
    --Filters.2.Key attack.subtype \
    --Filters.2.Value 经典注入 \
    --Filters.3.Type = \
    --Filters.3.Key db.instance \
    --Filters.3.Value mockproject \
    --Filters.4.Type = \
    --Filters.4.Key db.ip \
    --Filters.4.Value 9.135.250.82:3306 \
    --Filters.5.Type = \
    --Filters.5.Key db.statement \
    --Filters.5.Value H4sIAAAAAAAAAytOzUlNLlE1MtAC4rSi/FwgVVqcWhSfmZeWXxyfklqSmJkDAPuw0CAlAAAA \
    --Filters.6.Type = \
    --Filters.6.Key db.system \
    --Filters.6.Value mysql \
    --InstanceId apm-oJ7C40jYv \
    --GroupBy  \
    --Metrics.0.MetricName traceID \
    --Metrics.1.MetricName spanID \
    --Metrics.2.MetricName startTime \
    --Metrics.3.MetricName duration \
    --Metrics.4.MetricName attack.payload \
    --Metrics.5.MetricName attack.subtype \
    --Metrics.6.MetricName attack.level \
    --Metrics.7.MetricName repair.suggestion \
    --Metrics.8.MetricName db.statement \
    --Metrics.9.MetricName db.system \
    --Metrics.10.MetricName db.ip \
    --Metrics.11.MetricName db.instance
```

Output: 
```
{
    "Response": {
        "Records": [
            {
                "Fields": [
                    {
                        "CompareVal": "",
                        "CompareVals": null,
                        "Key": "startTime",
                        "LastPeriodValue": null,
                        "Unit": "",
                        "Value": 1735206997885801
                    },
                    {
                        "CompareVal": "",
                        "CompareVals": null,
                        "Key": "duration",
                        "LastPeriodValue": null,
                        "Unit": "",
                        "Value": 11457
                    },
                    {
                        "CompareVal": "",
                        "CompareVals": null,
                        "Key": "status",
                        "LastPeriodValue": null,
                        "Unit": "",
                        "Value": 0
                    }
                ],
                "Tags": [
                    {
                        "Key": "spanID",
                        "Value": "69671198c78af620"
                    },
                    {
                        "Key": "attack.payload",
                        "Value": "select * from user_infos_detail where 1=1"
                    },
                    {
                        "Key": "attack.subtype",
                        "Value": "经典注入"
                    },
                    {
                        "Key": "attack.level",
                        "Value": "important"
                    },
                    {
                        "Key": "repair.suggestion",
                        "Value": "H4sIAAAAAAAA/12QzU7CQBSFX6WZlSbEB9C4d6Hxh6U1pkCjjWXAaV0REkCQJkIrokSQHyWWEBOkMQYJUHgYO0O74hUcGEKMq7m5955zvjsxQKoJbBmkdu2V77DewFoZbHLAGWaIrjkDbfrQJto3XXJsHU8ybis5raTJo0XyH3hQZLKfRAr4gGNP6PL+0R55vSH13sJlfItbKW5HCogICqo4G+Vw1sBWYfr8RXSTFPOOXfUf7v41wEaK2uNciTRMt9uc23jJCc7kmQZX21TgdjvYMJ1+hxj3OGMySHdcpPU8w7K9rMHsvGZ6Oiq53QLFXglpHkWbjSoHSIwKSAz5VUoXFqHKKSq3zQUjEG5E2Ww1WlMu5fUtyslyvPec200uruyb5GU0/z6t94/EGZre0yfpNL1anZKQaoNh4ILtDN9WGH4VSfDs+IQLyELw4lSWFhQxHggwxAMfx4MIoi8PJKiISGWtYOQKLssQikSXzXPEirC0VCqyKNJhHMR/AS5DXCTsAQAA"
                    },
                    {
                        "Key": "db.statement",
                        "Value": "select * from user_infos_detail"
                    },
                    {
                        "Key": "db.system",
                        "Value": "mysql"
                    },
                    {
                        "Key": "db.ip",
                        "Value": "9.135.250.82:3306"
                    },
                    {
                        "Key": "db.instance",
                        "Value": "mockproject"
                    },
                    {
                        "Key": "traceID",
                        "Value": "3e5c9cbb6c607f38e4917b52e410c49c"
                    }
                ]
            },
            {
                "Fields": [
                    {
                        "CompareVal": "",
                        "CompareVals": null,
                        "Key": "startTime",
                        "LastPeriodValue": null,
                        "Unit": "",
                        "Value": 1735206995416390
                    },
                    {
                        "CompareVal": "",
                        "CompareVals": null,
                        "Key": "duration",
                        "LastPeriodValue": null,
                        "Unit": "",
                        "Value": 9004
                    },
                    {
                        "CompareVal": "",
                        "CompareVals": null,
                        "Key": "status",
                        "LastPeriodValue": null,
                        "Unit": "",
                        "Value": 0
                    }
                ],
                "Tags": [
                    {
                        "Key": "spanID",
                        "Value": "8ec3dba165ea141a"
                    },
                    {
                        "Key": "attack.payload",
                        "Value": "select * from user_infos_detail where 1=1"
                    },
                    {
                        "Key": "attack.subtype",
                        "Value": "经典注入"
                    },
                    {
                        "Key": "attack.level",
                        "Value": "important"
                    },
                    {
                        "Key": "repair.suggestion",
                        "Value": "H4sIAAAAAAAA/12QzU7CQBSFX6WZlSbEB9C4d6Hxh6U1pkCjjWXAaV0REkCQJkIrokSQHyWWEBOkMQYJUHgYO0O74hUcGEKMq7m5955zvjsxQKoJbBmkdu2V77DewFoZbHLAGWaIrjkDbfrQJto3XXJsHU8ybis5raTJo0XyH3hQZLKfRAr4gGNP6PL+0R55vSH13sJlfItbKW5HCogICqo4G+Vw1sBWYfr8RXSTFPOOXfUf7v41wEaK2uNciTRMt9uc23jJCc7kmQZX21TgdjvYMJ1+hxj3OGMySHdcpPU8w7K9rMHsvGZ6Oiq53QLFXglpHkWbjSoHSIwKSAz5VUoXFqHKKSq3zQUjEG5E2Ww1WlMu5fUtyslyvPec200uruyb5GU0/z6t94/EGZre0yfpNL1anZKQaoNh4ILtDN9WGH4VSfDs+IQLyELw4lSWFhQxHggwxAMfx4MIoi8PJKiISGWtYOQKLssQikSXzXPEirC0VCqyKNJhHMR/AS5DXCTsAQAA"
                    },
                    {
                        "Key": "db.statement",
                        "Value": "select * from user_infos_detail"
                    },
                    {
                        "Key": "db.system",
                        "Value": "mysql"
                    },
                    {
                        "Key": "db.ip",
                        "Value": "9.135.250.82:3306"
                    },
                    {
                        "Key": "db.instance",
                        "Value": "mockproject"
                    },
                    {
                        "Key": "traceID",
                        "Value": "1cf61d4b03c11f728573b205886e79b0"
                    }
                ]
            }
        ],
        "RequestId": "befc9b8d-d73a-4447-bcc6-a5d6212dad99",
        "Tags": [
            {
                "Key": "attack.subtype",
                "Value": "经典注入"
            },
            {
                "Key": "attack.level",
                "Value": "important"
            },
            {
                "Key": "repair.suggestion",
                "Value": "H4sIAAAAAAAA/12QzU7CQBSFX6WZlSbEB9C4d6Hxh6U1pkCjjWXAaV0REkCQJkIrokSQHyWWEBOkMQYJUHgYO0O74hUcGEKMq7m5955zvjsxQKoJbBmkdu2V77DewFoZbHLAGWaIrjkDbfrQJto3XXJsHU8ybis5raTJo0XyH3hQZLKfRAr4gGNP6PL+0R55vSH13sJlfItbKW5HCogICqo4G+Vw1sBWYfr8RXSTFPOOXfUf7v41wEaK2uNciTRMt9uc23jJCc7kmQZX21TgdjvYMJ1+hxj3OGMySHdcpPU8w7K9rMHsvGZ6Oiq53QLFXglpHkWbjSoHSIwKSAz5VUoXFqHKKSq3zQUjEG5E2Ww1WlMu5fUtyslyvPec200uruyb5GU0/z6t94/EGZre0yfpNL1anZKQaoNh4ILtDN9WGH4VSfDs+IQLyELw4lSWFhQxHggwxAMfx4MIoi8PJKiISGWtYOQKLssQikSXzXPEirC0VCqyKNJhHMR/AS5DXCTsAQAA"
            },
            {
                "Key": "db.statement",
                "Value": "select * from user_infos_detail"
            },
            {
                "Key": "db.system",
                "Value": "mysql"
            },
            {
                "Key": "db.ip",
                "Value": "9.135.250.82:3306"
            },
            {
                "Key": "db.instance",
                "Value": "mockproject"
            }
        ]
    }
}
```

