**Example 1: 查询渠道列表**

查询渠道列表

Input: 

```
tccli adp DescribeChannelList --cli-unfold-argument  \
    --AppId 20***2*********7712 \
    --Scene 1
```

Output: 
```
{
    "Response": {
        "ChannelList": [
            {
                "ChannelId": "20**************392",
                "ConnectStatus": 2,
                "CreateTime": "1784285002",
                "Spec": {
                    "ChannelName": "a*************_2",
                    "ChannelType": 10014,
                    "Description": "**************_desc",
                    "Scene": 1,
                    "UserAgent": {
                        "AgentId": "use*********d*******d01-bc10-cf999d37648*",
                        "UserId": "al******u"
                    },
                    "WecomRobot": {
                        "Websocket": {
                            "BindType": 0,
                            "BotId": "a****F*********N******1ldolKHwOOYCW",
                            "BotSecret": ""
                        }
                    }
                },
                "UpdateTime": "1784285002",
                "Updater": ""
            }
        ],
        "TotalCount": 2,
        "RequestId": "bc4a1046-fbac-49ce-9812-6e15701b200f"
    }
}
```

