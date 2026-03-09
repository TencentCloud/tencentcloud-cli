**Example 1: 修改模板**

测试环境真实请求

Input: 

```
tccli monitor ModifyNoticeContentTmpl --cli-unfold-argument  \
    --TmplName Eric-test-1117-2318-修改 \
    --TmplContents.QCloudYehe.0.MatchingStatus Trigger \
    --TmplContents.QCloudYehe.0.Template.Email.ContentTmpl RXJpY+a1i+ivleaooeadv3t7LlRlc3R9fQrov5nmmK/mjaLooYzlkI7nmoTlhoXlrrl7ey5UZXN0fX0KCuaNouihjOWQjuWPiOS/ruaUueS6hnt7LlRlc3R9fQ== \
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
    --TmplContents.WeWorkRobot.0.Template.ContentTmpl RXJpY+a1i+ivleaooeadv3t7LlRlc3R9fQrov5nmmK/mjaLooYzlkI7nmoTlhoXlrrl7ey5UZXN0fX0KCuaNouihjOWQjuWPiOS/ruaUueS6hnt7LlRlc3R9fQ== \
    --TmplContents.DingDingRobot.0.MatchingStatus Trigger \
    --TmplContents.DingDingRobot.0.Template.ContentTmpl RXJpY+a1i+ivleaooeadv3t7LlRlc3R9fQrov5nmmK/mjaLooYzlkI7nmoTlhoXlrrl7ey5UZXN0fX0= \
    --TmplContents.DingDingRobot.0.Template.TitleTmpl RXJpY+a1i+ivleagh+mimOaooeadv3t7LlRlc3R9fQ== \
    --TmplContents.FeiShuRobot.0.MatchingStatus Trigger \
    --TmplContents.FeiShuRobot.0.Template.ContentTmpl RXJpY+a1i+ivleaooeadv3t7LlRlc3R9fQrov5nmmK/mjaLooYzlkI7nmoTlhoXlrrl7ey5UZXN0fX0= \
    --TmplContents.FeiShuRobot.0.Template.TitleTmpl RXJpY+a1i+ivleagh+mimOaooeadv3t7LlRlc3R9fQ== \
    --TmplID ntpl-k3auv6kz
```

Output: 
```
{
    "Response": {
        "RequestId": "90049244-2b8c-4f38-bff0-aca06367ab51"
    }
}
```

