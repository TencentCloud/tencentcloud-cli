**Example 1: 修改源站组名称**

修改源站组名称为edgeone-new-origin

Input: 

```
tccli teo ModifyOriginGroup --cli-unfold-argument  \
    --ZoneId zone-2kblak89bkx1 \
    --GroupId origin-df19b73e-3a4c-11ee-a68f-5254000a367f \
    --Name edgeone-rename-origin
```

Output: 
```
{
    "Response": {
        "RequestId": "c2886bcd-173f-499e-b425-022ceaf636d8"
    }
}
```

**Example 2: 修改源站组记录**

修改源站组记录，新源站记录将覆盖旧源站组中的源站记录。

Input: 

```
tccli teo ModifyOriginGroup --cli-unfold-argument  \
    --ZoneId zone-2nrle17s0v0r \
    --GroupId origin-afbce0e9-6e8a-11ee-8944-52540084caf1 \
    --Records.0.Record 2.2.2.2 \
    --Records.0.Type IP_DOMAIN \
    --Records.1.Record 3.3.3.3 \
    --Records.1.Type IP_DOMAIN
```

Output: 
```
{
    "Response": {
        "RequestId": "39f96a44-9a52-4a9f-8b76-4ccc9e496f40"
    }
}
```

