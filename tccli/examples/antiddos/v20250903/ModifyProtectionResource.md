**Example 1: 向防护实例追加绑定 EIP 防护资源**

向防护实例 `prot-0004c045b8` 追加绑定两个 EIP 作为防护资源。

Input: 

```
tccli antiddos ModifyProtectionResource --cli-unfold-argument  \
    --ProtectionId prot-0004c045b8 \
    --Mode APPEND \
    --Resources qcs::cvm:ap-guangzhou:uin/164256472:eip/eip-1a2b3c4d qcs::cvm:ap-guangzhou:uin/164256472:eip/eip-5e6f7g8h
```

Output: 
```
{
    "Response": {
        "RequestId": "9kl50bew-89ga-44f4-91ce-78125d53vd2a"
    }
}
```

**Example 2: 更新防护实例的防护资源列表**

将防护实例 `prot-0004c045b8` 的防护资源更新为一个 CLB 实例，若该资源已绑定至其他防护实例则强制绑定。

Input: 

```
tccli antiddos ModifyProtectionResource --cli-unfold-argument  \
    --ProtectionId prot-0004c045b8 \
    --Mode UPDATE \
    --Resources qcs::clb:ap-guangzhou:uin/164256472:clb/lb-1a2b3c4d \
    --ConflictStrategy FORCE
```

Output: 
```
{
    "Response": {
        "RequestId": "ea95fca6-715c-4995-9680-2b72b394a2cb"
    }
}
```

