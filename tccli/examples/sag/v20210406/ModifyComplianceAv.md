**Example 1: 更改合规杀软配置**



Input: 

```
tccli sag ModifyComplianceAv --cli-unfold-argument  \
    --Os Windows \
    --AvName "MSE" \
    --AvVersion "" \
    --LibVersion "" \
    --CheckEnable 1
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx"
    }
}
```

