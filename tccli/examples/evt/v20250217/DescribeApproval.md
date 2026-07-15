**Example 1: 示例**



Input: 

```
tccli evt DescribeApproval --cli-unfold-argument  \
    --ApprovalId A202601281769603240523
```

Output: 
```
{
    "Response": {
        "Config": "{\"key\":\"v\"}",
        "CreateName": "test-role-tag",
        "CreateRoleId": "4611686018432090389",
        "CreateTime": "2026-01-28 20:27:21",
        "Creator": 0,
        "Detail": "[{\"key\":\"接口名称\",\"value\":\"CreateSecurityGroupWithPolicies\"},{\"key\":\"接口描述\",\"value\":\"本接口（CreateSecurityGroupWithPolicies）用于创建新的安全组（SecurityGroup），并且可以同时添加安全组规则（SecurityGroupPolicy）。\"},{\"key\":\"安全组名称\",\"value\":\"test8\"},{\"key\":\"安全组备注\",\"value\":\"公网放通云主机常用登录及web服务端口，内网全放通。\"},{\"key\":\"项目ID\",\"value\":\"0\"},{\"key\":\"出站规则\",\"value\":\"[{\\\"Action\\\":\\\"ACCEPT\\\"}]\"},{\"key\":\"入站规则\",\"value\":\"[{\\\"Action\\\":\\\"ACCEPT\\\",\\\"PolicyDescription\\\":\\\"放通Windows远程登录\\\",\\\"Port\\\":\\\"1234\\\",\\\"Protocol\\\":\\\"tcp\\\"},{\\\"Action\\\":\\\"ACCEPT\\\",\\\"PolicyDescription\\\":\\\"放通Linux SSH登录\\\",\\\"Port\\\":\\\"22\\\",\\\"Protocol\\\":\\\"tcp\\\"},{\\\"Action\\\":\\\"ACCEPT\\\",\\\"PolicyDescription\\\":\\\"放通Web服务端口\\\",\\\"Port\\\":\\\"80,443\\\",\\\"Protocol\\\":\\\"tcp\\\"},{\\\"Action\\\":\\\"ACCEPT\\\",\\\"PolicyDescription\\\":\\\"放通Ping服务\\\",\\\"Protocol\\\":\\\"icmp\\\"},{\\\"Action\\\":\\\"ACCEPT\\\",\\\"CidrBlock\\\":\\\"0.0.0.0/8\\\",\\\"PolicyDescription\\\":\\\"放通内网\\\"},{\\\"Action\\\":\\\"ACCEPT\\\",\\\"CidrBlock\\\":\\\"0.0.0.0/12\\\",\\\"PolicyDescription\\\":\\\"放通内网\\\"},{\\\"Action\\\":\\\"ACCEPT\\\",\\\"CidrBlock\\\":\\\"0.0.0.0/16\\\",\\\"PolicyDescription\\\":\\\"放通内网\\\"}]\"}]",
        "DetailUrl": "https://console.cloud.tencent.com/vpc/security-group?rid=1&rid=10",
        "NodeList": [
            {
                "ApprovalResult": [
                    {
                        "Opinion": "同意 【通过MOA快速审批】",
                        "Result": 1,
                        "Uin": 0,
                        "UserId": "118392",
                        "UserName": "tony"
                    }
                ],
                "IsDealer": 2,
                "Model": "2",
                "NodeId": "AN202601281769603240525",
                "Status": "Succeed"
            }
        ],
        "ReqParam": "",
        "Result": 1,
        "Status": "Succeed",
        "TicketId": "T202601284861465312639",
        "Title": "创建安全组及规则dadasd6",
        "RequestId": "27fea038-e367-4a54-85c6-ed0ba86bfa54",
        "BypassApplyUserName": "t******n"
    }
}
```

