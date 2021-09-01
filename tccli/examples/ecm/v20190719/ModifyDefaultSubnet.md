**Example 1: 设置杭州一区默认子网**



Input: 

```
tccli ecm ModifyDefaultSubnet --cli-unfold-argument  \
    --EcmRegion ap-hangzhou-ecm \
    --Zone ap-hangzhou-ecm-1 \
    --VpcId vpc-cp6wknwh \
    --SubnetId subnet-jxa0xg1o
```

Output: 
```
{
    "Response": {
        "RequestId": "7daa4e7c-7698-4cc1-8ed0-2f729462c110"
    }
}
```

