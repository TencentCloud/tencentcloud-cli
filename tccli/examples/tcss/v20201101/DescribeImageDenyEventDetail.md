**Example 1: 查询镜像拦截事件详情**

查询镜像拦截事件详情

Input: 

```
tccli tcss DescribeImageDenyEventDetail --cli-unfold-argument  \
    --EventID 10
```

Output: 
```
{
    "Response": {
        "ClusterID": "cls-4waue9dh",
        "ClusterName": "prom-g62znlhv",
        "DealBehavior": "BEHAVIOR_HOLDUP_SUCCESSED",
        "Description": "该镜像命中拦截规则（id:ce25d78c-d247-4e2f-80ee-190e089ea434）触发拦截操作, 规则详情：该镜像存在存在漏洞: 按漏洞分类",
        "EventCount": 185,
        "EventID": 2414001,
        "EventType": "EVENT_RISK",
        "FoundTime": "2024-11-02 00:03:32",
        "ImageID": "sha256:d41059c812a8741c15695046857b90747aef9c7f9d67733962d7bbb025b9d159",
        "ImageName": "registry.tce.com/etcd/etcd:3.4.18.amd64",
        "LatestFoundTime": "2024-11-02 15:42:37",
        "NodeID": "eklet-subnet-1ewk3avk",
        "NodeIP": "10.206.1.2",
        "NodeName": "tcs-10-206-67-153",
        "NodeSubNetCIDR": "172.16.64.0/20",
        "NodeSubNetID": "subnet-1ewk3avk",
        "NodeSubNetName": "subnet-1ewk3avk",
        "NodeType": "NORMAL",
        "NodeUniqueID": "eb7b9af448345924bab44fc90a1b4e3b",
        "PodIP": "127.0.0.1",
        "PodName": "pod1",
        "PodStatus": "RUNNING",
        "PublicIP": "127.0.0.1",
        "QUUID": "46d3b4de-add7-4378-af19-ad34baeb6b4b",
        "RequestId": "b610c113-b940-4c0c-b937-b8edf518ef92",
        "RuleDescription": "测试",
        "RuleEffectStatus": "IN_EFFECT",
        "RuleEffectTime": "2024-10-30 10:52:56",
        "RuleID": "ce25d78c-d247-4e2f-80ee-190e089ea434",
        "RuleInfo": [
            "IMAGE_DENY_VUL_CLASS"
        ],
        "RuleName": "name01",
        "RuleStatus": 1,
        "RuleType": "RULE_RISK",
        "Solution": "CVE漏洞：将存在漏洞的组件更新到对应修复版本",
        "StartParam": "/opt/containerd/bin/runc runc --root /var/run/docker/runtime-runc/moby --log /run/docker/containerd/daemon/io.containerd.runtime.v1.linux/moby/9deace634eeb3fc28f7ac7bdbdeae6e917c89d1fc668892b25af20555fbd2832/log.json --log-format json create --bundle /var/run/docker/containerd/daemon/io.containerd.runtime.v1.linux/moby/9deace634eeb3fc28f7ac7bdbdeae6e917c89d1fc668892b25af20555fbd2832 --pid-file /var/run/docker/containerd/daemon/io.containerd.runtime.v1.linux/moby/9deace634eeb3fc28f7ac7bdbdeae6e917c89d1fc668892b25af20555fbd2832/init.pid 9deace634eeb3fc28f7ac7bdbdeae6e917c89d1fc668892b25af20555fbd2832",
        "ImageRegistryInfo": {
            "Name": "registry01",
            "Type": "tcr",
            "Address": "ccr.ccs.tencentyun.com/t-pot/logstash"
        }
    }
}
```

