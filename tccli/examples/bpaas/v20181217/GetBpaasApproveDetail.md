**Example 1: 查看审批详情**

查看审批详情

Input: 

```
tccli bpaas GetBpaasApproveDetail --cli-unfold-argument  \
    --ApproveId 1000000001
```

Output: 
```
{
    "Response": {
        "ApplyUin": 1,
        "ApplyOwnUin": 1,
        "ApplyUinNick": "jack",
        "BpaasId": 1,
        "BpaasName": "申请mysql",
        "ApplicationParams": [
            {
                "Key": "name",
                "Value": [
                    "jack"
                ],
                "Name": "子用户"
            }
        ],
        "Reason": "业务需要",
        "CreateTime": "2024-11-27 19:26:57",
        "Status": 1,
        "Nodes": [
            {
                "NodeId": "1",
                "NodeName": "管理员审批",
                "NodeType": 1,
                "NextNode": "2",
                "Opinion": {
                    "Type": 1,
                    "Content": [
                        "abc"
                    ]
                },
                "ScfName": "get-names",
                "SubStatus": 1,
                "ApprovedUin": [
                    1
                ],
                "CreateTime": "2024-11-27 19:30:29",
                "Msg": "管理员审批",
                "Users": {
                    "Uin": 1,
                    "Type": 1,
                    "Desc": "普通用户",
                    "Nick": "jack",
                    "Scf": {
                        "ScfName": "get-approvers",
                        "ScfRegion": "ap-guangdong",
                        "ScfRegionName": "广东",
                        "Params": [
                            {
                                "Key": "total",
                                "Name": "总数",
                                "Type": 1,
                                "Values": [
                                    "1"
                                ]
                            }
                        ]
                    },
                    "ApproveStatus": 1,
                    "ApproveMsg": "同意",
                    "ApproveTime": "2024-11-27 19:30:29",
                    "ApproveGroup": "1"
                },
                "IsApprove": true,
                "ApproveId": "1",
                "ApproveMethod": 1,
                "ApproveType": 1,
                "CallMethod": 1,
                "DataHubId": "data94",
                "TaskName": "data",
                "CKafkaRegion": "ap-guangzhou",
                "ExternalUrl": "",
                "ParallelNodes": "3-2",
                "RejectedCloudFunctionMsg": "",
                "PrevNode": ""
            }
        ],
        "ApprovingNodeId": "2",
        "ModifyTime": "2024-11-27 19:30:29",
        "RequestId": "63a03810-f188-40ab-91ed-11fd81d6f9ce"
    }
}
```

