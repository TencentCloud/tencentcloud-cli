**Example 1: 查询镜像拦截事件列表**



Input: 

```
tccli tcss DescribeImageDenyEventList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "ClusterID": "cls-m2x0ndjy",
                "ClusterName": "cls-m2x0ndjy",
                "DealBehavior": "BEHAVIOR_HOLDUP_SUCCESSED",
                "EventCount": 185,
                "EventID": 2414001,
                "EventType": "EVENT_RISK",
                "FoundTime": "2024-11-02 00:03:32",
                "ImageID": "sha256:d41059c812a8741c15695046857b90747aef9c7f9d67733962d7bbb025b9d159",
                "ImageName": "registry.tce.com/etcd/etcd:3.4.18.amd64",
                "LatestFoundTime": "2024-11-02 15:42:37",
                "NodeID": "5a540076-d38a-4078-aa98-e7c86371d322",
                "NodeIP": "10.206.67.153",
                "NodeName": "tcs-10-206-67-153",
                "NodeType": "NORMAL",
                "NodeUniqueID": "d41d8cd98f00b204e9800998ecf8427e",
                "PodIP": "127.0.0.1",
                "PodName": "name02",
                "PublicIP": "118.195.195.86",
                "QUUID": "46d3b4de-add7-4378-af19-ad34baeb6b4b",
                "RuleDescription": "测试",
                "RuleEffectStatus": "IN_EFFECT",
                "RuleID": "ce25d78c-d247-4e2f-80ee-190e089ea434",
                "RuleInfo": [
                    "IMAGE_DENY_VUL_CLASS"
                ],
                "RuleName": "name03",
                "RuleStatus": 1,
                "RuleType": "RULE_RISK",
                "ImageRegistryInfo": {
                    "Name": "name01",
                    "Type": "tcr",
                    "Address": "ccr.ccs.tencentyun.com/t-pot/logstash"
                }
            }
        ],
        "TotalCount": 0,
        "RequestId": "a11d268f-1601-4f63-9131-0382537b9e55"
    }
}
```

