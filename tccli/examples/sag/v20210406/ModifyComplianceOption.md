**Example 1: 修改合规选项卡配置**



Input: 

```
tccli sag ModifyComplianceOption --cli-unfold-argument  \
    --Os Windows \
    --Name "ioa" \
    --CheckEnable 1 \
    --RiskLevel 3
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx"
    }
}
```

