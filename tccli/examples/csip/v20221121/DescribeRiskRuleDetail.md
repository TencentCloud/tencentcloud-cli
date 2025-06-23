**Example 1: 查询风险规则详情**



Input: 

```
tccli csip DescribeRiskRuleDetail --cli-unfold-argument  \
    --RiskRuleId tc_001
```

Output: 
```
{
    "Response": {
        "Provider": "tencent",
        "RequestId": "94fe20c6-ea21-4d00-a765-6c0cf133031f",
        "RiskFixAdvice": "W1t7IkRlc2NyaXB0aW9uIjogIuaCqOWPr+S7peWPguiAg+aIkeS7rOaPkOS+m+eahOivpuaDheWIl+ihqO+8jOaOqOi/m+a8j+a0nuS/ruWkjeOAguS5n+WPr+S7peiuv+mXruiFvuiur+S6keKAnOS4u+acuuWuieWFqOKAneKAlOKAlOKAnOa8j+a0nueuoeeQhuKAnemhtemdou+8jOadpeS6huino+a8j+a0nuaVsOaNruOAgiIsICJJbWdVcmwiOiBbImh0dHBzOi8vY2xvdWQteHNwbS1yaXNrLWZpeC1hZHZpY2UtMTI1ODM0NDY5OS5jb3MuYXAtZ3Vhbmd6aG91LnRlbmNlbnRjb3MuY24vaW1hZ2VzL3hzcG1fcHJlL2NydWlzZXJfODE3MTE0MjM4Mjg5ZmVjZjc0OGExYzY3OWZhZmE3NGMuanBlZyJdfV0sIFt7IkRlc2NyaXB0aW9uIjogIuiwg+aVtOS4u+acuuWuieWFqOa8j+a0nuKAnOS7heWxleekuumrmOS8mOS/ruWkjea8j+a0nuKAneaWueahiOOAguiuv+mXruiFvuiur+S6keKAnOS4u+acuuWuieWFqOKAneKAlOKAlOKAnOa8j+a0nueuoeeQhuKAnemhtemdou+8jOWIh+aNouiHs+KAnOWFqOmDqOa8j+a0nuKAnVRhYumhte+8jOaJk+W8gOKAnOS7heWxleekuumrmOS8mOS/ruWkjea8j+a0nuKAneW8gOWFs+WNs+WPr+OAgiIsICJJbWdVcmwiOiBbImh0dHBzOi8vY2xvdWQteHNwbS1yaXNrLWZpeC1hZHZpY2UtMTI1ODM0NDY5OS5jb3MuYXAtZ3Vhbmd6aG91LnRlbmNlbnRjb3MuY24vaW1hZ2VzL3hzcG1fcHJlL2NydWlzZXJfYWZmYzFiNDIyMWI4MzczN2E2NmQ5Yzc0ZWY2MzM5OGQuanBlZyJdfV1d",
        "RiskInfluence": "主机存在安全漏洞，可能导致主机被入侵，建议您按应急漏洞、应用漏洞、Web-CMS、Windows软件漏洞、Linux软件漏洞的优先级顺序进行修复。该顺序并不决定，也可能存在非常严重的Windows软件漏洞需要立即处理的情况。您还可以打开腾讯云主机“仅展示高优修复漏洞”按钮，来处理高优修复漏洞。",
        "RiskName": "腾讯云 主机安全漏洞检测",
        "RiskRuleId": "tc_083"
    }
}
```

