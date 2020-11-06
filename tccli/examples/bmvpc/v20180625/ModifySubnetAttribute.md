**Example 1: 修改子网名称**

修改子网名称

Input: 

```
tccli bmvpc ModifySubnetAttribute --cli-unfold-argument  \
    --VpcId vpc-q1j48dkd \
    --SubnetId subnet-q1j48dkd \
    --SubnetName test
```

Output: 
```
{
    "Response": {
        "RequestId": "30a4b438-a5f1-4fca-a34e-95dfd07695ca"
    }
}
```

