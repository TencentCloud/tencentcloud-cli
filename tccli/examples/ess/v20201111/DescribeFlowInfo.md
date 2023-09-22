**Example 1: 查询合同详情**

查询合同详情

Input: 

```
tccli ess DescribeFlowInfo --cli-unfold-argument  \
    --FlowIds yDwhIUUf*******tSuWZWJuzI0Zv
```

Output: 
```
{
    "Response": {
        "FlowDetailInfos": [
            {
                "CcInfos": [],
                "CreatedOn": 1695277267,
                "Creator": "yDRCLUUgygq2xun5UuO4zjEwg0vjoimj",
                "FlowApproverInfos": [
                    {
                        "ApproveMessage": "",
                        "ApproveName": "典子谦",
                        "ApproveStatus": 2,
                        "ApproveTime": 0,
                        "ApproveType": "PERSON",
                        "ApproverSource": "",
                        "CustomApproverTag": "",
                        "CustomUserId": "",
                        "Mobile": "13200000000",
                        "OrganizationId": "",
                        "OrganizationName": "",
                        "ReceiptId": "yDwJWUUckpkt3r17UxsD2OmvMWKhPCsC",
                        "SignId": "yDRS4UUgygqdcjjdUuO4zjEC0osCOsHS",
                        "SignOrder": 0
                    },
                    {
                        "ApproveMessage": "",
                        "ApproveName": "张三",
                        "ApproveStatus": 1,
                        "ApproveTime": 0,
                        "ApproveType": "ORGANIZATION",
                        "ApproverSource": "",
                        "CustomApproverTag": "",
                        "CustomUserId": "",
                        "Mobile": "18888888888",
                        "OrganizationId": "yDxbNUyKQDx3oAUuO4zjEBQGidlGe4hP",
                        "OrganizationName": "张三示例企业",
                        "ReceiptId": "yDwJWUUckpkt3r1bUxsD2Om8NdhsvAFk",
                        "SignId": "yDRS4UUgygqdcj51UuO4zjEyWTmzsIAR",
                        "SignOrder": 1
                    }
                ],
                "FlowDescription": "",
                "FlowId": "yDwhIUUf*******tSuWZWJuzI0Zv",
                "FlowMessage": "",
                "FlowName": "典子谦购买腾讯云机器的协议",
                "FlowStatus": 1,
                "FlowType": "劳动合同"
            }
        ],
        "FlowGroupId": "",
        "FlowGroupName": "",
        "RequestId": "fc6c2e4b-3f0b-402c-91a4-d74e9e96369e"
    }
}
```

**Example 2: 查询合同组详情**

查询合同组详情

Input: 

```
tccli ess DescribeFlowInfo --cli-unfold-argument  \
    --FlowGroupId yDwJWUUcss*******MjPKFm7bzFToAyk
```

Output: 
```
{
    "Response": {
        "FlowDetailInfos": [
            {
                "CcInfos": [],
                "CreatedOn": 1695279629,
                "Creator": "yDwfRUUw2vb22UESurE588OReErDv9jv",
                "FlowApproverInfos": [
                    {
                        "ApproveMessage": "",
                        "ApproveName": "张志英",
                        "ApproveStatus": 3,
                        "ApproveTime": 1695279840,
                        "ApproveType": "PERSON",
                        "ApproverSource": "",
                        "CustomApproverTag": "",
                        "CustomUserId": "",
                        "Mobile": "13200000000",
                        "OrganizationId": "",
                        "OrganizationName": "",
                        "ReceiptId": "yDwJWUUcss36hUx8VMjPR4jOb5ugrMSx",
                        "SignId": "yDwJWUUcss36rUx8VMjPwzdNESvociQv",
                        "SignOrder": 0
                    }
                ],
                "FlowDescription": "",
                "FlowId": "yDwJWUUcss*******MjPCmyDWhY5b6Ku",
                "FlowMessage": "",
                "FlowName": "个人征信查询申请表",
                "FlowStatus": 4,
                "FlowType": ""
            },
            {
                "CcInfos": [],
                "CreatedOn": 1695279629,
                "Creator": "yDwfRUUw2vb22UESurE588OReErDv9jv",
                "FlowApproverInfos": [
                    {
                        "ApproveMessage": "",
                        "ApproveName": "张志英",
                        "ApproveStatus": 3,
                        "ApproveTime": 1695279840,
                        "ApproveType": "PERSON",
                        "ApproverSource": "",
                        "CustomApproverTag": "",
                        "CustomUserId": "",
                        "Mobile": "13200000000",
                        "OrganizationId": "",
                        "OrganizationName": "",
                        "ReceiptId": "yDwJWUUcss36jUx8VMjPwPdsft773X11",
                        "SignId": "yDwJWUUcss362Ux8VMjPvn1TbsDyp85v",
                        "SignOrder": 0
                    }
                ],
                "FlowDescription": "",
                "FlowId": "yDwJWUUcss*******MjPEkLDPZBawumc",
                "FlowMessage": "",
                "FlowName": "个人征信查询授权书",
                "FlowStatus": 4,
                "FlowType": ""
            }
        ],
        "FlowGroupId": "",
        "FlowGroupName": "合同组JJ202309210000000017",
        "RequestId": "s1695280316032350176"
    }
}
```

**Example 3: 查询合同详情(如果合同ID不存在或者没有权限)**

如果FlowIds中某个合同ID不存在或者没有权限则会报错, 因为下面示例中的c7b5ca37ae*******2b4c6644不存在所以报错

Input: 

```
tccli ess DescribeFlowInfo --cli-unfold-argument  \
    --FlowIds c7b5ca37ae*******2b4c6644 yDRSRUUgygj******uO4zjESlnSFPcIE
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation",
            "Message": "无效的流程合同Id，检查后重试"
        },
        "RequestId": "s1692325082060040872"
    }
}
```

