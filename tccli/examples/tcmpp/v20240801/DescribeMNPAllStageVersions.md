**Example 1: DescribeMNPAllStageVersions**



Input: 

```
tccli tcmpp DescribeMNPAllStageVersions --cli-unfold-argument  \
    --MNPId mpg9yjc0qbpkelik \
    --PlatformId T04257DS9431720WTAG
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "MNPId": "mpg9yjc0qbpkelik",
                "MNPVersionId": 2596,
                "MNPName": "autotest_miniapp",
                "MNPIcon": "http://127.0.0.1/T04257DS9431720WTAG/console/20240820061043-30fc239971.png",
                "MNPType": "Logistics Services->1_Pickup/Delivery,Life Service->144_Lilliputian Services",
                "MNPIntro": "test",
                "MNPDesc": "test",
                "CreateUser": "autotest_op",
                "CreateTime": "1724142147",
                "MNPVersion": "1.0.277",
                "MNPVersionIntro": "test",
                "Phase": "Platform",
                "ApprovalNo": "aud7hnb70973ng51ca",
                "ApprovalStatus": 3,
                "VersionCurrentStatus": 3,
                "ShowCase": 1,
                "RollbackVersion": 0,
                "Status": 1
            },
            {
                "MNPId": "mpg9yjc0qbpkelik",
                "MNPVersionId": 2596,
                "MNPName": "autotest_miniapp",
                "MNPIcon": "http://127.0.0.1/T04257DS9431720WTAG/console/20240820061043-30fc239971.png",
                "MNPType": "Logistics Services->1_Pickup/Delivery,Life Service->144_Lilliputian Services",
                "MNPIntro": "test",
                "MNPDesc": "test",
                "CreateUser": "autotest_op",
                "CreateTime": "1724142147",
                "MNPVersion": "1.0.277",
                "MNPVersionIntro": "test",
                "Phase": "Online",
                "ApprovalNo": "aud7hnb70973ng51ca",
                "ApprovalStatus": 3,
                "VersionCurrentStatus": 3,
                "ShowCase": 1,
                "RollbackVersion": 0,
                "Status": 1
            },
            {
                "MNPId": "mpg9yjc0qbpkelik",
                "MNPVersionId": 2596,
                "MNPName": "autotest_miniapp",
                "MNPIcon": "http://127.0.0.1/T04257DS9431720WTAG/console/20240820061043-30fc239971.png",
                "MNPType": "Logistics Services->1_Pickup/Delivery,Life Service->144_Lilliputian Services",
                "MNPIntro": "test",
                "MNPDesc": "test",
                "CreateUser": "autotest_op",
                "CreateTime": "1724142147",
                "MNPVersion": "1.0.277",
                "MNPVersionIntro": "test",
                "Phase": "Develop",
                "ApprovalNo": "aud7hnb70973ng51ca",
                "ApprovalStatus": 3,
                "VersionCurrentStatus": 3,
                "ShowCase": 1,
                "RollbackVersion": 0,
                "Status": 1
            },
            {
                "MNPId": "mpg9yjc0qbpkelik",
                "MNPVersionId": 2395,
                "MNPName": "autotest_miniapp",
                "MNPIcon": "https://api.tcmpp-staging.tmfcloud.com:80/Mutable/T04257DS9431720WTAG/console/20240802101902-805af7c9bf.png",
                "MNPType": "Logistics Services->1_Pickup/Delivery,Life Service->144_Lilliputian Services",
                "MNPIntro": "用于自动化测试0820163007",
                "MNPDesc": "该小程序用于自动化测试0820163007",
                "CreateUser": "admin",
                "CreateTime": "1722571328",
                "MNPVersion": "1.0.115",
                "MNPVersionIntro": "add a new mnp version from console",
                "Phase": "Develop",
                "ApprovalNo": "",
                "ApprovalStatus": 3,
                "VersionCurrentStatus": 0,
                "ShowCase": 0,
                "RollbackVersion": 0,
                "Status": 1
            },
            {
                "MNPId": "mpg9yjc0qbpkelik",
                "MNPVersionId": 2582,
                "MNPName": "autotest_miniapp",
                "MNPIcon": "http://127.0.0.1/T04257DS9431720WTAG/console/20240820061043-30fc239971.png",
                "MNPType": "Logistics Services->1_Pickup/Delivery,Life Service->144_Lilliputian Services",
                "MNPIntro": "test",
                "MNPDesc": "test",
                "CreateUser": "800001208871",
                "CreateTime": "1724127655",
                "MNPVersion": "1.0.276",
                "MNPVersionIntro": "213123",
                "Phase": "Develop",
                "ApprovalNo": "audlyeenb7l9rfd51z",
                "ApprovalStatus": 3,
                "VersionCurrentStatus": 3,
                "ShowCase": 0,
                "RollbackVersion": 0,
                "Status": 1
            }
        ],
        "RequestId": "2802e966-d4ab-4a91-8350-00b803e5a49c"
    }
}
```

