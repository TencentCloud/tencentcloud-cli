**Example 1: LinkPrometheus**

连接Prometheus实例

Input: 

```
tccli tcm LinkPrometheus --cli-unfold-argument  \
    --MeshID "mesh-test" \
    --Prometheus.VpcId test-vpcid \
    --Prometheus.SubnetId test-subnetid \
    --Prometheus.Region sh \
    --Prometheus.InstanceId ""
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

