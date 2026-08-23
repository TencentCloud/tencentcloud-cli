**Example 1: 修改镜像木马白名单**



Input: 

```
tccli csip ModifyImageVirusWhitelist --cli-unfold-argument  \
    --RuleId 1 \
    --MemberId mem-12e1se11 \
    --Md5List 5FEC0F7****************BBF2E9B89 \
    --Scope 1 \
    --ImageIds 1 \
    --Remark 木马白名单
```

Output: 
```
{
    "Response": {
        "RequestId": "a6dde640-5779-4ee2-b652-5fe94e879147"
    }
}
```

