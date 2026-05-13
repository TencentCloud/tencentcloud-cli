**Example 1: 创建Dspm个人身份id**



Input: 

```
tccli csip CreateDspmPersonalIdentify --cli-unfold-argument  \
    --Phone 17790000000 \
    --Name 张三 \
    --Remark 
```

Output: 
```
{
    "Response": {
        "PersonId": "pid_cd0b2mdj",
        "IdentifyId": "dspm_c1d0b2mdj2",
        "RequestId": "45ca21d4-f373-4274-9295-5380abc74bed"
    }
}
```

