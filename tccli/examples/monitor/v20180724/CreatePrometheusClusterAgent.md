**Example 1: 关联集群**

关联eks集群

Input: 

```
tccli monitor CreatePrometheusClusterAgent --cli-unfold-argument  \
    --InstanceId prom-wjeh \
    --Agents.0.EnableExternal True \
    --Agents.0.Region ap-jehr \
    --Agents.0.ClusterId cls-hrbr \
    --Agents.0.ClusterType eks \
    --Agents.0.NotInstallBasicScrape True \
    --Agents.0.InClusterPodConfig.HostNet True \
    --Agents.0.InClusterPodConfig.Tolerations.0.Operator Exists \
    --Agents.0.InClusterPodConfig.Tolerations.0.Effect NoSchedule \
    --Agents.0.InClusterPodConfig.Tolerations.0.Key key-name \
    --Agents.0.InClusterPodConfig.NodeSelector.0.Name label-name \
    --Agents.0.InClusterPodConfig.NodeSelector.0.Value label-value \
    --Agents.0.NotScrape True \
    --Agents.0.ExternalLabels.0.Name label-name \
    --Agents.0.ExternalLabels.0.Value label-value
```

Output: 
```
{
    "Response": {
        "RequestId": "ejfhfol-lejrgbf"
    }
}
```

**Example 2: 关联eks集群**

关联eks集群

Input: 

```
tccli monitor CreatePrometheusClusterAgent --cli-unfold-argument  \
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

