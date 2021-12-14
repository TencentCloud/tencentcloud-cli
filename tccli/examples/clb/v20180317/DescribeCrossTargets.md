**Example 1: 查询跨域2.0版本云联网后端子机和网卡信息**



Input: 

```
tccli clb DescribeCrossTargets --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "CrossTargetSet": [
            {
                "LocalVpcId": "vpc-test1234",
                "VpcId": "vpc-test4321",
                "IP": "10.22.106.8",
                "VpcName": "测试",
                "EniId": "eni-test1234",
                "InstanceId": "ins-test1234",
                "InstanceName": "test",
                "Region": "ap-shanghai"
            }
        ],
        "TotalCount": 1,
        "RequestId": "7717db32-9080-4391-acd7-18f8bbd0664d"
    }
}
```

