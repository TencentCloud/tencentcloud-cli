**Example 1: 拉取实例列表**

拉取实例列表

Input: 

```
tccli tke DescribePrometheusOverviews --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Instances": [
            {
                "Status": "running",
                "VpcId": "vpc-dsajgfksj",
                "Name": "测试实例",
                "InstanceId": "prom-sdsahfuf",
                "COSBucket": "prometheus-prom-xdfsfffwed-data-1234567898",
                "SubnetId": "subnet-hjkghjgjk"
            }
        ],
        "Total": 1,
        "RequestId": "0e5873a3-8525-41c1-9ba9-dshjahdfkjfhg"
    }
}
```

