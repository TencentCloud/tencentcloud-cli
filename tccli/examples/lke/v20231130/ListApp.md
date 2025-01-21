**Example 1: ListApp**

获取企业下应用列表

Input: 

```
tccli lke ListApp --cli-unfold-argument  \
    --AppType knowledge_qa
```

Output: 
```
{
    "Response": {
        "Total": "1",
        "List": [
            {
                "AppType": "knowledge_qa",
                "AppTypeDesc": "知识库问答",
                "AppBizId": "1801166480814637052",
                "Name": "我的应用",
                "Avatar": "https://qidian-qbot-xxxxxxx.cos.ap-guangzhou.myqcloud.com/public/174434244193038090240/1801166482343244637056/image/jNVJvoXsTsBzo2324324121HZdgd-1816016475183120384.png",
                "Desc": "描述",
                "AppStatus": 2,
                "AppStatusDesc": "运行中",
                "UpdateTime": "1731407395",
                "Operator": "操作人",
                "ModelName": "精调知识大模型标准版",
                "Pattern": "standard",
                "ThoughtModelAliasName": "意图识别模型高级版"
            }
        ],
        "RequestId": "143a9f30-a21c-4eb3-af82-ccacd4cdcbfd"
    }
}
```

