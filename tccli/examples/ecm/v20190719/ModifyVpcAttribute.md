**Example 1: 修改VPC名称&描述**



Input: 

```
tccli ecm ModifyVpcAttribute --cli-unfold-argument  \
    --VpcName vpc名称 \
    --VpcId vpc-vpc-q6cke2sv \
    --EcmRegion ap-hangzhou-ecm \
    --Description vpc描述
```

Output: 
```
{
    "Response": {
        "RequestId": "60329c63-0abb-4c4e-b875-c6b01c44e294"
    }
}
```

