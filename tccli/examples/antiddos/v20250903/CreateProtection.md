**Example 1: 创建防护实例**

创建一个名为 `protection_name`、防护级别为增强防护的防护实例，并为其绑定业务标签。

Input: 

```
tccli antiddos CreateProtection --cli-unfold-argument  \
    --Name protection_name \
    --ProtectionLevel advanced \
    --Tags.0.TagKey env \
    --Tags.0.TagValue production
```

Output: 
```
{
    "Response": {
        "ProtectionId": "prot-0004c045b8",
        "RequestId": "9kl50bew-89ga-44f4-91ce-78125d53vd2a"
    }
}
```

