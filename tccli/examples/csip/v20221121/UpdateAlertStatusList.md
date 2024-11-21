**Example 1: 批量处理告警状态**



Input: 

```
tccli csip UpdateAlertStatusList --cli-unfold-argument  \
    --MemberId mem-tencent-4120f232321129 \
    --OperateType 3 \
    --ID.0.AppId 1235123242 \
    --ID.0.Type ActiveOutbound \
    --ID.0.SubType MaliciousRequest \
    --ID.0.Source CWP \
    --ID.0.Name 访问恶意地址或域名 \
    --ID.0.Key WRzIsdfMPkmukkUdsfsXfpZu \
    --ID.0.Date 2024-10-30T00:00:00+08:00
```

Output: 
```
{
    "Response": {
        "Code": "0",
        "Msg": "success",
        "RequestId": "fa5de592-7926-4e69-8ebe-00d1a7d6df55"
    }
}
```

