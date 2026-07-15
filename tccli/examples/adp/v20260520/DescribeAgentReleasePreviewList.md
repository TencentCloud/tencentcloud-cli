**Example 1: 获取应用下 Agent 的发布预览列表**



Input: 

```
tccli adp DescribeAgentReleasePreviewList --cli-unfold-argument  \
    --AppId 204*************016 \
    --PageNumber 20 \
    --PageSize 0
```

Output: 
```
{
    "Response": {
        "ReleaseList": [
            {
                "Action": 1,
                "ActionDescription": "新增",
                "AgentId": "e25e9a2b-96c4-4cad-979b-f6f869e7cfb9",
                "Message": "待发布变更 5 项",
                "Name": "huiru_test",
                "UpdateTime": "1776838008"
            }
        ],
        "TotalCount": 1,
        "RequestId": "9a346cb2-1583-4afc-8d13-df5845245523"
    }
}
```

