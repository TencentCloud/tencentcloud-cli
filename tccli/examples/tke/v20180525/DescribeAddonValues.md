**Example 1: 获取addon的参数**

获取一个addon的参数

Input: 

```
tccli tke DescribeAddonValues --cli-unfold-argument  \
    --ClusterId cls-kihzth22 \
    --AddonName nvidia-gpu
```

Output: 
```
{
    "Response": {
        "DefaultValues": "{\"config\":{\"disablehealthchecks\":\"\",\"waituvm\":false},\"exporter\":{\"tag\":\"v1.0.18\"},\"global\":{\"cluster\":{\"appid\":1255429800,\"clustertype\":\"MANAGED_CLUSTER\",\"id\":\"cls-kihzth22\",\"kubeminor\":\"30.0\",\"kubeversion\":\"1.30.0-tke.2\",\"longregion\":\"ap-guangzhou\",\"region\":\"gz\",\"subuin\":100040133055,\"type\":\"tke\",\"uin\":100002743387},\"image\":{\"host\":\"ccr.ccs.tencentyun.com\"}},\"plugin\":{\"tag\":\"v0.14.3\"},\"pluginInit\":{\"tag\":\"v1.0\"}}",
        "RequestId": "4fb715e9-8233-4f82-9730-afe743ea89a7",
        "Values": "{\"config\":{\"disablehealthchecks\":\"\",\"waituvm\":false},\"exporter\":{\"tag\":\"v1.0.18\"},\"global\":{\"cluster\":{\"appid\":1255429800,\"clustertype\":\"MANAGED_CLUSTER\",\"id\":\"cls-kihzth22\",\"kubeminor\":\"30.0\",\"kubeversion\":\"1.30.0-tke.2\",\"longregion\":\"ap-guangzhou\",\"region\":\"gz\",\"subuin\":100040133055,\"type\":\"tke\",\"uin\":100002743387},\"image\":{\"host\":\"ccr.ccs.tencentyun.com\"}},\"plugin\":{\"tag\":\"v0.14.3\"},\"pluginInit\":{\"tag\":\"v1.0\"}}"
    }
}
```

