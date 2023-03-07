**Example 1: 检测规则视角**



Input: 

```
tccli cwp DescribeBaselineRuleDetectList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "RuleId": 125,
                "RuleName": "信息泄露基线检查",
                "RuleDesc": "信息泄露基线检查",
                "ItemCount": 5,
                "HostCount": 36,
                "FirstTime": "2022-05-11 01:03:35",
                "LastTime": "2022-08-23 09:48:19",
                "DetectStatus": 0,
                "ItemIds": [
                    1900,
                    1901,
                    1902,
                    1903,
                    1904
                ]
            },
            {
                "RuleId": 124,
                "RuleName": "Nginx安全基线检查",
                "RuleDesc": "Nginx安全基线检查",
                "ItemCount": 6,
                "HostCount": 36,
                "FirstTime": "2022-05-11 01:03:35",
                "LastTime": "2022-08-23 10:48:36",
                "DetectStatus": 0,
                "ItemIds": [
                    1800,
                    1801,
                    1802,
                    1803,
                    1804,
                    1805
                ]
            },
            {
                "RuleId": 120,
                "RuleName": "MongoDB安全基线检查",
                "RuleDesc": "MongoDB安全基线检查",
                "ItemCount": 4,
                "HostCount": 36,
                "FirstTime": "2022-05-11 01:03:35",
                "LastTime": "2022-08-23 09:48:19",
                "DetectStatus": 3,
                "ItemIds": [
                    1400,
                    1401,
                    1402,
                    1403
                ]
            },
            {
                "RuleId": 74,
                "RuleName": "Kubelet 未授权访问",
                "RuleDesc": "Kubelet 未授权访问",
                "ItemCount": 1,
                "HostCount": 34,
                "FirstTime": "2022-05-11 17:07:31",
                "LastTime": "2022-08-23 09:48:19",
                "DetectStatus": 3,
                "ItemIds": [
                    1001
                ]
            },
            {
                "RuleId": 51,
                "RuleName": "MySQL 弱口令检测",
                "RuleDesc": "MySQL 弱口令检测",
                "ItemCount": 1,
                "HostCount": 34,
                "FirstTime": "2022-05-11 01:03:35",
                "LastTime": "2022-08-23 09:48:19",
                "DetectStatus": 0,
                "ItemIds": [
                    1103
                ]
            },
            {
                "RuleId": 52,
                "RuleName": "Tomcat 弱口令检测",
                "RuleDesc": "Tomcat 弱口令检测",
                "ItemCount": 1,
                "HostCount": 34,
                "FirstTime": "2022-05-11 01:03:35",
                "LastTime": "2022-08-23 09:48:19",
                "DetectStatus": 3,
                "ItemIds": [
                    1101
                ]
            },
            {
                "RuleId": 70,
                "RuleName": "CouchDB未授权访问",
                "RuleDesc": "CouchDB未授权访问",
                "ItemCount": 1,
                "HostCount": 34,
                "FirstTime": "2022-05-11 17:07:31",
                "LastTime": "2022-08-23 09:48:19",
                "DetectStatus": 3,
                "ItemIds": [
                    1005
                ]
            },
            {
                "RuleId": 71,
                "RuleName": "Elasticsearch未授权访问",
                "RuleDesc": "Elasticsearch未授权访问",
                "ItemCount": 1,
                "HostCount": 34,
                "FirstTime": "2022-05-11 17:07:31",
                "LastTime": "2022-08-23 09:48:19",
                "DetectStatus": 3,
                "ItemIds": [
                    1004
                ]
            },
            {
                "RuleId": 58,
                "RuleName": "ActiveMQ基线合规检测",
                "RuleDesc": "ActiveMQ基线合规检测",
                "ItemCount": 1,
                "HostCount": 34,
                "FirstTime": "2022-05-11 01:03:35",
                "LastTime": "2022-08-23 09:48:19",
                "DetectStatus": 3,
                "ItemIds": [
                    1108
                ]
            },
            {
                "RuleId": 72,
                "RuleName": "MongoDB未授权访问",
                "RuleDesc": "MongoDB未授权访问",
                "ItemCount": 1,
                "HostCount": 33,
                "FirstTime": "2022-05-11 17:07:31",
                "LastTime": "2022-08-23 09:48:19",
                "DetectStatus": 3,
                "ItemIds": [
                    1003
                ]
            }
        ],
        "RequestId": "55a2919d-7bd6-4220-b347-cb9cfca9dd6c",
        "Total": 70
    }
}
```

