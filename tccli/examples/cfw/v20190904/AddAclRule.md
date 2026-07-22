**Example 1: 添加一条出站互联网边界观察规则**

使用 RFC 5737 文档地址添加一条出站串行 TCP 观察规则；显式指定启用状态、生效范围、规则来源和末尾优先级。

Input: 

```
tccli cfw AddAclRule --cli-unfold-argument  \
    --Rules.0.SourceContent 192.0.2.0/24 \
    --Rules.0.SourceType net \
    --Rules.0.TargetContent 198.51.100.10 \
    --Rules.0.TargetType net \
    --Rules.0.Protocol TCP \
    --Rules.0.RuleAction log \
    --Rules.0.Port 443 \
    --Rules.0.Direction 0 \
    --Rules.0.OrderIndex -1 \
    --Rules.0.Enable true \
    --Rules.0.Description 出站 TCP 观察示例 \
    --Rules.0.Scope serial \
    --Rules.0.RuleSource 0
```

Output: 
```
{
    "Response": {
        "RuleUuid": [
            100001
        ],
        "RequestId": "00000000-0000-4000-8000-000000000001"
    }
}
```

**Example 2: 添加一条入站地域来源规则**

添加一条入站串行 TCP 规则，来源使用地域 code；地域 code 应通过只读查询取得，示例中的 gd44 仅用于展示格式。

Input: 

```
tccli cfw AddAclRule --cli-unfold-argument  \
    --Rules.0.SourceContent gd44 \
    --Rules.0.SourceType location \
    --Rules.0.TargetContent 198.51.100.0/24 \
    --Rules.0.TargetType net \
    --Rules.0.Protocol TCP \
    --Rules.0.RuleAction accept \
    --Rules.0.Port 443 \
    --Rules.0.Direction 1 \
    --Rules.0.OrderIndex -1 \
    --Rules.0.Enable true \
    --Rules.0.Description 允许地域来源访问 HTTPS \
    --Rules.0.Scope serial \
    --Rules.0.RuleSource 0
```

Output: 
```
{
    "Response": {
        "RuleUuid": [
            100002
        ],
        "RequestId": "00000000-0000-4000-8000-000000000002"
    }
}
```

**Example 3: 插入一条旁路互联网边界规则**

使用 insert_rule 在指定位置插入一条禁用的出站旁路规则；调用前应查询当前出站规则顺序，并将 OrderIndex 替换为可用位置。

Input: 

```
tccli cfw AddAclRule --cli-unfold-argument  \
    --From insert_rule \
    --Rules.0.SourceContent 192.0.2.0/24 \
    --Rules.0.SourceType net \
    --Rules.0.TargetContent 198.51.100.10 \
    --Rules.0.TargetType net \
    --Rules.0.Protocol TCP \
    --Rules.0.RuleAction log \
    --Rules.0.Port 443 \
    --Rules.0.Direction 0 \
    --Rules.0.OrderIndex 3118 \
    --Rules.0.Enable false \
    --Rules.0.Description 插入旁路观察规则 \
    --Rules.0.Scope side \
    --Rules.0.RuleSource 0
```

Output: 
```
{
    "Response": {
        "RuleUuid": [
            100003
        ],
        "RequestId": "00000000-0000-4000-8000-000000000003"
    }
}
```

**Example 4: 批量导入两条全局互联网边界规则**

使用非覆盖的 batch_import 新增两条禁用的出站全局规则；该方式不会删除已有规则。

Input: 

```
tccli cfw AddAclRule --cli-unfold-argument  \
    --From batch_import \
    --Rules.0.SourceContent 192.0.2.1 \
    --Rules.0.SourceType net \
    --Rules.0.TargetContent 198.51.100.31 \
    --Rules.0.TargetType net \
    --Rules.0.Protocol TCP \
    --Rules.0.RuleAction log \
    --Rules.0.Port 443 \
    --Rules.0.Direction 0 \
    --Rules.0.OrderIndex -1 \
    --Rules.0.Enable false \
    --Rules.0.Description 批量全局规则一 \
    --Rules.0.Scope all \
    --Rules.0.RuleSource 0 \
    --Rules.1.SourceContent 192.0.2.2 \
    --Rules.1.SourceType net \
    --Rules.1.TargetContent 198.51.100.32 \
    --Rules.1.TargetType net \
    --Rules.1.Protocol TCP \
    --Rules.1.RuleAction log \
    --Rules.1.Port 8443 \
    --Rules.1.Direction 0 \
    --Rules.1.OrderIndex -1 \
    --Rules.1.Enable false \
    --Rules.1.Description 批量全局规则二 \
    --Rules.1.Scope all \
    --Rules.1.RuleSource 0
```

Output: 
```
{
    "Response": {
        "RuleUuid": [
            100004,
            100005
        ],
        "RequestId": "00000000-0000-4000-8000-000000000004"
    }
}
```

**Example 5: 使用地址模板新增互联网边界规则**

使用当前账号的原生 mb_ 地址模板 UUID 作为访问源；调用前应通过只读查询取得模板 UUID，不能直接写展示 ID。

Input: 

```
tccli cfw AddAclRule --cli-unfold-argument  \
    --Rules.0.SourceContent mb_1300448058_1702352890143 \
    --Rules.0.SourceType template \
    --Rules.0.TargetContent 198.51.100.60 \
    --Rules.0.TargetType net \
    --Rules.0.Protocol TCP \
    --Rules.0.RuleAction log \
    --Rules.0.Port 443 \
    --Rules.0.Direction 0 \
    --Rules.0.OrderIndex -1 \
    --Rules.0.Enable false \
    --Rules.0.Description 地址模板观察规则 \
    --Rules.0.Scope serial \
    --Rules.0.RuleSource 0
```

Output: 
```
{
    "Response": {
        "RuleUuid": [
            100006
        ],
        "RequestId": "00000000-0000-4000-8000-000000000005"
    }
}
```

