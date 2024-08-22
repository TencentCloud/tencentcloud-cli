**Example 1: DescribeUserList**



Input: 

```
tccli tcmpp DescribeUserList --cli-unfold-argument  \
    --Keyword  \
    --Limit 10 \
    --Offset 0 \
    --AccountType 0 \
    --TeamId 0 \
    --PlatformId T04257DS9431720WTAG
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 10,
            "DataList": [
                {
                    "UserId": "U20240819174742HGXHXT",
                    "UserAccount": "OpenApiUser0819174740",
                    "UserName": "OpenApiUser0819174740",
                    "TeamName": "",
                    "Status": 1,
                    "AccountType": 3,
                    "CreateTime": "1724060862"
                },
                {
                    "UserId": "U20240819170247WSBYNR",
                    "UserAccount": "OpenApiUser0819170245",
                    "UserName": "12313",
                    "TeamName": "",
                    "Status": 1,
                    "AccountType": 3,
                    "CreateTime": "1724058167"
                },
                {
                    "UserId": "U20240819140751NLQQBP",
                    "UserAccount": "eric1",
                    "UserName": "eric1",
                    "TeamName": "eric_mini_team,eric_app_team",
                    "Status": 1,
                    "AccountType": 3,
                    "CreateTime": "1724047671"
                },
                {
                    "UserId": "U20240819115645WTLQND",
                    "UserAccount": "vinya",
                    "UserName": "vinya",
                    "TeamName": "vinya_mini,vinya_app",
                    "Status": 1,
                    "AccountType": 3,
                    "CreateTime": "1724039805"
                },
                {
                    "UserId": "U20240819113830AMQYEH",
                    "UserAccount": "eric_test",
                    "UserName": "eric_test",
                    "TeamName": "",
                    "Status": 1,
                    "AccountType": 2,
                    "CreateTime": "1724038710"
                },
                {
                    "UserId": "U20240819113604EESVUF",
                    "UserAccount": "vinya_plat",
                    "UserName": "vinya_plat",
                    "TeamName": "",
                    "Status": 1,
                    "AccountType": 2,
                    "CreateTime": "1724038564"
                },
                {
                    "UserId": "U20240814102554KKJOOF",
                    "UserAccount": "ela_platform",
                    "UserName": "ela_platform",
                    "TeamName": "",
                    "Status": 1,
                    "AccountType": 2,
                    "CreateTime": "1723602354"
                },
                {
                    "UserId": "U20240801192820CVRUBH",
                    "UserAccount": "jadentest009",
                    "UserName": "jadentest009",
                    "TeamName": "test",
                    "Status": 1,
                    "AccountType": 4,
                    "CreateTime": "1722511700"
                },
                {
                    "UserId": "U20240801145857JOWJCJ",
                    "UserAccount": "jaden",
                    "UserName": "jaden",
                    "TeamName": "",
                    "Status": 1,
                    "AccountType": 2,
                    "CreateTime": "1722495537"
                },
                {
                    "UserId": "U20240729223443LLXRFS",
                    "UserAccount": "vinya_test006",
                    "UserName": "vinya_test006",
                    "TeamName": "autotest_app_team",
                    "Status": 1,
                    "AccountType": 3,
                    "CreateTime": "1722263683"
                }
            ]
        },
        "RequestId": "ef3d028d-d74f-4764-a980-f71b867dcd89"
    }
}
```

