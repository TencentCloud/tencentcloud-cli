**Example 1: 删除agent**

删除agent

Input: 

```
tccli monitor DeletePrometheusClusterAgent --cli-unfold-argument  \
    --Agents.0.ClusterType cls-kehr \
    --Agents.0.ClusterId tke \
    --Agents.0.Describe test-des \
    --InstanceId prom-sjerg
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

