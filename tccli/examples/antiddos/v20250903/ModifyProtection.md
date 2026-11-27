**Example 1: 修改防护实例的名称**

将防护实例 `prot-0004c045b8` 的名称修改为 `new_protection_name`。

Input: 

```
tccli antiddos ModifyProtection --cli-unfold-argument  \
    --ProtectionId prot-0004c045b8 \
    --Name new_protection_name
```

Output: 
```
{
    "Response": {
        "RequestId": "9kl50bew-89ga-44f4-91ce-78125d53vd2a"
    }
}
```

