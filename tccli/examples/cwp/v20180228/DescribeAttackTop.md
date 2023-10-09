**Example 1: 网络攻击top统计数据**

网络攻击top统计数据

Input: 

```
tccli cwp DescribeAttackTop --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "NetAttackTopInfo": {
            "Agent": [
                {
                    "Count": 13,
                    "Value": "centreezhao-dev-centos8"
                }
            ],
            "DstPort": [
                {
                    "Count": 13,
                    "Value": "8080"
                }
            ],
            "SrcIp": [
                {
                    "Count": 5,
                    "Value": "10.0.0.14"
                },
                {
                    "Count": 5,
                    "Value": "10.0.0.5"
                },
                {
                    "Count": 3,
                    "Value": "127.0.0.1"
                }
            ],
            "Vul": [
                {
                    "Count": 13,
                    "Value": "Apache log4j2 远程代码执行漏洞 (CVE-2021-44228)"
                }
            ]
        },
        "RequestId": "e2b22aab-4ec5-447b-814b-0edcc7aa4465"
    }
}
```

