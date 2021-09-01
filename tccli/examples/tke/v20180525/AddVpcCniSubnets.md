**Example 1: 为VPC-CNI模式集群增加子网**

当用户选择了VPC-CNI网络模式时，创建集群时选择的子网资源IP可能将来不足，需要增加子网。

Input: 

```
tccli tke AddVpcCniSubnets --cli-unfold-argument  \
    --VpcId vpc-xxxx \
    --ClusterId cls-xxxx \
    --SubnetIds subnet-xxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

