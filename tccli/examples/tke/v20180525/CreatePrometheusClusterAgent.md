**Example 1: 关联集群**



Input: 

```
tccli tke CreatePrometheusClusterAgent --cli-unfold-argument  \
    --InstanceId abc \
    --Agents.0.Region abc \
    --Agents.0.ClusterType abc \
    --Agents.0.ClusterId abc \
    --Agents.0.InClusterPodConfig.HostNet True \
    --Agents.0.InClusterPodConfig.NodeSelector.0.Name abc \
    --Agents.0.InClusterPodConfig.NodeSelector.0.Value abc \
    --Agents.0.InClusterPodConfig.Tolerations.0.Key abc \
    --Agents.0.InClusterPodConfig.Tolerations.0.Operator abc \
    --Agents.0.InClusterPodConfig.Tolerations.0.Effect abc \
    --Agents.0.EnableExternal True \
    --Agents.0.ExternalLabels.0.Name abc \
    --Agents.0.ExternalLabels.0.Value abc \
    --Agents.0.NotInstallBasicScrape True \
    --Agents.0.NotScrape True
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

