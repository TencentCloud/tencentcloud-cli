**Example 1: 云资源配置检测规则详情**



Input: 

```
tccli csip DescribeRiskRuleDetail --cli-unfold-argument  \
    --RiskRuleId tc_055
```

Output: 
```
{
    "Response": {
        "AssetType": "cos_bucket",
        "Provider": "tencent",
        "RiskFixAdvice": "W1t7IkRlc2NyaXB0aW9uIjogIueZu+W9lSDlr7nosaHlrZjlgqjmjqfliLblj7DvvIzlnKjlt6bkvqfoj5zljZXmoI/kuK3ljZXlh7vlrZjlgqjmobbliJfooajvvIzov5vlhaXlrZjlgqjmobbliJfooajpobXpnaLjgIIiLCAiSW1nVXJsIjogWyJodHRwczovL2Nsb3VkLXhzcG0tcmlzay1maXgtYWR2aWNlLTEyNTgzNDQ2OTkuY29zLmFwLWd1YW5nemhvdS50ZW5jZW50Y29zLmNuL2ltYWdlcy94c3BtX3Byb2QvY3J1aXNlcl9lMDY3MDliMmQ4ZjRjYTFlNGUxMGNjNzhjNGJlMjE1Yi5wbmciXX0sIHsiRGVzY3JpcHRpb24iOiAi5om+5Yiw5oKo6ZyA6KaB6K6+572u6Ziy55uX6ZO+55qE5a2Y5YKo5qG277yM5Y2V5Ye75YW25ZCN56ew77yM6L+b5YWl5a2Y5YKo5qG2566h55CG6aG16Z2i44CCIiwgIkltZ1VybCI6IFtdfSwgeyJEZXNjcmlwdGlvbiI6ICLljZXlh7vlronlhajnrqHnkIYgPiDpmLLnm5fpk77orr7nva7vvIzmib7liLDpmLLnm5fpk77orr7nva7vvIzljZXlh7vnvJbovpHov5vlhaXlj6/nvJbovpHnirbmgIHjgIIiLCAiSW1nVXJsIjogWyJodHRwczovL2Nsb3VkLXhzcG0tcmlzay1maXgtYWR2aWNlLTEyNTgzNDQ2OTkuY29zLmFwLWd1YW5nemhvdS50ZW5jZW50Y29zLmNuL2ltYWdlcy94c3BtX3Byb2QvY3J1aXNlcl8wZGM5NzhkYzMwYzk2ZDI3YjEzZDA0ZDYxNDcwYWM2Ni5wbmciXX0sIHsiRGVzY3JpcHRpb24iOiAi5pS55b2T5YmN54q25oCB5Li65byA5ZCv77yM6YCJ5oup5ZCN5Y2V57G75Z6L77yI6buR5ZCN5Y2V5oiW55m95ZCN5Y2V77yJ77yM6K6+572u5aW955u45bqU5Z+f5ZCN77yM6K6+572u5a6M5oiQ5ZCO5Y2V5Ye75L+d5a2Y5Y2z5Y+v44CCIiwgIkltZ1VybCI6IFsiaHR0cHM6Ly9jbG91ZC14c3BtLXJpc2stZml4LWFkdmljZS0xMjU4MzQ0Njk5LmNvcy5hcC1ndWFuZ3pob3UudGVuY2VudGNvcy5jbi9pbWFnZXMveHNwbV9wcm9kL2NydWlzZXJfYWE1ZWI2ODAwNWIxNDJmYzIxNjQwYTRhZmNmZTg5YjgucG5nIl19LCB7IkRlc2NyaXB0aW9uIjogIuWPr+WPguiAgyA8YSBocmVmPVwiaHR0cHM6Ly9jbG91ZC50ZW5jZW50LmNvbS9kb2N1bWVudC9wcm9kdWN0LzQzNi8xMzMxOVwiIHRhcmdldD1cIl9ibGFua1wiPmh0dHBzOi8vY2xvdWQudGVuY2VudC5jb20vZG9jdW1lbnQvcHJvZHVjdC80MzYvMTMzMTk8L2E+IOmhtemdoui/m+ihjOaTjeS9nOOAgiIsICJJbWdVcmwiOiBbXX1dXQ==",
        "RiskInfluence": "COS存储桶未开启防盗链配置，会导致恶意程序使用资源URL盗刷您的公网流量。",
        "RiskName": "COS存储桶未启用防盗链",
        "RiskRuleId": "tc_055",
        "RequestId": "d36e3e4c-bbd9-4df2-a5d3-222551da4326"
    }
}
```

