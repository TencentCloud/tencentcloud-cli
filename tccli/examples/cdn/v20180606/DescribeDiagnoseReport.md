**Example 1: 获取诊断报告**



Input: 

```
tccli cdn DescribeDiagnoseReport --cli-unfold-argument  \
    --ReportId 123
```

Output: 
```
{
    "Response": {
        "RequestId": "b3eee570-0d5f-46b2-89a3-160f4e654eaf",
        "BaskInfo": {
            "Data": [
                {
                    "Key": "report_id",
                    "KeyText": "报告ID",
                    "Value": "123",
                    "ValueText": "123"
                },
                {
                    "Key": "diagnose_url",
                    "KeyText": "诊断URL",
                    "Value": "http://www.test.com/1.txt",
                    "ValueText": "http://www.test.com/1.txt"
                },
                {
                    "Key": "diagnose_time",
                    "KeyText": "诊断时间",
                    "Value": "2020-09-21 12:00:16",
                    "ValueText": "2020-09-21 12:00:16"
                }
            ],
            "Status": "ok"
        },
        "CnameInfo": {
            "Status": "ok",
            "Data": [
                {
                    "Key": "cname",
                    "KeyText": "解析配置",
                    "Value": "CNAMEu2003www.test.com.cdn.dnsv1.com<br>",
                    "ValueText": "CNAMEu2003www.test.com.cdn.dnsv1.com<br>"
                }
            ]
        },
        "ClientInfo": {
            "Status": "ok",
            "Data": [
                {
                    "Key": "ip",
                    "KeyText": "客户端IP",
                    "Value": "1.1.1.1",
                    "ValueText": "1.1.1.1"
                },
                {
                    "Key": "prov_isp",
                    "KeyText": "所在区域",
                    "Value": "广东省-中国电信",
                    "ValueText": "广东省-中国电信"
                },
                {
                    "Key": "request",
                    "KeyText": "请求详情",
                    "Value": "--",
                    "ValueText": "--"
                }
            ]
        },
        "DnsInfo": {
            "Data": [
                {
                    "Key": "dns",
                    "KeyText": "DNS IP",
                    "Value": "183.3.229.15u2003广东省-中国电信<br>219.133.40.12u2003广东省-中国电信<br>",
                    "ValueText": "183.3.229.15u2003广东省-中国电信<br>219.133.40.12u2003广东省-中国电信<br>"
                }
            ],
            "Status": "ok"
        },
        "NetworkInfo": {
            "Status": "ok",
            "Data": [
                {
                    "Key": "network",
                    "KeyText": "探测延迟",
                    "Value": "123ms",
                    "ValueText": "123ms"
                }
            ]
        },
        "OcNodeInfo": {
            "Status": "error",
            "Data": [
                {
                    "Key": "ip",
                    "KeyText": "节点IP",
                    "Value": "--",
                    "ValueText": "--"
                },
                {
                    "Key": "area",
                    "KeyText": "所在区域",
                    "Value": "--",
                    "ValueText": "--"
                },
                {
                    "Key": "code",
                    "KeyText": "状态码",
                    "Value": "--",
                    "ValueText": "--"
                },
                {
                    "Key": "md5",
                    "KeyText": "文件MD5",
                    "Value": "--",
                    "ValueText": "--"
                },
                {
                    "Key": "hit",
                    "KeyText": "命中情况",
                    "Value": "--",
                    "ValueText": "--"
                },
                {
                    "Key": "solution",
                    "KeyText": "解决方案",
                    "Value": "--",
                    "ValueText": "--"
                }
            ]
        },
        "MidNodeInfo": {
            "Data": [
                {
                    "Key": "ip",
                    "KeyText": "节点IP",
                    "Value": "--",
                    "ValueText": "--"
                },
                {
                    "Key": "area",
                    "KeyText": "所在区域",
                    "Value": "--",
                    "ValueText": "--"
                },
                {
                    "Key": "hit",
                    "KeyText": "命中情况",
                    "Value": "--",
                    "ValueText": "--"
                }
            ],
            "Status": "initial"
        },
        "OriginInfo": {
            "Status": "initial",
            "Data": [
                {
                    "Key": "ip",
                    "KeyText": "源站IP",
                    "Value": "--",
                    "ValueText": "--"
                },
                {
                    "Key": "area",
                    "KeyText": "所在区域",
                    "Value": "--",
                    "ValueText": "--"
                },
                {
                    "Key": "fwd_host",
                    "KeyText": "回源host",
                    "Value": "--",
                    "ValueText": "--"
                },
                {
                    "Key": "code",
                    "KeyText": "状态码",
                    "Value": "--",
                    "ValueText": "--"
                },
                {
                    "Key": "md5",
                    "KeyText": "文件MD5",
                    "Value": "--",
                    "ValueText": "--"
                }
            ]
        },
        "PurgeInfo": {
            "Status": "ok",
            "Data": [
                {
                    "Key": "purge",
                    "KeyText": "刷新详情",
                    "Value": "检测中",
                    "ValueText": "检测中"
                },
                {
                    "Key": "solution",
                    "KeyText": "解决方案",
                    "Value": "无需检测",
                    "ValueText": "无需检测"
                }
            ]
        }
    }
}
```

