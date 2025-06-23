**Example 1: 添加互联网边界访问控制规则**

添加互联网边界访问控制规则

Input: 

```
tccli cfw AddAclRule --cli-unfold-argument  \
    --Rules.0.SourceContent 0.0.0.0/0 \
    --Rules.0.SourceType net \
    --Rules.0.Description pro \
    --Rules.0.TargetContent www.qq.com \
    --Rules.0.TargetType domain \
    --Rules.0.Protocol HTTP \
    --Rules.0.RuleAction accept \
    --Rules.0.Port -1/-1 \
    --Rules.0.Direction 0 \
    --Rules.0.OrderIndex 1 \
    --Rules.0.Scope serial \
    --Rules.0.RuleSource 0
```

Output: 
```
{
    "Response": {
        "RuleUuid": [
            0
        ],
        "RequestId": "3f60a76f-0f44-4b58-bf98-615cbbc59ede"
    }
}
```

**Example 2: 添加互联网边界访问控制规则，模板类型**

添加互联网边界访问控制规则，模板类型，其中模板id为mb_开头形式，由接口DescribeAddressTemplateList 可以查询所得模板

Input: 

```
tccli cfw AddAclRule --cli-unfold-argument  \
    --Rules.0.SourceContent mb_1256532032_1655200956209 \
    --Rules.0.SourceType template \
    --Rules.0.TargetContent mb_1300448058_1740510699974 \
    --Rules.0.TargetType template \
    --Rules.0.Protocol TCP \
    --Rules.0.RuleAction accept \
    --Rules.0.Port -1/-1 \
    --Rules.0.Direction 0 \
    --Rules.0.OrderIndex 1 \
    --Rules.0.Enable true \
    --Rules.0.Description test \
    --Rules.0.Scope serial
```

Output: 
```
{
    "Response": {
        "RequestId": "6d6b877f-9a5f-4da2-876d-9968c9fe0491",
        "RuleUuid": [
            1907266
        ]
    }
}
```

**Example 3: 添加互联网边界访问控制规则，资产分组类型**

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

