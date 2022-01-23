**Example 1: 列出用户关联的策略（包括随组关联）**



Input: 

```
tccli cam ListAttachedUserAllPolicies --cli-unfold-argument  \
    --Rp 1 \
    --Page 10 \
    --AttachType 1 \
    --TargetUin 1234565
```

Output: 
```
{
    "Response": {
        "TotalNum": 11,
        "PolicyList": [
            {
                "PolicyId": "522474",
                "PolicyName": "policygen-20191204195412",
                "Description": "",
                "AddTime": "2019-12-04 19:56:35",
                "StrategyType": "1",
                "CreateMode": "3",
                "Deactived": 1,
                "Groups": [],
                "DeactivedDetail": [
                    "xx"
                ]
            }
        ],
        "RequestId": "d369dabb-ebc9-4598-baae-e1177e9e3868"
    }
}
```

