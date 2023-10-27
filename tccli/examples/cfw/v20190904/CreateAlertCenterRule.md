**Example 1: 攻击告警汇总示例**

攻击告警汇总-封禁IP示例

Input: 

```
tccli cfw CreateAlertCenterRule --cli-unfold-argument  \
    --HandleIdList a67d60bb5ede9b962ac19ad24b28be54 \
    --HandleTime 7 \
    --HandleType 1 \
    --AlertDirection 1 \
    --HandleDirection 1 \
    --HandleComment test
```

Output: 
```
{
    "Response": {
        "RequestId": "9cddfe10-cbf2-4dd8-ba39-dd8488bb8a42",
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "Status": 0
    }
}
```

**Example 2: 攻击拦截统计示例**

攻击拦截统计-封禁IP示例

Input: 

```
tccli cfw CreateAlertCenterRule --cli-unfold-argument  \
    --HandleIpList 192.155.90.220 \
    --HandleTime 7 \
    --HandleType 3 \
    --AlertDirection 0 \
    --HandleDirection 0 \
    --HandleComment test
```

Output: 
```
{
    "Response": {
        "RequestId": "9ff0c548-66c4-4989-8e6e-c616a1340d84",
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "Status": 0
    }
}
```

