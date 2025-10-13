**Example 1: 更新cbs组件参数**

用户可以通过RawValues参数更新cbs组件支持的自定义配置参数，比如修改容忍调度设置，可以将 {"tolerations":[{"effect":"NoExecute","key":"gpu-not-ready","operator":"Equal","tolerationSeconds":300,"value":"true"},{"key":"ip-not-ready","operator":"Exists"}]}  进行base64编码后放入到 RawValues 参数中。cbs组件支持的自定义配置参数说明如下：
```
{
  "tolerations": [
    {
      "effect": "string，效果，例如：NoExecute",
      "key": "string，标签值，例如：gpu-not-ready",
      "operator": "string，操作符，例如：Equal",
      "tolerationSeconds": "int，容忍时间（秒），例如：300",
      "value": "string，标签值，例如：true"
    },
    {
      "key": "string，标签值，例如：ip-not-ready",
      "operator": "string，操作符，例如：Exists"
    }
  ]
}
```

Input: 

```
tccli tke UpdateAddon --cli-unfold-argument  \
    --ClusterId cls-qbc3zefo \
    --AddonName cbs \
    --RawValues eyJ0b2xlcmF0aW9ucyI6W3siZWZmZWN0IjoiTm9FeGVjdXRlIiwia2V5IjoiZ3B1LW5vdC1yZWFkeSIsIm9wZXJhdG9yIjoiRXF1YWwiLCJ0b2xlcmF0aW9uU2Vjb25kcyI6MzAwLCJ2YWx1ZSI6InRydWUifSx7ImtleSI6ImlwLW5vdC1yZWFkeSIsIm9wZXJhdG9yIjoiRXhpc3RzIn1dfQ== \
    --UpdateStrategy merge
```

Output: 
```
{
    "Response": {
        "RequestId": "f55aaa93-c681-47c9-860a-59ae16af648"
    }
}
```

**Example 2: 更新eniipamd组件参数**

用户可以通过RawValues参数更新eniipamd组件支持的自定义配置参数，比如清空已配置的安全组，可以将 {"vpcCni":{"securityGroups":{"securityGroups":[]}}} 进行base64编码后放入到 RawValues 参数中。eniipamd组件支持的自定义配置参数说明如下：
```
{
  "clusterId": "string, 集群ID, 例如：cls-qbc3zefo",
  "vpcCni": {
    "vpcId": "string, VPC的ID, 例如：vpc-qbc3zefo",
    "enableVpcCni": "bool, 是否启用VPC CNI, 例如：true",
    "routeEni": {
      "ipMinWarmTarget": "int, 新增节点共享网卡辅助IP的最小预绑定值, 例如：5",
      "ipMaxWarmTarget": "int, 新增节点共享网卡辅助IP的最大预绑定值, 例如：5"
    },
    "ipam": {
      "subnetIds": "array, 用于IP地址分配的Pod子网ID列表, 例如：[\"subnet-qbc3zefo\"]"
    }, 
  	"securityGroups": {
      "enableSecurityGroups": "bool, 是否启用安全组, 例如：true",
      "securityGroups": [
        "string, 安全组ID, 例如：sg-qbc3zefo"
      ]
    }
  },
  "agent": {
    "kubeClient": {
      "masterAddr": "string, kubeClient主节点地址, 例如: 169.254.128.54:60002"
    }
  }
}
```

Input: 

```
tccli tke UpdateAddon --cli-unfold-argument  \
    --ClusterId cls-qbc3zefo \
    --AddonName eniipamd \
    --RawValues eyJ2cGNDbmkiOnsic2VjdXJpdHlHcm91cHMiOnsic2VjdXJpdHlHcm91cHMiOltdfX19 \
    --UpdateStrategy merge
```

Output: 
```
{
    "Response": {
        "RequestId": "f55aaa93-c681-47c9-860a-59ae16ade268"
    }
}
```

**Example 3: 更新tke-log-agent组件参数**

用户可以通过RawValues参数更新tke-log-agent组件支持的自定义配置参数，比如设置启用kafkalistener，可以将 {"kafkalistener":{"enabled":true}} 进行base64编码后放入到 RawValues 参数中。tke-log-agent 组件支持的自定义配置参数说明如下：
```
{
    "global": {
        "clsHost": "string, cls服务域名，例如：ap-chengdu.cls.tencentyun.com",
        "cluster": {
            "clustertype": "string，集群管理类型，例如：MANAGED_CLUSTER 或 INDEPENDENT_CLUSTER",
            "kubeminor": "string，集群版本，例如：minor 30.0",
            "kubeversion": "string，集群k8s版本，例如：1.30.0",
            "type": "string，集群类型，例如：tke 或 eks"
        },
        "clusterID": "string，集群ID，例如：cls-qbc3zefo",
        "hostNetwork": "bool，是否使用hostNetwork，例如：false",
        "localRegion": "string，集群所在地域，例如：ap-chengdu",
        "registry": "string，镜像仓库，例如：ccr.ccs.tencentyun.com",
        "sources": "string，鉴权方式，例如：norm"
    },
    "kafkalistener": {
        "enabled": "bool，是否启用kafkalistener，例如：true",
    },
    "logAgent": {
        "enabled": "bool，是否启用logAgent，例如：true",
    },
    "loglistener": {
        "enabled": "bool，是否启用loglistener",
    },
    "provisioner": {
        "replicaCount": "int，cls-provisioner副本数，例如：2",
        "sources": "string，cls-provisioner鉴权方式，例如：norm"
    }
}
```

Input: 

```
tccli tke UpdateAddon --cli-unfold-argument  \
    --ClusterId cls-qbc3zefo \
    --AddonName tke-log-agent \
    --RawValues eyJrYWZrYWxpc3RlbmVyIjp7ImVuYWJsZWQiOnRydWV9fQ== \
    --UpdateStrategy merge
```

Output: 
```
{
    "Response": {
        "RequestId": "f55aaa93-c681-47c9-860a-59ae16ajgf1"
    }
}
```

**Example 4: 更新cluster-autoscaler参数**

用户可以通过RawValues参数更新cluster-autoscaler组件支持的自定义配置参数，比如关闭缩容，可以将 {"extraArgs":{"scale-down-enabled":false}}  进行base64编码后放入到 RawValues 参数中。cluster-autoscaler组件支持的自定义配置参数说明如下：
```
{
  "extraArgs": {
    "expander": string, 扩容策略，例如：random
    "ignore-daemonsets-utilization": bool, ds类型不计入利用率，例如：false
    "max-empty-bulk-delete": int, 空节点最大并发缩容数，例如：10
    "scale-down-delay-after-add": string, 扩容后再触发缩容等待时间，例如：10m
    "scale-down-enabled": bool, 开启缩容能力，例如：false
    "scale-down-unneeded-time": string, 节点连续空闲触发缩容时间，例如：10m
    "scale-down-utilization-threshold": float, 触发缩容节点利用率阈值，例如：0.5
    "skip-nodes-with-local-storage": bool, 不缩容包含本地存储的节点，例如：true
    "skip-nodes-with-system-pods": bool 不缩容kube-system namespace下非DaemonSet管理的Pod的节点，例如：true
  }
}
```

Input: 

```
tccli tke UpdateAddon --cli-unfold-argument  \
    --ClusterId cls-qbc3zefo \
    --AddonName cluster-autoscaler \
    --RawValues eyJleHRyYUFyZ3MiOnsic2NhbGUtZG93bi1lbmFibGVkIjpmYWxzZX19 \
    --UpdateStrategy merge
```

Output: 
```
{
    "Response": {
        "RequestId": "b0a2e412-6e5e-4a93-9a22-edf5102e9eae"
    }
}
```

