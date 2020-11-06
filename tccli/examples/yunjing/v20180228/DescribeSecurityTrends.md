**Example 1: 获取安全事件统计数据**

获取安全事件统计数据。

Input: 

```
tccli yunjing DescribeSecurityTrends --cli-unfold-argument  \
    --BeginDate 2020-06-20 \
    --EndDate 2020-06-22
```

Output: 
```
{
    "Response": {
        "Malware": [
            {
                "Date": "2020-06-20",
                "EventNum": 301
            },
            {
                "Date": "2020-06-21",
                "EventNum": 301
            },
            {
                "Date": "2020-06-22",
                "EventNum": 311
            }
        ],
        "NonLocalLogin": [
            {
                "Date": "2020-06-20",
                "EventNum": 1
            },
            {
                "Date": "2020-06-21",
                "EventNum": 1
            },
            {
                "Date": "2020-06-22",
                "EventNum": 1
            }
        ],
        "BruteattackSuccess": [
            {
                "Date": "2020-06-20",
                "EventNum": 0
            },
            {
                "Date": "2020-06-21",
                "EventNum": 0
            },
            {
                "Date": "2020-06-22",
                "EventNum": 0
            }
        ],
        "Vul": [
            {
                "Date": "2020-06-20",
                "EventNum": 0
            },
            {
                "Date": "2020-06-21",
                "EventNum": 0
            },
            {
                "Date": "2020-06-22",
                "EventNum": 0
            }
        ],
        "Baseline": [
            {
                "Date": "2020-06-20",
                "EventNum": 8
            },
            {
                "Date": "2020-06-21",
                "EventNum": 8
            },
            {
                "Date": "2020-06-22",
                "EventNum": 8
            }
        ],
        "MaliciousRequest": [
            {
                "Date": "2020-06-20",
                "EventNum": 0
            },
            {
                "Date": "2020-06-21",
                "EventNum": 0
            },
            {
                "Date": "2020-06-22",
                "EventNum": 0
            }
        ],
        "HighRiskBash": [
            {
                "Date": "2020-06-20",
                "EventNum": 0
            },
            {
                "Date": "2020-06-21",
                "EventNum": 0
            },
            {
                "Date": "2020-06-22",
                "EventNum": 0
            }
        ],
        "ReverseShell": [
            {
                "Date": "2020-06-20",
                "EventNum": 0
            },
            {
                "Date": "2020-06-21",
                "EventNum": 0
            },
            {
                "Date": "2020-06-22",
                "EventNum": 0
            }
        ],
        "PrivilegeEscalation": [
            {
                "Date": "2020-06-20",
                "EventNum": 0
            },
            {
                "Date": "2020-06-21",
                "EventNum": 0
            },
            {
                "Date": "2020-06-22",
                "EventNum": 0
            }
        ],
        "CyberAttack": [
            {
                "Date": "2020-06-20",
                "EventNum": 0
            },
            {
                "Date": "2020-06-21",
                "EventNum": 0
            },
            {
                "Date": "2020-06-22",
                "EventNum": 0
            }
        ],
        "RequestId": "64643b63-303d-e52c-d262-38222e7dba8f"
    }
}
```

