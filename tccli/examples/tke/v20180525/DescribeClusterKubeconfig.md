**Example 1: Obtaining the cluster kubeconfig file**



Input: 

```
tccli tke DescribeClusterKubeconfig --cli-unfold-argument  \
    --ClusterId cls-65r1c5nu
```

Output: 
```
{
    "Response": {
        "Kubeconfig": "xxx",
        "RequestId": "33483fde-efec-4d3c-8ff6-340d9dbc2d01"
    }
}
```

