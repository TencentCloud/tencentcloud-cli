**Example 1: 修改分析集群数据源**



Input: 

```
tccli cynosdb ModifyLibraDBClusterDataSource --cli-unfold-argument  \
    --ClusterId libradb-r32u74w9 \
    --InstanceId libradb-ins-0p7mxy28 \
    --SrcInfo.0.SrcInstanceType cynos \
    --SrcInfo.0.SrcInstanceId cynosmysql-ins-123 \
    --SrcInfo.0.SrcClusterId cynosmysql-123 \
    --SrcInfo.0.AccessType vpc \
    --SrcInfo.0.IP 127.0.0.1 \
    --SrcInfo.0.Port 3306 \
    --SrcInfo.0.User root \
    --SrcInfo.0.Password root456
```

Output: 
```
{
    "Response": {
        "FlowId": 2105088,
        "RequestId": "7a24788f-f857-4751-a5aa-a06d676da24c"
    }
}
```

