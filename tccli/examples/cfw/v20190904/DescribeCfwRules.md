**Example 1: 查询 NAT 边界规则**

查询 NAT 边界 ACL；ExpandNames=false 返回原始规则字段，scope 是修改规则时需要保留的生效范围。

Input: 

```
tccli cfw DescribeCfwRules --cli-unfold-argument  \
    --RuleType nat \
    --ExpandNames False \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "Data": "{\"rule_type\":\"nat\",\"total\":1,\"returned\":1,\"rules\":[{\"sequence\":1,\"src_ip\":\"10.0.0.0/24\",\"dst_content\":\"0.0.0.0/0\",\"protocol\":\"TCP\",\"dst_port\":\"443\",\"scope\":\"ap-guangzhou\"}]}",
        "RequestId": "4266525E-10C4-41E1-8A28-5CCE1FBF6A58"
    }
}
```

**Example 2: 查询 VPC 间规则**

查询 VPC 间 ACL；ip_version 即使为 0 也会保留，修改规则时不得猜测或丢弃。

Input: 

```
tccli cfw DescribeCfwRules --cli-unfold-argument  \
    --RuleType vpc \
    --ExpandNames False \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "Data": "{\"rule_type\":\"vpc\",\"total\":1,\"returned\":1,\"rules\":[{\"sequence\":1,\"protocol\":\"TCP\",\"dst_port\":\"443\",\"ip_version\":0,\"enabled\":true}]}",
        "RequestId": "4266525E-10C4-41E1-8A28-5CCE1FBF6A58"
    }
}
```

**Example 3: 查询互联网边界规则**

查询互联网边界 ACL；Direction=0 表示出站，规则数组包含源、目的、协议、端口、动作和启用状态。

Input: 

```
tccli cfw DescribeCfwRules --cli-unfold-argument  \
    --RuleType border \
    --Direction 0 \
    --ExpandNames False \
    --Limit 100 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Data": "{\"rule_type\":\"border\",\"total\":1,\"returned\":1,\"rules\":[{\"sequence\":1,\"src_ip\":\"10.0.0.1\",\"dst_content\":\"0.0.0.0/0\",\"protocol\":\"TCP\",\"dst_port\":\"443\",\"direction\":0,\"action\":1,\"enabled\":true}]}",
        "RequestId": "4266525E-10C4-41E1-8A28-5CCE1FBF6A58"
    }
}
```

**Example 4: 查询企业安全组规则**

查询企业安全组规则；可使用 Protocol、SrcIp、DstIp 和 Description 继续过滤。

Input: 

```
tccli cfw DescribeCfwRules --cli-unfold-argument  \
    --RuleType enterprise_sg \
    --Protocol TCP \
    --ExpandNames False \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "Data": "{\"rule_type\":\"enterprise_sg\",\"total\":1,\"returned\":1,\"rules\":[{\"sequence\":1,\"protocol\":\"TCP\",\"dst_port\":\"443\",\"action\":1,\"enabled\":true}]}",
        "RequestId": "4266525E-10C4-41E1-8A28-5CCE1FBF6A58"
    }
}
```

**Example 5: 查询入侵防御封禁列表**

RuleType=intrusion_prevention 时通过 ListType 选择 blocklist、whitelist 或 isolate。

Input: 

```
tccli cfw DescribeCfwRules --cli-unfold-argument  \
    --RuleType intrusion_prevention \
    --ListType blocklist \
    --Keyword 1.1.1.1 \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "Data": "{\"rule_type\":\"intrusion_prevention\",\"list_type\":\"blocklist\",\"total\":1}",
        "RequestId": "4266525E-10C4-41E1-8A28-5CCE1FBF6A58"
    }
}
```

**Example 6: 查询入侵防御白名单策略**

查询入侵防御白名单策略，ListType 使用 whitelist。

Input: 

```
tccli cfw DescribeCfwRules --cli-unfold-argument  \
    --RuleType intrusion_prevention \
    --ListType whitelist \
    --Keyword safe.example.com \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "Data": "{\"rule_type\":\"intrusion_prevention\",\"list_type\":\"whitelist\",\"total\":1}",
        "RequestId": "4266525E-10C4-41E1-8A28-5CCE1FBF6A58"
    }
}
```

**Example 7: 查询入侵防御隔离列表**

按实例 ID 精确查询入侵防御隔离记录，用于写操作前后核验。

Input: 

```
tccli cfw DescribeCfwRules --cli-unfold-argument  \
    --RuleType intrusion_prevention \
    --ListType isolate \
    --InstanceId ins-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "Data": "{\"rule_type\":\"intrusion_prevention\",\"list_type\":\"isolate\",\"total\":1}",
        "RequestId": "4266525E-10C4-41E1-8A28-5CCE1FBF6A58"
    }
}
```

