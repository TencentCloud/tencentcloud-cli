**Example 1: 删除agent**



Input: 

```
tccli tke DeletePrometheusClusterAgent --cli-unfold-argument  \
    --InstanceId xx \
    --Agents.0.Describe xx \
    --Agents.0.ClusterId xx \
    --Agents.0.ClusterType xx
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

