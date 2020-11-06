**Example 1: 修改弹性公网IP ACL**

此接口用于修改弹性公网IP ACL 名称、入/出站规则

Input: 

```
tccli bmeip ModifyEipAcl --cli-unfold-argument  \
    --AclId bmeipacl-s1hf4voq \
    --Type in \
    --Rules.0.Ip 8.8.8.8 \
    --Rules.0.Port 8080 \
    --Rules.0.Protocol tcp \
    --Rules.0.Action accept \
    --Rules.0.Description testrule
```

Output: 
```
{
    "Response": {
        "RequestId": "73ec9a84-2385-43ba-a00b-f27c619858ff"
    }
}
```

