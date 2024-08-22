**Example 1: AddTeamMember**



Input: 

```
tccli tcmpp AddTeamMember --cli-unfold-argument  \
    --TeamId 3686677859 \
    --MemberList.0.UserId U20240820175742EEOXFS \
    --MemberList.0.UserRoleId 20070 \
    --PlatformId T04257DS9431720WTAG
```

Output: 
```
{
    "Response": {
        "Data": {
            "Result": true
        },
        "RequestId": "11bfebaf-b179-402a-8c1e-e9ecb633c414"
    }
}
```

