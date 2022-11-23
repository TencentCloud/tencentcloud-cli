**Example 1: 修改高性能计算集群名称**

修改高性能计算集群名称

Input: 

```
tccli cvm ModifyHpcClusterAttribute --cli-unfold-argument  \
    --HpcClusterId hpc-gzahhoy5 \
    --Name test
```

Output: 
```
{
    "Response": {
        "RequestId": "5834f1a5-cd9c-449d-acba-df1803a8583e"
    }
}
```

