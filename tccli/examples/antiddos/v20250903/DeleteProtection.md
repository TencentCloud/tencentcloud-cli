**Example 1: 删除防护实例**

删除 ID 为 `prot-0004c045b8` 的防护实例。

Input: 

```
tccli antiddos DeleteProtection --cli-unfold-argument  \
    --ProtectionId prot-0004c045b8
```

Output: 
```
{
    "Response": {
        "RequestId": "9kl50bew-89ga-44f4-91ce-78125d53vd2a"
    }
}
```

