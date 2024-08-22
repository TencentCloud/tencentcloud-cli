**Example 1: DescribeMNPList**



Input: 

```
tccli tcmpp DescribeMNPList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 100 \
    --PlatformId T04257DS9431720WTAG \
    --Keyword  \
    --TeamId  \
    --ApplicationId 
```

Output: 
```
{
    "Response": {
        "Data": {
            "DataList": [
                {
                    "ApplicationName": "",
                    "CreateTime": "1722579133",
                    "CreateUser": "autotest_op",
                    "EffectMNPVersion": "",
                    "EffectMNPVersionId": 0,
                    "EffectStatus": 0,
                    "MNPIcon": "http://127.0.0.1/T04257DS9431720WTAG/tcmpp/20240802-b5f49f6f-56e9-4013-95ed-bc5e7311350e.png",
                    "MNPId": "mpyndm7bj0778psz",
                    "MNPIntro": "fdfgdsfg",
                    "MNPName": "fdfgdsfg",
                    "MNPType": "Medical Service->26_Public Medical Institutions",
                    "Status": 2,
                    "TeamName": "autotest_mini_team",
                    "UpdateTime": "1724123222",
                    "UpdateUser": "autotest_op"
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "bbd787b1-d083-403e-ba16-6a1285560f40"
    }
}
```

