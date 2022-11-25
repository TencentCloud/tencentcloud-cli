**Example 1: 查询k8s api 异常事件详情**



Input: 

```
tccli tcss DescribeK8sApiAbnormalEventInfo --cli-unfold-argument  \
    --ID 10
```

Output: 
```
{
    "Response": {
        "Info": {
            "Status": "xx",
            "MatchRuleName": "xx",
            "ClusterMasterIP": "xx",
            "MatchRule": {
                "Action": "xx",
                "Scope": "xx",
                "RiskLevel": "xx",
                "IsDelete": true,
                "Status": true
            },
            "ClusterRunningStatus": "xx",
            "K8sVersion": "xx",
            "RiskLevel": "xx",
            "ClusterID": "xx",
            "Suggestion": "xx",
            "HighLightFields": [
                "xx"
            ],
            "ClusterName": "xx",
            "MatchRuleID": "xx",
            "Info": "xx",
            "RunningComponent": [
                "xx"
            ],
            "FirstCreateTime": "xx",
            "MatchRuleType": "xx",
            "LastCreateTime": "xx",
            "AlarmCount": 1,
            "Desc": "xx"
        },
        "RequestId": "xx"
    }
}
```

