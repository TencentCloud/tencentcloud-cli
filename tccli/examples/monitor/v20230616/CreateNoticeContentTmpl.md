**Example 1: 创建模板**

测试环境真实请求

Input: 

```
tccli monitor CreateNoticeContentTmpl --cli-unfold-argument  \
    --TmplName Eric-test-1117-2236 \
    --MonitorType MT_QCE \
    --TmplLanguage en \
    --TmplContents.QCloudYehe.0.MatchingStatus Trigger \
    --TmplContents.QCloudYehe.0.Template.Email.ContentTmpl RXJpY+a1i+ivleaooeadv3t7LlRlc3R9fQrov5nmmK/mjaLooYzlkI7nmoTlhoXlrrl7ey5UZXN0fX0= \
    --TmplContents.QCloudYehe.0.Template.Email.TitleTmpl RXJpY+a1i+ivleagh+mimOaooeadv3t7LlRlc3R9fQ== \
    --TmplContents.QCloudYehe.0.Template.QYWX.ContentTmpl RXJpY+a1i+ivleaooeadv3t7LlRlc3R9fQrov5nmmK/mjaLooYzlkI7nmoTlhoXlrrl7ey5UZXN0fX0= \
    --TmplContents.QCloudYehe.0.Template.QYWX.TitleTmpl RXJpY+a1i+ivleagh+mimOaooeadv3t7LlRlc3R9fQ== \
    --TmplContents.QCloudYehe.0.Template.SMS.ContentTmpl RXJpY+a1i+ivleaooeadv3t7LlRlc3R9fQrov5nmmK/mjaLooYzlkI7nmoTlhoXlrrl7ey5UZXN0fX0= \
    --TmplContents.QCloudYehe.0.Template.SMS.TitleTmpl RXJpY+a1i+ivleagh+mimOaooeadv3t7LlRlc3R9fQ== \
    --TmplContents.QCloudYehe.0.Template.Voice.ContentTmpl RXJpY+a1i+ivleaooeadv3t7LlRlc3R9fQrov5nmmK/mjaLooYzlkI7nmoTlhoXlrrl7ey5UZXN0fX0= \
    --TmplContents.QCloudYehe.0.Template.Voice.TitleTmpl RXJpY+a1i+ivleagh+mimOaooeadv3t7LlRlc3R9fQ== \
    --TmplContents.QCloudYehe.0.Template.Site.ContentTmpl RXJpY+a1i+ivleaooeadv3t7LlRlc3R9fQrov5nmmK/mjaLooYzlkI7nmoTlhoXlrrl7ey5UZXN0fX0= \
    --TmplContents.QCloudYehe.0.Template.Site.TitleTmpl RXJpY+a1i+ivleagh+mimOaooeadv3t7LlRlc3R9fQ== \
    --TmplContents.QCloudYehe.0.Template.Andon.ContentTmpl RXJpY+a1i+ivleaooeadv3t7LlRlc3R9fQrov5nmmK/mjaLooYzlkI7nmoTlhoXlrrl7ey5UZXN0fX0= \
    --TmplContents.QCloudYehe.0.Template.Andon.TitleTmpl RXJpY+a1i+ivleagh+mimOaooeadv3t7LlRlc3R9fQ== \
    --TmplContents.WeWorkRobot.0.MatchingStatus Trigger \
    --TmplContents.WeWorkRobot.0.Template.ContentTmpl RXJpY+a1i+ivleaooeadv3t7LlRlc3R9fQrov5nmmK/mjaLooYzlkI7nmoTlhoXlrrl7ey5UZXN0fX0= \
    --TmplContents.DingDingRobot.0.MatchingStatus Trigger \
    --TmplContents.DingDingRobot.0.Template.ContentTmpl RXJpY+a1i+ivleaooeadv3t7LlRlc3R9fQrov5nmmK/mjaLooYzlkI7nmoTlhoXlrrl7ey5UZXN0fX0= \
    --TmplContents.DingDingRobot.0.Template.TitleTmpl RXJpY+a1i+ivleagh+mimOaooeadv3t7LlRlc3R9fQ== \
    --TmplContents.FeiShuRobot.0.MatchingStatus Trigger \
    --TmplContents.FeiShuRobot.0.Template.ContentTmpl RXJpY+a1i+ivleaooeadv3t7LlRlc3R9fQrov5nmmK/mjaLooYzlkI7nmoTlhoXlrrl7ey5UZXN0fX0= \
    --TmplContents.FeiShuRobot.0.Template.TitleTmpl RXJpY+a1i+ivleagh+mimOaooeadv3t7LlRlc3R9fQ==
```

Output: 
```
{
    "Response": {
        "RequestId": "aae79e81-4824-4b97-9307-2c7ff8f73e2e",
        "TmplID": "ntpl-3r1spzjn"
    }
}
```

