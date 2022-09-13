**Example 1: 修改边缘计算集群**

修改边缘计算集群

Input: 

```
tccli tke UpdateTKEEdgeCluster --cli-unfold-argument  \
    --ClusterName test_cluster1 \
    --ClusterDesc my_test_cluster888 \
    --ClusterId cls-xxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

