**Example 1: 查询告警历史**

查询告警历史

Input: 

```
tccli tke DescribePrometheusAlertHistory --cli-unfold-argument  \
    --InstanceId prom-adsdfdsf \
    --RuleName test
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "Content": "pod发生重启",
                "StartTime": "2021-02-19 16:51:44",
                "RuleName": "test"
            }
        ],
        "Total": 1,
        "RequestId": "7ef8496c-b966-4c23-b160-dsadahsjf12ehjh"
    }
}
```

