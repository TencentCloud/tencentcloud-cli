**Example 1: 成功示例**

成功示例

Input: 

```
tccli apm DescribeApmAllVulCount --cli-unfold-argument  \
    --StartTime 1741170000 \
    --EndTime 1741173900
```

Output: 
```
{
    "Response": {
        "CriticalVulnerabilityCount": 0,
        "ImportantVulnerabilityCount": 64,
        "RequestId": "1f1cd1b3-8129-4391-8554-f16e5e233d95",
        "VulnerabilityCount": 64,
        "VulnerabilityList": [
            {
                "Fields": [
                    {
                        "CompareVal": "",
                        "CompareVals": null,
                        "Key": "instance_count",
                        "LastPeriodValue": null,
                        "Unit": "",
                        "Value": 4
                    }
                ],
                "Tags": [
                    {
                        "Key": "tapm.instance.key",
                        "Value": "apm-oJ7C40jYv"
                    },
                    {
                        "Key": "instrumentation.name",
                        "Value": "com.fasterxml.jackson.core:jackson-databind"
                    },
                    {
                        "Key": "version",
                        "Value": "2.12.3"
                    },
                    {
                        "Key": "cve.id",
                        "Value": "CVE-2020-36518"
                    },
                    {
                        "Key": "vul.id",
                        "Value": "200006"
                    },
                    {
                        "Key": "level",
                        "Value": "important"
                    },
                    {
                        "Key": "score",
                        "Value": "7.50"
                    },
                    {
                        "Key": "vul.name",
                        "Value": "FasterXML jackson-databind 缓冲区错误漏洞（CVE-2020-36518）"
                    }
                ]
            },
            {
                "Fields": [
                    {
                        "CompareVal": "",
                        "CompareVals": null,
                        "Key": "instance_count",
                        "LastPeriodValue": null,
                        "Unit": "",
                        "Value": 3
                    }
                ],
                "Tags": [
                    {
                        "Key": "tapm.instance.key",
                        "Value": "apm-ewyzCXlxj"
                    },
                    {
                        "Key": "instrumentation.name",
                        "Value": "com.fasterxml.jackson.core:jackson-databind"
                    },
                    {
                        "Key": "version",
                        "Value": "2.12.3"
                    },
                    {
                        "Key": "cve.id",
                        "Value": "CVE-2021-46877"
                    },
                    {
                        "Key": "vul.id",
                        "Value": "200007"
                    },
                    {
                        "Key": "level",
                        "Value": "important"
                    },
                    {
                        "Key": "score",
                        "Value": "7.50"
                    },
                    {
                        "Key": "vul.name",
                        "Value": "jackson-databind 拒绝服务漏洞（CVE-2021-46877）"
                    }
                ]
            },
            {
                "Fields": [
                    {
                        "CompareVal": "",
                        "CompareVals": null,
                        "Key": "instance_count",
                        "LastPeriodValue": null,
                        "Unit": "",
                        "Value": 3
                    }
                ],
                "Tags": [
                    {
                        "Key": "tapm.instance.key",
                        "Value": "apm-ewyzCXlxj"
                    },
                    {
                        "Key": "instrumentation.name",
                        "Value": "com.fasterxml.jackson.core:jackson-databind"
                    },
                    {
                        "Key": "version",
                        "Value": "2.12.3"
                    },
                    {
                        "Key": "cve.id",
                        "Value": "CVE-2022-42003"
                    },
                    {
                        "Key": "vul.id",
                        "Value": "200008"
                    },
                    {
                        "Key": "level",
                        "Value": "important"
                    },
                    {
                        "Key": "score",
                        "Value": "7.50"
                    },
                    {
                        "Key": "vul.name",
                        "Value": "FasterXML jackson-databind 代码问题漏洞（CVE-2022-42003）"
                    }
                ]
            },
            {
                "Fields": [
                    {
                        "CompareVal": "",
                        "CompareVals": null,
                        "Key": "instance_count",
                        "LastPeriodValue": null,
                        "Unit": "",
                        "Value": 4
                    }
                ],
                "Tags": [
                    {
                        "Key": "tapm.instance.key",
                        "Value": "apm-21NwGgR53"
                    },
                    {
                        "Key": "instrumentation.name",
                        "Value": "com.fasterxml.jackson.core:jackson-databind"
                    },
                    {
                        "Key": "version",
                        "Value": "2.12.3"
                    },
                    {
                        "Key": "cve.id",
                        "Value": "CVE-2022-42004"
                    },
                    {
                        "Key": "vul.id",
                        "Value": "200009"
                    },
                    {
                        "Key": "level",
                        "Value": "important"
                    },
                    {
                        "Key": "score",
                        "Value": "7.50"
                    },
                    {
                        "Key": "vul.name",
                        "Value": "FasterXML jackson-databind 代码问题漏洞（CVE-2022-42004）"
                    }
                ]
            },
            {
                "Fields": [
                    {
                        "CompareVal": "",
                        "CompareVals": null,
                        "Key": "instance_count",
                        "LastPeriodValue": null,
                        "Unit": "",
                        "Value": 4
                    }
                ],
                "Tags": [
                    {
                        "Key": "tapm.instance.key",
                        "Value": "apm-avYdLEjHp"
                    },
                    {
                        "Key": "instrumentation.name",
                        "Value": "com.fasterxml.jackson.core:jackson-databind"
                    },
                    {
                        "Key": "version",
                        "Value": "2.12.3"
                    },
                    {
                        "Key": "cve.id",
                        "Value": "CVE-2022-42004"
                    },
                    {
                        "Key": "vul.id",
                        "Value": "200009"
                    },
                    {
                        "Key": "level",
                        "Value": "important"
                    },
                    {
                        "Key": "score",
                        "Value": "7.50"
                    },
                    {
                        "Key": "vul.name",
                        "Value": "FasterXML jackson-databind 代码问题漏洞（CVE-2022-42004）"
                    }
                ]
            },
            {
                "Fields": [
                    {
                        "CompareVal": "",
                        "CompareVals": null,
                        "Key": "instance_count",
                        "LastPeriodValue": null,
                        "Unit": "",
                        "Value": 3
                    }
                ],
                "Tags": [
                    {
                        "Key": "tapm.instance.key",
                        "Value": "apm-ewyzCXlxj"
                    },
                    {
                        "Key": "instrumentation.name",
                        "Value": "com.fasterxml.jackson.core:jackson-databind"
                    },
                    {
                        "Key": "version",
                        "Value": "2.12.3"
                    },
                    {
                        "Key": "cve.id",
                        "Value": "CVE-2020-36518"
                    },
                    {
                        "Key": "vul.id",
                        "Value": "200006"
                    },
                    {
                        "Key": "level",
                        "Value": "important"
                    },
                    {
                        "Key": "score",
                        "Value": "7.50"
                    },
                    {
                        "Key": "vul.name",
                        "Value": "FasterXML jackson-databind 缓冲区错误漏洞（CVE-2020-36518）"
                    }
                ]
            },
            {
                "Fields": [
                    {
                        "CompareVal": "",
                        "CompareVals": null,
                        "Key": "instance_count",
                        "LastPeriodValue": null,
                        "Unit": "",
                        "Value": 4
                    }
                ],
                "Tags": [
                    {
                        "Key": "tapm.instance.key",
                        "Value": "apm-21NwGgR53"
                    },
                    {
                        "Key": "instrumentation.name",
                        "Value": "com.fasterxml.jackson.core:jackson-databind"
                    },
                    {
                        "Key": "version",
                        "Value": "2.12.3"
                    },
                    {
                        "Key": "cve.id",
                        "Value": "CVE-2021-46877"
                    },
                    {
                        "Key": "vul.id",
                        "Value": "200007"
                    },
                    {
                        "Key": "level",
                        "Value": "important"
                    },
                    {
                        "Key": "score",
                        "Value": "7.50"
                    },
                    {
                        "Key": "vul.name",
                        "Value": "jackson-databind 拒绝服务漏洞（CVE-2021-46877）"
                    }
                ]
            },
            {
                "Fields": [
                    {
                        "CompareVal": "",
                        "CompareVals": null,
                        "Key": "instance_count",
                        "LastPeriodValue": null,
                        "Unit": "",
                        "Value": 4
                    }
                ],
                "Tags": [
                    {
                        "Key": "tapm.instance.key",
                        "Value": "apm-oJ7C40jYv"
                    },
                    {
                        "Key": "instrumentation.name",
                        "Value": "com.fasterxml.jackson.core:jackson-databind"
                    },
                    {
                        "Key": "version",
                        "Value": "2.12.3"
                    },
                    {
                        "Key": "cve.id",
                        "Value": "CVE-2021-46877"
                    },
                    {
                        "Key": "vul.id",
                        "Value": "200007"
                    },
                    {
                        "Key": "level",
                        "Value": "important"
                    },
                    {
                        "Key": "score",
                        "Value": "7.50"
                    },
                    {
                        "Key": "vul.name",
                        "Value": "jackson-databind 拒绝服务漏洞（CVE-2021-46877）"
                    }
                ]
            },
            {
                "Fields": [
                    {
                        "CompareVal": "",
                        "CompareVals": null,
                        "Key": "instance_count",
                        "LastPeriodValue": null,
                        "Unit": "",
                        "Value": 4
                    }
                ],
                "Tags": [
                    {
                        "Key": "tapm.instance.key",
                        "Value": "apm-oJ7C40jYv"
                    },
                    {
                        "Key": "instrumentation.name",
                        "Value": "com.fasterxml.jackson.core:jackson-databind"
                    },
                    {
                        "Key": "version",
                        "Value": "2.12.3"
                    },
                    {
                        "Key": "cve.id",
                        "Value": "CVE-2022-42003"
                    },
                    {
                        "Key": "vul.id",
                        "Value": "200008"
                    },
                    {
                        "Key": "level",
                        "Value": "important"
                    },
                    {
                        "Key": "score",
                        "Value": "7.50"
                    },
                    {
                        "Key": "vul.name",
                        "Value": "FasterXML jackson-databind 代码问题漏洞（CVE-2022-42003）"
                    }
                ]
            },
            {
                "Fields": [
                    {
                        "CompareVal": "",
                        "CompareVals": null,
                        "Key": "instance_count",
                        "LastPeriodValue": null,
                        "Unit": "",
                        "Value": 4
                    }
                ],
                "Tags": [
                    {
                        "Key": "tapm.instance.key",
                        "Value": "apm-21NwGgR53"
                    },
                    {
                        "Key": "instrumentation.name",
                        "Value": "com.fasterxml.jackson.core:jackson-databind"
                    },
                    {
                        "Key": "version",
                        "Value": "2.12.3"
                    },
                    {
                        "Key": "cve.id",
                        "Value": "CVE-2020-36518"
                    },
                    {
                        "Key": "vul.id",
                        "Value": "200006"
                    },
                    {
                        "Key": "level",
                        "Value": "important"
                    },
                    {
                        "Key": "score",
                        "Value": "7.50"
                    },
                    {
                        "Key": "vul.name",
                        "Value": "FasterXML jackson-databind 缓冲区错误漏洞（CVE-2020-36518）"
                    }
                ]
            },
            {
                "Fields": [
                    {
                        "CompareVal": "",
                        "CompareVals": null,
                        "Key": "instance_count",
                        "LastPeriodValue": null,
                        "Unit": "",
                        "Value": 4
                    }
                ],
                "Tags": [
                    {
                        "Key": "tapm.instance.key",
                        "Value": "apm-oJ7C40jYv"
                    },
                    {
                        "Key": "instrumentation.name",
                        "Value": "com.fasterxml.jackson.core:jackson-databind"
                    },
                    {
                        "Key": "version",
                        "Value": "2.12.3"
                    },
                    {
                        "Key": "cve.id",
                        "Value": "CVE-2022-42004"
                    },
                    {
                        "Key": "vul.id",
                        "Value": "200009"
                    },
                    {
                        "Key": "level",
                        "Value": "important"
                    },
                    {
                        "Key": "score",
                        "Value": "7.50"
                    },
                    {
                        "Key": "vul.name",
                        "Value": "FasterXML jackson-databind 代码问题漏洞（CVE-2022-42004）"
                    }
                ]
            },
            {
                "Fields": [
                    {
                        "CompareVal": "",
                        "CompareVals": null,
                        "Key": "instance_count",
                        "LastPeriodValue": null,
                        "Unit": "",
                        "Value": 1
                    }
                ],
                "Tags": [
                    {
                        "Key": "tapm.instance.key",
                        "Value": "apm-oJ7C40jYv"
                    },
                    {
                        "Key": "instrumentation.name",
                        "Value": "com.fasterxml.jackson.core:jackson-databind"
                    },
                    {
                        "Key": "version",
                        "Value": "2.13.0"
                    },
                    {
                        "Key": "cve.id",
                        "Value": "CVE-2022-42003"
                    },
                    {
                        "Key": "vul.id",
                        "Value": "200008"
                    },
                    {
                        "Key": "level",
                        "Value": "important"
                    },
                    {
                        "Key": "score",
                        "Value": "7.50"
                    },
                    {
                        "Key": "vul.name",
                        "Value": "FasterXML jackson-databind 代码问题漏洞（CVE-2022-42003）"
                    }
                ]
            },
            {
                "Fields": [
                    {
                        "CompareVal": "",
                        "CompareVals": null,
                        "Key": "instance_count",
                        "LastPeriodValue": null,
                        "Unit": "",
                        "Value": 1
                    }
                ],
                "Tags": [
                    {
                        "Key": "tapm.instance.key",
                        "Value": "apm-oJ7C40jYv"
                    },
                    {
                        "Key": "instrumentation.name",
                        "Value": "com.fasterxml.jackson.core:jackson-databind"
                    },
                    {
                        "Key": "version",
                        "Value": "2.13.0"
                    },
                    {
                        "Key": "cve.id",
                        "Value": "CVE-2022-42004"
                    },
                    {
                        "Key": "vul.id",
                        "Value": "200009"
                    },
                    {
                        "Key": "level",
                        "Value": "important"
                    },
                    {
                        "Key": "score",
                        "Value": "7.50"
                    },
                    {
                        "Key": "vul.name",
                        "Value": "FasterXML jackson-databind 代码问题漏洞（CVE-2022-42004）"
                    }
                ]
            },
            {
                "Fields": [
                    {
                        "CompareVal": "",
                        "CompareVals": null,
                        "Key": "instance_count",
                        "LastPeriodValue": null,
                        "Unit": "",
                        "Value": 1
                    }
                ],
                "Tags": [
                    {
                        "Key": "tapm.instance.key",
                        "Value": "apm-oJ7C40jYv"
                    },
                    {
                        "Key": "instrumentation.name",
                        "Value": "org.springframework.data:spring-data-commons"
                    },
                    {
                        "Key": "version",
                        "Value": "2.6.10"
                    },
                    {
                        "Key": "cve.id",
                        "Value": "CVE-2018-1259"
                    },
                    {
                        "Key": "vul.id",
                        "Value": "100356"
                    },
                    {
                        "Key": "level",
                        "Value": "important"
                    },
                    {
                        "Key": "score",
                        "Value": "7.50"
                    },
                    {
                        "Key": "vul.name",
                        "Value": "Spring Data 集成 XMLBeam存在XXE漏洞"
                    }
                ]
            },
            {
                "Fields": [
                    {
                        "CompareVal": "",
                        "CompareVals": null,
                        "Key": "instance_count",
                        "LastPeriodValue": null,
                        "Unit": "",
                        "Value": 4
                    }
                ],
                "Tags": [
                    {
                        "Key": "tapm.instance.key",
                        "Value": "apm-avYdLEjHp"
                    },
                    {
                        "Key": "instrumentation.name",
                        "Value": "com.fasterxml.jackson.core:jackson-databind"
                    },
                    {
                        "Key": "version",
                        "Value": "2.12.3"
                    },
                    {
                        "Key": "cve.id",
                        "Value": "CVE-2021-46877"
                    },
                    {
                        "Key": "vul.id",
                        "Value": "200007"
                    },
                    {
                        "Key": "level",
                        "Value": "important"
                    },
                    {
                        "Key": "score",
                        "Value": "7.50"
                    },
                    {
                        "Key": "vul.name",
                        "Value": "jackson-databind 拒绝服务漏洞（CVE-2021-46877）"
                    }
                ]
            },
            {
                "Fields": [
                    {
                        "CompareVal": "",
                        "CompareVals": null,
                        "Key": "instance_count",
                        "LastPeriodValue": null,
                        "Unit": "",
                        "Value": 4
                    }
                ],
                "Tags": [
                    {
                        "Key": "tapm.instance.key",
                        "Value": "apm-21NwGgR53"
                    },
                    {
                        "Key": "instrumentation.name",
                        "Value": "com.fasterxml.jackson.core:jackson-databind"
                    },
                    {
                        "Key": "version",
                        "Value": "2.12.3"
                    },
                    {
                        "Key": "cve.id",
                        "Value": "CVE-2022-42003"
                    },
                    {
                        "Key": "vul.id",
                        "Value": "200008"
                    },
                    {
                        "Key": "level",
                        "Value": "important"
                    },
                    {
                        "Key": "score",
                        "Value": "7.50"
                    },
                    {
                        "Key": "vul.name",
                        "Value": "FasterXML jackson-databind 代码问题漏洞（CVE-2022-42003）"
                    }
                ]
            },
            {
                "Fields": [
                    {
                        "CompareVal": "",
                        "CompareVals": null,
                        "Key": "instance_count",
                        "LastPeriodValue": null,
                        "Unit": "",
                        "Value": 4
                    }
                ],
                "Tags": [
                    {
                        "Key": "tapm.instance.key",
                        "Value": "apm-avYdLEjHp"
                    },
                    {
                        "Key": "instrumentation.name",
                        "Value": "com.fasterxml.jackson.core:jackson-databind"
                    },
                    {
                        "Key": "version",
                        "Value": "2.12.3"
                    },
                    {
                        "Key": "cve.id",
                        "Value": "CVE-2022-42003"
                    },
                    {
                        "Key": "vul.id",
                        "Value": "200008"
                    },
                    {
                        "Key": "level",
                        "Value": "important"
                    },
                    {
                        "Key": "score",
                        "Value": "7.50"
                    },
                    {
                        "Key": "vul.name",
                        "Value": "FasterXML jackson-databind 代码问题漏洞（CVE-2022-42003）"
                    }
                ]
            },
            {
                "Fields": [
                    {
                        "CompareVal": "",
                        "CompareVals": null,
                        "Key": "instance_count",
                        "LastPeriodValue": null,
                        "Unit": "",
                        "Value": 3
                    }
                ],
                "Tags": [
                    {
                        "Key": "tapm.instance.key",
                        "Value": "apm-ewyzCXlxj"
                    },
                    {
                        "Key": "instrumentation.name",
                        "Value": "com.fasterxml.jackson.core:jackson-databind"
                    },
                    {
                        "Key": "version",
                        "Value": "2.12.3"
                    },
                    {
                        "Key": "cve.id",
                        "Value": "CVE-2022-42004"
                    },
                    {
                        "Key": "vul.id",
                        "Value": "200009"
                    },
                    {
                        "Key": "level",
                        "Value": "important"
                    },
                    {
                        "Key": "score",
                        "Value": "7.50"
                    },
                    {
                        "Key": "vul.name",
                        "Value": "FasterXML jackson-databind 代码问题漏洞（CVE-2022-42004）"
                    }
                ]
            },
            {
                "Fields": [
                    {
                        "CompareVal": "",
                        "CompareVals": null,
                        "Key": "instance_count",
                        "LastPeriodValue": null,
                        "Unit": "",
                        "Value": 1
                    }
                ],
                "Tags": [
                    {
                        "Key": "tapm.instance.key",
                        "Value": "apm-oJ7C40jYv"
                    },
                    {
                        "Key": "instrumentation.name",
                        "Value": "com.fasterxml.jackson.core:jackson-databind"
                    },
                    {
                        "Key": "version",
                        "Value": "2.13.0"
                    },
                    {
                        "Key": "cve.id",
                        "Value": "CVE-2020-36518"
                    },
                    {
                        "Key": "vul.id",
                        "Value": "200006"
                    },
                    {
                        "Key": "level",
                        "Value": "important"
                    },
                    {
                        "Key": "score",
                        "Value": "7.50"
                    },
                    {
                        "Key": "vul.name",
                        "Value": "FasterXML jackson-databind 缓冲区错误漏洞（CVE-2020-36518）"
                    }
                ]
            },
            {
                "Fields": [
                    {
                        "CompareVal": "",
                        "CompareVals": null,
                        "Key": "instance_count",
                        "LastPeriodValue": null,
                        "Unit": "",
                        "Value": 4
                    }
                ],
                "Tags": [
                    {
                        "Key": "tapm.instance.key",
                        "Value": "apm-avYdLEjHp"
                    },
                    {
                        "Key": "instrumentation.name",
                        "Value": "com.fasterxml.jackson.core:jackson-databind"
                    },
                    {
                        "Key": "version",
                        "Value": "2.12.3"
                    },
                    {
                        "Key": "cve.id",
                        "Value": "CVE-2020-36518"
                    },
                    {
                        "Key": "vul.id",
                        "Value": "200006"
                    },
                    {
                        "Key": "level",
                        "Value": "important"
                    },
                    {
                        "Key": "score",
                        "Value": "7.50"
                    },
                    {
                        "Key": "vul.name",
                        "Value": "FasterXML jackson-databind 缓冲区错误漏洞（CVE-2020-36518）"
                    }
                ]
            }
        ]
    }
}
```

