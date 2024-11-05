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
            "AlarmCount": 1,
            "ClusterID": "cls-abhq0j4o-666",
            "ClusterMasterIP": "10.0.1.92",
            "ClusterName": "clsfoo***",
            "ClusterRunningStatus": "CSR_RUN****",
            "Desc": "检测到您的K8s API Server存在匿名用户访问请求，攻击者可利用匿名用户，通过API Server访问集群资源，如进入容器执行命令等。",
            "FirstCreateTime": "2024-10-22T11:00:45Z",
            "HighLightFields": [
                "RequestUser"
            ],
            "Info": "{\"Verb\": \"list\", \"AuditID\": \"4e477a26-b171-4702-a2ac-1ac494ae8c85\", \"PodNameIP\": \"\", \"SourceIPS\": \"[\\\"10.0.0.4\\\"]\", \"UserAgent\": \"tcss_agent_cluster/v0.0.0 (linux/amd64) kubernetes/$Format\", \"RequestURI\": \"/api/v1/namespaces?limit=1\", \"RequestUser\": \"{\\\"groups\\\":\\\"[\\\\\\\"system:unauthenticated\\\\\\\"]\\\",\\\"uid\\\":\\\"\\\",\\\"username\\\":\\\"system:anonymous\\\"}\", \"MountHostDir\": \"\", \"RequestObject\": \"{\\\"metadata\\\":\\\"\\\"}\", \"ResponseObject\": \"{\\\"metadata\\\":\\\"\\\"}\", \"ResponseStatusCode\": \"200\"}",
            "K8sVersion": "1.0.1",
            "LastCreateTime": "2024-10-22T11:00:45Z",
            "MatchRule": {
                "Action": "RULE_MODE_ALERT",
                "IsDelete": false,
                "RiskLevel": "HIGH",
                "Scope": "{\"RequestUser\": \"system:anonymous\", \"RequestUserGroups\": \"system:anonymous\"}",
                "Status": false
            },
            "MatchRuleID": "SYSTEM",
            "MatchRuleName": "系统规则",
            "MatchRuleType": "ANONYMOUS_ACCESS",
            "RiskLevel": "HIGH",
            "RunningComponent": [],
            "Status": "EVENT_UNDEAL",
            "Suggestion": "启用匿名用户存在较高的风险，建议您及时停用匿名用户，避免被攻击者利用；并排查来源IP和操作的资源是否属于正常运维操作。\n1、修改API Server 配置文件（如：/etc/kubernetes/manifests/kube-apiserver.yaml）将anonymous-auth改为false；并修改bind-address，避免监听在0.0.0.0，或使用安全组限制；去掉insecure-port配置。\n2、禁用kubelet的匿名认证功能，如去除kubelet服务配置文件中的anonymous-auth配置。\n建议修改配置前，确认是否为业务所需；在修改配置文件前，做好备份。"
        },
        "RequestId": "8d8d41ab-6dfd-4f66-ad09-4a882485e733"
    }
}
```

