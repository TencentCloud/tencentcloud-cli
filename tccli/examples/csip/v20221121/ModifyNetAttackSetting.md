**Example 1: 修改**



Input: 

```
tccli csip ModifyNetAttackSetting --cli-unfold-argument  \
    --NetAttackEnable 1 \
    --MemberId mem-tencent-b624e485fee5fe29 \
    --NetAttackAlarmStatus 1 \
    --AutoInclude 1 \
    --CWPScope 0 \
    --TagIDs 1 \
    --TCSSScope 0
```

Output: 
```
{
    "Response": {
        "RequestId": "bc888f22-c7c8-4fa5-9e17-2e989c2b0416"
    }
}
```

