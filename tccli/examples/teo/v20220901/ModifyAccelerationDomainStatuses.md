**Example 1: 批量修改加速域名状态**

停用指定DomainId的加速域名。

Input: 

```
tccli teo ModifyAccelerationDomainStatuses --cli-unfold-argument  \
    --DomainNames example.com \
    --ZoneId zone-225qgrnvbi9w \
    --Status offline \
    --Force false
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707"
    }
}
```

