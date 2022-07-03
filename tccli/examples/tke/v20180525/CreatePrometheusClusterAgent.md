**Example 1: 关联集群**



Input: 

```
tccli tke CreatePrometheusClusterAgent --cli-unfold-argument  \
    --InstanceId xx \
    --Agents.0.EnableExternal True \
    --Agents.0.Region xx \
    --Agents.0.ClusterId xx \
    --Agents.0.ClusterType xx \
    --Agents.0.NotInstallBasicScrape True \
    --Agents.0.InClusterPodConfig.HostNet True \
    --Agents.0.InClusterPodConfig.Tolerations.0.Operator xx \
    --Agents.0.InClusterPodConfig.Tolerations.0.Effect xx \
    --Agents.0.InClusterPodConfig.Tolerations.0.Key xx \
    --Agents.0.InClusterPodConfig.NodeSelector.0.Name xx \
    --Agents.0.InClusterPodConfig.NodeSelector.0.Value xx \
    --Agents.0.NotScrape True \
    --Agents.0.ExternalLabels.0.Name xx \
    --Agents.0.ExternalLabels.0.Value xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx"
    }
}
```

**Example 2: 关联eks集群**



Input: 

```
tccli tke CreatePrometheusClusterAgent --cli-unfold-argument  \
    --InstanceId prom-2tghe0lv \
    --Agents.0.Region ap-beijing \
    --Agents.0.EnableExternal false \
    --Agents.0.ClusterId cls-ou716dcp \
    --Agents.0.NotScrape true \
    --Agents.0.ClusterType eks
```

Output: 
```
{
    "Response": {
        "RequestId": "562197b9-5253-4981-ab2c-8c648fc5dec8"
    }
}
```

