**Example 1: 查询全部接收机器人**



Input: 

```
tccli csip DescribeWebhookReceiverList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "ID": 1001,
                "Name": "开发组-飞书",
                "Type": "WEBHOOK",
                "WebhookAddr": "https://open.feishu.cn/open-apis/bot/v2/hook/abc",
                "SCFRegion": "",
                "Namespace": "",
                "FunctionName": "",
                "FunctionVersion": "",
                "Alias": ""
            }
        ],
        "TotalCount": 1,
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    }
}
```

