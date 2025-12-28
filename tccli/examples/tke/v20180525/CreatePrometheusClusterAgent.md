**Example 1: 关联eks集群**



Input: 

```
tccli tke CreatePrometheusClusterAgent --cli-unfold-argument  \
    --InstanceId prom-2tghe0lv \
    --Agents.0.Region ap-beijing \
    --Agents.0.EnableExternal False \
    --Agents.0.ClusterId cls-ou716dcp \
    --Agents.0.NotScrape True \
    --Agents.0.ClusterType eks
```

Output: 
```
{
    "Response": {
        "RequestId": "562197b9-5253-4981-yb2c-8c648fc5dec8"
    }
}
```

