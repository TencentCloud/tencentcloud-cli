**Example 1: 删除命名空间**



Input: 

```
tccli tdmq DeleteEnvironments --cli-unfold-argument  \
    --EnvironmentIds devNs \
    --ClusterId pulsar-5r59xd4vnx
```

Output: 
```
{
    "Response": {
        "EnvironmentIds": [
            "test1"
        ],
        "RequestId": "db8bd520-496e-4e7c-a4a1-e7414d3c315c"
    }
}
```

