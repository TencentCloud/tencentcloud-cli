**Example 1: 查看不满意回复上下文**

查看不满意回复上下文

Input: 

```
tccli lke DescribeUnsatisfiedReplyContext --cli-unfold-argument  \
    --BotBizId 1696822786072117248 \
    --ReplyBizId 29
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Avatar": "https://qidian-qbot-1251316161.cos.ap-guangzhou.myqcloud.com/public/avatar_penguin01.png",
                "Content": "你好",
                "IsVisitor": true,
                "NickName": "131****1632",
                "RecordBizId": "ea896164-fd4a-4020-9fd0-cc86faaa6f1d"
            },
            {
                "Avatar": "https://qbot-1251316161.cos.ap-nanjing.myqcloud.com/avatar.png",
                "Content": "您好！有什么我可以帮助您的吗？",
                "IsVisitor": false,
                "NickName": "企点智能客服02",
                "RecordBizId": "3f913f9e-8efb-473a-aea4-2e97268360f9"
            },
            {
                "Avatar": "https://qidian-qbot-1251316161.cos.ap-guangzhou.myqcloud.com/public/avatar_penguin01.png",
                "Content": "你好",
                "IsVisitor": true,
                "NickName": "131****1632",
                "RecordBizId": "48cb5e24-88e6-46f0-8d2d-75f517686de4"
            },
            {
                "Avatar": "https://qbot-1251316161.cos.ap-nanjing.myqcloud.com/avatar.png",
                "Content": "您好！有什么我可以帮助您的吗？",
                "IsVisitor": false,
                "NickName": "企点智能客服02",
                "RecordBizId": "2f007448-7af6-420c-a14c-2de23f28f8d2"
            },
            {
                "Avatar": "https://qidian-qbot-1251316161.cos.ap-guangzhou.myqcloud.com/public/avatar_penguin01.png",
                "Content": "你好",
                "IsVisitor": true,
                "NickName": "131****1632",
                "RecordBizId": "354bac2d-2b27-4dbd-b6bb-c53de9808a4d"
            },
            {
                "Avatar": "https://qbot-1251316161.cos.ap-nanjing.myqcloud.com/avatar.png",
                "Content": "您好！有什么我可以帮助您的吗？",
                "IsVisitor": false,
                "NickName": "企点智能客服02",
                "RecordBizId": "594c875a-6332-4042-b4a6-3ffeaac6ccde"
            },
            {
                "Avatar": "https://qidian-qbot-1251316161.cos.ap-guangzhou.myqcloud.com/public/avatar_penguin01.png",
                "Content": "你好",
                "IsVisitor": true,
                "NickName": "131****1632",
                "RecordBizId": "aa86aee5-ee06-4cb1-91f3-33a967b7f437"
            },
            {
                "Avatar": "https://qbot-1251316161.cos.ap-nanjing.myqcloud.com/avatar.png",
                "Content": "您好！有什么我可以帮助您的吗？",
                "IsVisitor": false,
                "NickName": "企点智能客服02",
                "RecordBizId": "83095ab9-61b5-4392-980b-d76fdf4bcdd8"
            },
            {
                "Avatar": "https://qidian-qbot-1251316161.cos.ap-guangzhou.myqcloud.com/public/avatar_penguin01.png",
                "Content": "你好",
                "IsVisitor": true,
                "NickName": "131****1632",
                "RecordBizId": "4b152507-04da-44ae-9e39-b8f170a7c58d"
            },
            {
                "Avatar": "https://qbot-1251316161.cos.ap-nanjing.myqcloud.com/avatar.png",
                "Content": "您好！有什么我可以帮助您的吗？",
                "IsVisitor": false,
                "NickName": "企点智能客服02",
                "RecordBizId": "4158c9a9-724e-447d-9973-f35bfc6af38d"
            },
            {
                "Avatar": "https://qidian-qbot-1251316161.cos.ap-guangzhou.myqcloud.com/public/avatar_penguin01.png",
                "Content": "你好",
                "IsVisitor": true,
                "NickName": "131****1632",
                "RecordBizId": "265b25a2-95d0-4775-86e3-a9dd3278c747"
            },
            {
                "Avatar": "https://qbot-1251316161.cos.ap-nanjing.myqcloud.com/avatar.png",
                "Content": "您好！有什么我可以帮助您的吗？",
                "IsVisitor": false,
                "NickName": "企点智能客服02",
                "RecordBizId": "34366c2d-065c-498e-a9f7-c7e06ac82bc5"
            },
            {
                "Avatar": "https://qidian-qbot-1251316161.cos.ap-guangzhou.myqcloud.com/public/avatar_penguin01.png",
                "Content": "你好",
                "IsVisitor": true,
                "NickName": "131****1632",
                "RecordBizId": "996d7eff-8345-4858-a290-fe0b8b2b5c87"
            },
            {
                "Avatar": "https://qbot-1251316161.cos.ap-nanjing.myqcloud.com/avatar.png",
                "Content": "您好！有什么我可以帮助您的吗？",
                "IsVisitor": false,
                "NickName": "企点智能客服02",
                "RecordBizId": "04171ac2-46b0-4371-9983-176ecda6ffc0"
            }
        ],
        "RequestId": "72e31a2d-59cf-42f6-9fc2-c6b3676971cd"
    }
}
```

