**Example 1: DescribeTeamMemberList**

demo

Input: 

```
tccli tcmpp DescribeTeamMemberList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 30 \
    --TeamId 3686677859 \
    --Keyword  \
    --PlatformId T04257DS9431720WTAG
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 9,
            "DataList": [
                {
                    "UserId": "U20240820175742EEOXFS",
                    "UserAccount": "OpenApiUser0820175741",
                    "UserName": "OpenApiUser0820175741",
                    "TeamId": "3686677859",
                    "TeamName": "autotest_app_team",
                    "TeamRoleName": "Application Senior Developer",
                    "TeamRoleId": 20070,
                    "CanEdit": true
                },
                {
                    "UserId": "U20240729223443LLXRFS",
                    "UserAccount": "vinya_test006",
                    "UserName": "vinya_test006",
                    "TeamId": "3686677859",
                    "TeamName": "autotest_app_team",
                    "TeamRoleName": "Application Developer",
                    "TeamRoleId": 20071,
                    "CanEdit": true
                },
                {
                    "UserId": "U20240729215649PUGAPJ",
                    "UserAccount": "autouser",
                    "UserName": "autouser",
                    "TeamId": "3686677859",
                    "TeamName": "autotest_app_team",
                    "TeamRoleName": "Application Member Manager",
                    "TeamRoleId": 20069,
                    "CanEdit": true
                },
                {
                    "UserId": "U20240729194217ADBCHQ",
                    "UserAccount": "vinya_test005",
                    "UserName": "vinya_test005",
                    "TeamId": "3686677859",
                    "TeamName": "autotest_app_team",
                    "TeamRoleName": "Application Senior Developer",
                    "TeamRoleId": 20070,
                    "CanEdit": true
                },
                {
                    "UserId": "U20240729150318FTLAOG",
                    "UserAccount": "vinya_test003",
                    "UserName": "vinya_test003",
                    "TeamId": "3686677859",
                    "TeamName": "autotest_app_team",
                    "TeamRoleName": "Application Senior Developer",
                    "TeamRoleId": 20070,
                    "CanEdit": true
                },
                {
                    "UserId": "U20240728132000GOTVUF",
                    "UserAccount": "debug_test002",
                    "UserName": "debug_test002",
                    "TeamId": "3686677859",
                    "TeamName": "autotest_app_team",
                    "TeamRoleName": "Application Operator",
                    "TeamRoleId": 20072,
                    "CanEdit": true
                },
                {
                    "UserId": "U20240728131439UWAUHU",
                    "UserAccount": "debug_test001",
                    "UserName": "debug_test001",
                    "TeamId": "3686677859",
                    "TeamName": "autotest_app_team",
                    "TeamRoleName": "Application Developer",
                    "TeamRoleId": 20071,
                    "CanEdit": true
                },
                {
                    "UserId": "U20240718143421SRCPKQ",
                    "UserAccount": "test008",
                    "UserName": "test008",
                    "TeamId": "3686677859",
                    "TeamName": "autotest_app_team",
                    "TeamRoleName": "Application Senior Developer",
                    "TeamRoleId": 20070,
                    "CanEdit": true
                },
                {
                    "UserId": "U20240711141611BBFYIF",
                    "UserAccount": "autotest_op",
                    "UserName": "autotest_op",
                    "TeamId": "3686677859",
                    "TeamName": "autotest_app_team",
                    "TeamRoleName": "Application Administrator",
                    "TeamRoleId": 20068,
                    "CanEdit": false
                }
            ]
        },
        "RequestId": "c0939315-ce63-4a1a-b0a9-5404d7649666"
    }
}
```

