**Example 1: 修改label**



Input: 

```
tccli tke ModifyPrometheusAgentExternalLabels --cli-unfold-argument  \
    --InstanceId xx \
    --ExternalLabels.0.Name xx \
    --ExternalLabels.0.Value xx \
    --ClusterId xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

