**Example 1: 查询防火墙模板应用记录**

查询防火墙模板应用记录

Input: 

```
tccli lighthouse DescribeFirewallTemplateApplyRecords --cli-unfold-argument  \
    --TemplateId lhft-6brh0ciy
```

Output: 
```
{
    "Response": {
        "ApplyRecordSet": [
            {
                "ApplyDetailSet": [
                    {
                        "ApplyState": "SUCCESS",
                        "ErrorMessage": "",
                        "Instance": {
                            "InstanceId": "lhins-abcd1234",
                            "Region": "ap-guangzhou"
                        }
                    }
                ],
                "TaskId": "lgtk-dodi8tqa",
                "ApplyState": "SUCCESS",
                "ApplyTime": "2023-06-21T02:47:42Z",
                "FailedCount": 0,
                "RunningCount": 0,
                "SuccessCount": 1,
                "TemplateRuleSet": [
                    {
                        "FirewallRule": {
                            "Action": "ACCEPT",
                            "CidrBlock": "0.0.0.0/0",
                            "FirewallRuleDescription": "tcp 80",
                            "Port": "81",
                            "Protocol": "TCP"
                        },
                        "TemplateRuleId": "lhftr-gexf7cmvpq"
                    },
                    {
                        "FirewallRule": {
                            "Action": "DROP",
                            "CidrBlock": "0.0.0.0/0",
                            "FirewallRuleDescription": "udp 80",
                            "Port": "81",
                            "Protocol": "UDP"
                        },
                        "TemplateRuleId": "lhftr-9uxz9zuz62"
                    }
                ]
            }
        ],
        "RequestId": "cd7f9d77-c19b-4490-8d5e-42a776383f90"
    }
}
```

