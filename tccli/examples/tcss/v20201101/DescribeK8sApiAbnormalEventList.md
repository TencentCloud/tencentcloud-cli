**Example 1: 查询k8s api异常事件列表**



Input: 

```
tccli tcss DescribeK8sApiAbnormalEventList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AlarmCount": 1,
                "ClusterID": "cls-abhq0j4o-666",
                "ClusterName": "",
                "ClusterRunningStatus": "",
                "Desc": "检测到您的K8s API Server存在匿名用户访问请求，攻击者可利用匿名用户，通过API Server访问集群资源，如进入容器执行命令等。",
                "FirstCreateTime": "2024-10-22T11:00:45Z",
                "ID": 501472,
                "LastCreateTime": "2024-10-22T11:00:45Z",
                "MatchRule": {
                    "Action": "RULE_MODE_ALERT",
                    "IsDelete": false,
                    "RiskLevel": "HIGH",
                    "Scope": "{\"RequestUser\": \"system:anonymous\", \"RequestUserGroups\": \"system:anonymous\"}",
                    "Status": false
                },
                "MatchRuleType": "ANONYMOUS_ACCESS",
                "RiskLevel": "HIGH",
                "RuleName": "系统规则",
                "RuleType": "SYSTEM_DEFINED_RULE",
                "Status": "EVENT_UNDEAL",
                "Suggestion": "启用匿名用户存在较高的风险，建议您及时停用匿名用户，避免被攻击者利用；并排查来源IP和操作的资源是否属于正常运维操作。\n1、修改API Server 配置文件（如：/etc/kubernetes/manifests/kube-apiserver.yaml）将anonymous-auth改为false；并修改bind-address，避免监听在0.0.0.0，或使用安全组限制；去掉insecure-port配置。\n2、禁用kubelet的匿名认证功能，如去除kubelet服务配置文件中的anonymous-auth配置。\n建议修改配置前，确认是否为业务所需；在修改配置文件前，做好备份。"
            }
        ],
        "RequestId": "74b6dcb5-f38e-45f4-9f3f-be848b52466f",
        "TotalCount": 218
    }
}
```

