**Example 1: 修改私有网络VPC的属性**

修改私有网络的名称或者监控标识

Input: 

```
tccli bmvpc ModifyVpcAttribute --cli-unfold-argument  \
    --VpcId vpc-ox7p0l9u \
    --VpcIName test
```

Output: 
```
{
    "Response": {
        "RequestId": "72899e7e-dbeb-4add-bf8f-8efe5a315f98"
    }
}
```

