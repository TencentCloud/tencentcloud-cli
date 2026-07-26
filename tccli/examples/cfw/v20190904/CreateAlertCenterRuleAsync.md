**Example 1: Event 封禁**

使用 HandleEventIdList 封禁告警事件。

Input: 

```
tccli cfw CreateAlertCenterRuleAsync --cli-unfold-argument  \
    --HandleTime 7 \
    --HandleType 1 \
    --AlertDirection 0 \
    --HandleDirection 0 \
    --HandleEventIdList event-example-block-001
```

Output: 
```
{
    "Response": {
        "RequestId": "00000000-0000-4000-8000-000000000001",
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "Status": 0
    }
}
```

**Example 2: Event 加白**

使用 HandleEventIdList 加白告警事件；IgnoreReason=2 表示误报。

Input: 

```
tccli cfw CreateAlertCenterRuleAsync --cli-unfold-argument  \
    --HandleTime 7 \
    --HandleType 2 \
    --AlertDirection 0 \
    --HandleDirection 1 \
    --IgnoreReason 2 \
    --HandleEventIdList event-example-allow-001
```

Output: 
```
{
    "Response": {
        "RequestId": "00000000-0000-4000-8000-000000000002",
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "Status": 0
    }
}
```

**Example 3: IP 封禁**

使用 HandleIpList 封禁一个 IP。

Input: 

```
tccli cfw CreateAlertCenterRuleAsync --cli-unfold-argument  \
    --HandleTime 1 \
    --HandleType 4 \
    --AlertDirection 0 \
    --HandleDirection 0 \
    --HandleIpList 192.0.2.10
```

Output: 
```
{
    "Response": {
        "RequestId": "00000000-0000-4000-8000-000000000003",
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "Status": 0
    }
}
```

**Example 4: IP 加白**

使用 HandleIpList 加白一个 IP。

Input: 

```
tccli cfw CreateAlertCenterRuleAsync --cli-unfold-argument  \
    --HandleTime 7 \
    --HandleType 3 \
    --AlertDirection 1 \
    --HandleDirection 1 \
    --IgnoreReason 2 \
    --HandleIpList 198.51.100.20
```

Output: 
```
{
    "Response": {
        "RequestId": "00000000-0000-4000-8000-000000000004",
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "Status": 0
    }
}
```

**Example 5: 域名加白**

使用 BlockDomain 加白一个域名，并通过 TargetEventIdList 关联来源事件。

Input: 

```
tccli cfw CreateAlertCenterRuleAsync --cli-unfold-argument  \
    --HandleTime 7 \
    --HandleType 2 \
    --AlertDirection 0 \
    --HandleDirection 0 \
    --IgnoreReason 2 \
    --BlockDomain security.example \
    --TargetEventIdList event-id-domain-001
```

Output: 
```
{
    "Response": {
        "RequestId": "00000000-0000-4000-8000-000000000005",
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "Status": 0
    }
}
```

**Example 6: 将安全基线告警地址加入基线列表**

仅用于安全基线告警。将告警日志对应的 IP 地址或域名加入 HandleDirection 指定方向的安全基线列表；后续匹配访问不再触发安全基线告警，但仍可能触发其他入侵防御告警。这不是创建安全基线策略，也不是加入普通放通列表。HandleIdList 使用 DescribeLogs 返回的 log_id；也可改用 HandleEventIdList 并传入 DescribeCfwAlerts 返回的告警事件 ID。

Input: 

```
tccli cfw CreateAlertCenterRuleAsync --cli-unfold-argument  \
    --HandleTime -2 \
    --HandleType 5 \
    --AlertDirection 1 \
    --HandleDirection 1 \
    --HandleIdList log-example-baseline-001
```

Output: 
```
{
    "Response": {
        "RequestId": "00000000-0000-4000-8000-000000000009",
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "Status": 0
    }
}
```

**Example 7: 隔离资产的互联网入站访问**

使用 DescribeCfwAssets 唯一确认的实例 ID 隔离资产；IsolateType=1 表示隔离互联网入站访问，HandleTime=1 表示持续 1 天。隔离会影响资产通信，请在调用前确认实例和隔离范围。

Input: 

```
tccli cfw CreateAlertCenterRuleAsync --cli-unfold-argument  \
    --HandleTime 1 \
    --HandleType 8 \
    --AlertDirection 0 \
    --HandleDirection 0 \
    --AssetIdList ins-example-isolate-001 \
    --IsolateType 1
```

Output: 
```
{
    "Response": {
        "RequestId": "00000000-0000-4000-8000-000000000010",
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "Status": 0
    }
}
```

