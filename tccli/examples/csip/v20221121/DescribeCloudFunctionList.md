**Example 1: 云函数列表**



Input: 

```
tccli csip DescribeCloudFunctionList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "FunctionList": [
            {
                "AccountInfo": "10009212/测试账号",
                "CoreAssetFlag": "core",
                "Domain": "bm.com",
                "FunctionType": "HTTP",
                "InstanceName": "http-xlQBVib0ex",
                "InstanceStatus": "active",
                "InstanceStatusDisplay": "正常",
                "InstanceTag": "核心资产",
                "Namespace": "default",
                "Region": "华南地区(广州)",
                "InstanceType": "scf_instance",
                "PrivateURL": "",
                "PublicURL": "",
                "AppID": 67267321,
                "InstanceID": "lam-xsu132"
            }
        ],
        "RegionList": [
            {
                "Text": "华南地区(广州)",
                "Value": "ap-guangzhou"
            }
        ],
        "RequestId": "adc882615-725b-4fd1-b74c-b9ca981412b1",
        "TotalCount": 1
    }
}
```

