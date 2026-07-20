**Example 1: 添加互联网边界访问控制规则，资产分组类型**

添加互联网边界访问控制规则，资产分组类型，其中资产分组d为cfwrg_开头形式，由接口DescribeResourceGroupNew可以查询所得资产分组id

Input: 

```
tccli cfw AddAclRule --cli-unfold-argument  \
    --Rules.0.SourceContent cfwrg-b002b9b9d71b1a63951da2059d78cef41744255370 \
    --Rules.0.SourceType group \
    --Rules.0.TargetContent mb_1300448058_1740510699974 \
    --Rules.0.TargetType template \
    --Rules.0.Protocol TCP \
    --Rules.0.RuleAction accept \
    --Rules.0.Port -1/-1 \
    --Rules.0.Direction 0 \
    --Rules.0.OrderIndex 1 \
    --Rules.0.Enable true \
    --Rules.0.Description rule-pro \
    --Rules.0.Scope serial
```

Output: 
```
{
    "Response": {
        "RequestId": "278cabc7-b282-4ec8-a5b1-89d1e38195df",
        "RuleUuid": [
            1907269
        ]
    }
}
```

