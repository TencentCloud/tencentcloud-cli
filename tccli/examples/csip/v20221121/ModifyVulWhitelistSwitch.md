**Example 1: 修改漏洞白名单开关**



Input: 

```
tccli csip ModifyVulWhitelistSwitch --cli-unfold-argument  \
    --Id 9 \
    --MemberId mem-tencent-6f5795752f66e429 \
    --Switch 0
```

Output: 
```
{
    "Response": {
        "RequestId": "cde1b8eb-8ea7-40ef-b1be-29b98633cc4b"
    }
}
```

