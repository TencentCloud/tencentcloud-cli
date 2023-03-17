**Example 1: 解绑用户独享进群**

前置条件：测试用户251005944在测试低于ap-guangzhou-2绑定了测试独享集群cluster-22120192，现在需要解绑该集群，需要调用接口UnbindUserDedicatedCluster接口实现。

Input: 

```
tccli cbs UnbindUserDedicatedCluster --cli-unfold-argument  \
    --UserAppId 251005944 \
    --Zone ap-guangzhou-2 \
    --DedicatedClusterId cluster-22120192
```

Output: 
```
{
    "Response": {
        "RequestId": "129uhhdsgh983-sdff-sdfsadfg-qsdfasdfsad"
    }
}
```

