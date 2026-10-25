**Example 1: DescribeSessionList**



Input: 

```
tccli rum DescribeSessionList --cli-unfold-argument  \
    --AppId 146662 \
    --StartTime 1776403015595 \
    --EndTime 1776417415595 \
    --SessionType all \
    --Page 1 \
    --PageSize 20 \
    --AppVersions 1.0.0
```

Output: 
```
{
    "Response": {
        "Result": "{\"Page\":1,\"PageSize\":20,\"Sessions\":[{\"SessionId\":\"c5116f619aba47d2b224a861297a06a9\",\"UserId\":\"700001860566\",\"StartTime\":1776415224792,\"EndTime\":1776417510956,\"Duration\":2286164,\"EventCount\":319,\"ErrorCount\":86,\"HasError\":true,\"PageCount\":34,\"FirstPageUrl\":\"https://console.cloud.tencent.com/monitor/rum/dem-config\",\"DeviceType\":\"desktop\",\"Platform\":\"web\",\"AppVersion\":\"1.0.0\",\"Os\":\"macOS\",\"Browser\":\"Chrome\",\"Country\":\"中国\",\"Region\":\"广东\",\"StruggleScore\":1.0099667774086378,\"StruggleRank\":\"Good\",\"StruggleCount\":18,\"Lcp\":7899,\"Inp\":77.33333333333333,\"Cls\":0.5419550882850751,\"LatestReplayId\":\"rep_40a4ed58d205567aeec2df89dba832d4\"},{\"SessionId\":\"d6db9fe86ef34d6aaf399673626947b5\",\"UserId\":\"700001860566\",\"StartTime\":1776414983628,\"EndTime\":1776415187481,\"Duration\":203853,\"EventCount\":58,\"ErrorCount\":12,\"HasError\":true,\"PageCount\":8,\"FirstPageUrl\":\"https://console.cloud.tencent.com/monitor/rum\",\"DeviceType\":\"desktop\",\"Platform\":\"web\",\"AppVersion\":\"1.0.0\",\"Os\":\"macOS\",\"Browser\":\"Chrome\",\"Country\":\"中国\",\"Region\":\"广东\",\"StruggleScore\":1.3333333333333333,\"StruggleRank\":\"Good\",\"StruggleCount\":4,\"Lcp\":4464,\"Inp\":248,\"Cls\":0.08204904981830531,\"LatestReplayId\":\"rep_92d583b03c8c0e6d0c9dedf2cabfe551\"},{\"SessionId\":\"f1f1a7c657ce4435b64652a8cf4f7589\",\"UserId\":\"700001860566\",\"StartTime\":1776414526253,\"EndTime\":1776415153800,\"Duration\":627547,\"EventCount\":45,\"ErrorCount\":10,\"HasError\":true,\"PageCount\":12,\"FirstPageUrl\":\"https://console.cloud.tencent.com/monitor/rum/session\",\"DeviceType\":\"desktop\",\"Platform\":\"web\",\"AppVersion\":\"1.0.0\",\"Os\":\"Mac OS X\",\"Browser\":\"Electron\",\"Country\":\"中国\",\"Region\":\"广东\",\"StruggleScore\":2.3,\"StruggleRank\":\"Fair\",\"StruggleCount\":5,\"Lcp\":9269.5,\"Inp\":112,\"Cls\":0.18938273533709518,\"LatestReplayId\":\"rep_d60d0e616614f42122f8b95ed04b4d7b\"},{\"SessionId\":\"3bb07f568f3c4e56bfb857a16faaa072\",\"UserId\":\"700001860566\",\"StartTime\":1776413382865,\"EndTime\":1776414511785,\"Duration\":1128920,\"EventCount\":70,\"ErrorCount\":21,\"HasError\":true,\"PageCount\":12,\"FirstPageUrl\":\"https://console.cloud.tencent.com/monitor/rum\",\"DeviceType\":\"desktop\",\"Platform\":\"web\",\"AppVersion\":\"1.0.0\",\"Os\":\"Mac OS X\",\"Browser\":\"Electron\",\"Country\":\"中国\",\"Region\":\"广东\",\"StruggleScore\":1.9682539682539681,\"StruggleRank\":\"Fair\",\"StruggleCount\":7,\"Lcp\":8452.649999976158,\"Inp\":8,\"Cls\":0.40992709039594166,\"LatestReplayId\":\"rep_baacc4b1ac519ae6bc922270462fa9a8\"}],\"Total\":4}",
        "RequestId": "3e5887b4-cf01-4958-a8d7-42146dc4690b"
    }
}
```

