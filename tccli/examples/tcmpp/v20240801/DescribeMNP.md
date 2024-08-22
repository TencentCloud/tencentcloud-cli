**Example 1: DescribeMNP**



Input: 

```
tccli tcmpp DescribeMNP --cli-unfold-argument  \
    --MNPId mpjl3td541qppx9k \
    --PlatformId T04257DS9431720WTAG
```

Output: 
```
{
    "Response": {
        "Data": {
            "AccessStatus": 2,
            "CreateTime": "1721010947",
            "CreateUser": "autotest_op",
            "MNPDesc": "test",
            "MNPIcon": "https://api.tcmpp-staging.tmfcloud.com:80/Mutable/T04257DS9431720WTAG/console/20240719101648-d75111ba9d.png?algo=sha1&exp=2036678400&sid=s-7da2a17b05&t=VI5x2Va%2B32TmbJFh63UoUkIhCgU%3D",
            "MNPId": "mpjl3td541qppx9k",
            "MNPIntro": "test",
            "MNPName": "autotest_online_miniapp",
            "MNPType": "Life Service->144_Lilliputian Services",
            "Status": 1,
            "TeamId": "1363731006",
            "TeamName": "autotest_mini_team"
        },
        "RequestId": "b25464f8-da2b-49e7-b3d4-1dcbc2e9c065"
    }
}
```

