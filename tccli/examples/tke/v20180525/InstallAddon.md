**Example 1: 安装cbs组件**

用户安装cbs组件时支持通过RawValues配置自定义参数，比如设置容忍调度，可以将 {"tolerations":[{"effect":"NoExecute","key":"gpu-not-ready","operator":"Equal","tolerationSeconds":300,"value":"true"},{"key":"ip-not-ready","operator":"Exists"}]} 进行base64编码后放入到 RawValues 参数中。cbs组件支持的自定义配置参数说明如下：
```
{
  "tolerations": [
    {
      "effect": "string, 效果，例如：NoExecute",
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
tccli tke InstallAddon --cli-unfold-argument  \
    --ClusterId cls-qbc3zefo \
    --AddonName cbs \
    --RawValues eyJ0b2xlcmF0aW9ucyI6W3siZWZmZWN0IjoiTm9FeGVjdXRlIiwia2V5IjoiZ3B1LW5vdC1yZWFkeSIsIm9wZXJhdG9yIjoiRXF1YWwiLCJ0b2xlcmF0aW9uU2Vjb25kcyI6MzAwLCJ2YWx1ZSI6InRydWUifSx7ImtleSI6ImlwLW5vdC1yZWFkeSIsIm9wZXJhdG9yIjoiRXhpc3RzIn1dfQ==
```

Output: 
```
{
    "Response": {
        "RequestId": "b583f05e-d4f4-4963-8082-b651605hg432"
    }
}
```

**Example 2: 安装eniipamd组件**

用户安装eniipamd组件时支持通过RawValues配置自定义参数，比如添加安全组，可以将 {"vpcCni":{"securityGroups":{"securityGroups":["sg-qbc3zefo"]}}} 进行base64编码后放入到 RawValues 参数中。eniipamd组件支持的自定义配置参数说明如下：
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
tccli tke InstallAddon --cli-unfold-argument  \
    --ClusterId cls-qbc3zefo \
    --AddonName eniipamd \
    --RawValues eyJ2cGNDbmkiOnsic2VjdXJpdHlHcm91cHMiOnsic2VjdXJpdHlHcm91cHMiOlsic2ctMTIzNDU2NzgiXX19fQ==
```

Output: 
```
{
    "Response": {
        "RequestId": "b583f05e-d4f4-4963-8082-b651605jh275"
    }
}
```

**Example 3: 安装tcr组件**

用户可以通过 RawValues 参数制定组件需要的配置参数，比如 imagePullSecretsCrs。 tcr 组件支持的配置参数示例如下：
```
{
    "global": {
        "imagePullSecretsCrs": [
            {
                "name": "string，imagePullSecretsCr 的名称，例如：tcr-qbc3zefo-public",
                "namespaces": "string，免密功能作用范围，例如：* 表示所有命名空间",
                "serviceAccounts": "string，免密功能作用范围，例如：* 表示所有k8s服务账户",
                "type": "string，必须为 docker",
                "dockerUsername": "string，镜像仓库登录用户名",
                "dockerPassword": "string，镜像仓库登录密码",
                "dockerServer": "string，镜像仓库服务器地址"
            }
        ]
    }
}
```

Input: 

```
tccli tke InstallAddon --cli-unfold-argument  \
    --ClusterId cls-qbc3zefo \
    --AddonName tcr \
    --RawValues eyJnbG9iYWwiOnsiaW1hZ2VQdWxsU2VjcmV0c0NycyI6W3sibmFtZSI6InRjci1kZzI4NGltcS1wdWJsaWMiLCJuYW1lc3BhY2VzIjoiKiIsInNlcnZpY2VBY2NvdW50cyI6IioiLCJ0eXBlIjoiZG9ja2VyIiwiZG9ja2VyVXNlcm5hbWUiOiIxMDAwMTQzNjQ4MjIiLCJkb2NrZXJQYXNzd29yZCI6IjEyMzQ1Njc4IiwiZG9ja2VyU2VydmVyIjoibmljb2thbmctdGNyLWd6LnRlbmNlbnRjbG91ZGNyLmNvbSJ9XX19
```

Output: 
```
{
    "Response": {
        "RequestId": "b583f05e-d4f4-4963-8082-b651605ca765"
    }
}
```

**Example 4: 安装tke-log-agent组件**

用户安装tke-log-agent组件时支持通过RawValues配置自定义参数，比如设置启用kafkalistener，可以将 {"kafkalistener":{"enabled":true}} 进行base64编码后放入到 RawValues 参数中。tke-log-agent 组件支持的自定义配置参数说明如下：
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
tccli tke InstallAddon --cli-unfold-argument  \
    --ClusterId cls-e55paxnt \
    --AddonName tke-log-agent \
    --RawValues eyJrYWZrYWxpc3RlbmVyIjp7ImVuYWJsZWQiOnRydWV9fQ==
```

Output: 
```
{
    "Response": {
        "RequestId": "b583f05e-d4f4-4963-8082-b651605ca427"
    }
}
```

