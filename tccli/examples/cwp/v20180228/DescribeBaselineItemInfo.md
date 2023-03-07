**Example 1: 检测项信息**



Input: 

```
tccli cwp DescribeBaselineItemInfo --cli-unfold-argument  \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "ItemId": 1001,
                "ItemName": "Kubelet 未授权访问",
                "RuleId": 74,
                "ItemDesc": "Kubelet 未限制访问来源且未配置任何认证，导致攻击者可以在任意 Pod 中执行任意代码。也可以造成 Pod 泄漏导致敏感信息泄漏等。",
                "FixMethod": "1. kubelet 监听在本地：\n--address=127.0.0.1\n\n2. kubelet server 禁止匿名访问：\n--anonymous-auth=false\n\n如果已经通过防火墙等方式对端口访问进行限制，请忽略。\n\n3. 配置证书：\n--client-ca-file=path/to/ca\n--kubelet-client-certificate\n--kubelet-client-key",
                "RuleName": "Kubelet 未授权访问",
                "Level": 3,
                "SysRuleId": 74,
                "RelatedCustomRuleInfo": []
            }
        ],
        "RequestId": "90344239-519c-4f7f-8a71-1820d38e163c",
        "Total": 2955
    }
}
```

