**Example 1: 查询外部数据源模板列表**



Input: 

```
tccli lowcode DescribeTemplateList --cli-unfold-argument  \
    --PageIndex 1 \
    --PageSize 0 \
    --Code xx
```

Output: 
```
{
    "Response": {
        "Data": {
            "Count": 1,
            "Rows": [
                {
                    "Code": "meeting",
                    "Name": "腾讯会议",
                    "Icon": "https://wemeet-oauth-1258344699.cos.ap-guangzhou.myqcloud.com/default-app-icon/icon.png",
                    "Description": "腾讯会议（Tencent Meeting，TM）Rest API 是为参与腾讯会议生态系统建设的合作方开发者接入并访问腾讯会议资源提供的一组工具，是访问腾讯会议 SaaS 服务的入口。合作伙伴可以通过腾讯会议 API 进行二次开发，例如创建一个会议，修改会议，查询会议信息等。",
                    "Source": 2,
                    "AuthUrl": "https://meeting.tencent.com/authorize.html?corp_id=1400115281&sdk_id=16279852518&redirect_uri=http://console.cloud.tencent.com&state=eyJyYW5kb20iOiJpcXkyZm10eXk4Iiwic291cmNlIjoibWVldGluZyJ9"
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

