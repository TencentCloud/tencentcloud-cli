**Example 1: 解绑坐席所属技能组示例**



Input: 

```
tccli ccc UnbindStaffSkillGroupList --cli-unfold-argument  \
    --SdkAppId 1400000000 \
    --StaffEmail staff1@xxx.com \
    --SkillGroupList 100 101
```

Output: 
```
{
    "Response": {
        "RequestId": "48edd236-7ef1-45af-9e12-fc376ba355bf"
    }
}
```

