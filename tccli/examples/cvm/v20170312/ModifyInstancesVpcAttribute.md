**Example 1: Migrating an instance to a VPC and specifying the instance IP**

This example shows you how to migrate the instances `r8hr2upy` and `5d8a23rs` to the subnet `dcs9x3gz` of the VPC `1urkhbj4` and specify 10.0.0.18 as the private IP of the instance `r8hr2upy` and 10.0.0.19 as that of the instance `5d8a23rs`.

Input: 

```
tccli cvm ModifyInstancesVpcAttribute --cli-unfold-argument  \
    --InstanceIds ins-r8hr2upy ins-5d8a23rs\
    --VirtualPrivateCloud.SubnetId subnet-dcs9x3gz\
    --VirtualPrivateCloud.VpcId vpc-1urkhbj4\
    --VirtualPrivateCloud.PrivateIpAddresses 10.0.0.18 10.0.0.19
```

Output: 
```
{
    "Response": {
        "RequestId": "3c14def19-cfes-470e-b241-90787u6jf5uj"
    }
}
```

