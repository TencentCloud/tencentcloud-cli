**Example 1: 修改label**

修改label

Input: 

```
tccli monitor ModifyPrometheusAgentExternalLabels --cli-unfold-argument  \
    --InstanceId abc \
    --ClusterId abc \
    --ExternalLabels.0.Name abc \
    --ExternalLabels.0.Value abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

