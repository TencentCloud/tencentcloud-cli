**Example 1: 查看审批详情**



Input: 

```
tccli bpaas GetBpaasApproveDetail --cli-unfold-argument  \
    --ApproveId 1000000001
```

Output: 
```
{
    "Response": {
        "ApplyUin": 123456,
        "ApplyOwnUin": 123456,
        "ApplyUinNick": "",
        "BpaasId": 1000000001,
        "BpaasName": "qqqq",
        "ApplicationParams": [],
        "Reason": "1",
        "CreateTime": "2020-06-09 18:48:43",
        "Status": 1,
        "ApprovingNodeId": "",
        "Nodes": [
            {
                "NodeId": "1",
                "NodeName": "审批节点1",
                "NodeType": 1,
                "NextNode": "-1",
                "Opinion": [],
                "ScfName": "",
                "SubStatus": 8,
                "ApprovedUin": [],
                "CreateTime": "",
                "Msg": "success",
                "Users": [],
                "IsApprove": false,
                "ApproveId": 0,
                "ApproveType": 2,
                "ApproveMethod": -1
            }
        ],
        "RequestId": "fe080a39-3644-4070-94c5-460001281ec7"
    }
}
```

