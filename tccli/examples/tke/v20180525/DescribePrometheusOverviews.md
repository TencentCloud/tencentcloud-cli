**Example 1: 拉取实例列表**



Input: 

```
tccli tke DescribePrometheusOverviews --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Instances": [
            {
                "Status": "xx",
                "VpcId": "xx",
                "Name": "xx",
                "InstanceId": "xx",
                "COSBucket": "xx",
                "SubnetId": "xx"
            }
        ],
        "Total": 1,
        "RequestId": "xx"
    }
}
```

