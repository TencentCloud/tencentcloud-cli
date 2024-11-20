**Example 1: 查询所有网络探测**

查询所有网络探测

Input: 

```
tccli vpc DescribeNetDetects --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "NetDetectSet": [
            {
                "VpcId": "vpc-12345678",
                "VpcName": "vpc-kngiybxl",
                "SubnetId": "subnet-nswq8wkq",
                "SubnetName": "demo",
                "NetDetectId": "netd-pnpcflil",
                "NetDetectName": "demo",
                "DetectDestinationIp": [
                    "10.0.0.2",
                    "10.0.0.3"
                ],
                "DetectSourceIp": [
                    "10.0.0.5",
                    "10.0.0.6"
                ],
                "NextHopType": "NORMAL_CVM",
                "NextHopDestination": "10.0.0.4",
                "NextHopName": "",
                "NetDetectDescription": "",
                "CreateTime": "2020-06-08 10:00:00"
            },
            {
                "VpcId": "vpc-kngiybxl",
                "VpcName": "demo",
                "SubnetId": "subnet-nswq8wkq",
                "SubnetName": "demo",
                "NetDetectId": "netd-4t7fr3fi",
                "NetDetectName": "demo",
                "DetectDestinationIp": [
                    "10.0.1.2",
                    "10.0.1.3"
                ],
                "DetectSourceIp": [
                    "10.0.1.5",
                    "10.0.1.6"
                ],
                "NextHopType": "NORMAL_CVM",
                "NextHopDestination": "10.0.0.4",
                "NextHopName": "",
                "NetDetectDescription": "",
                "CreateTime": "2020-06-08 10:00:00"
            }
        ],
        "TotalCount": 2,
        "RequestId": "6aa316a4-07d2-4355-b87d-40b7f22972b0"
    }
}
```

**Example 2: 根据ID查询网络探测**

根据ID查询网络探测

Input: 

```
tccli vpc DescribeNetDetects --cli-unfold-argument  \
    --NetDetectIds netd-pnpcflil
```

Output: 
```
{
    "Response": {
        "NetDetectSet": [
            {
                "VpcId": "vpc-kngiybxl",
                "VpcName": "vpc-test",
                "SubnetId": "subnet-nswq8wkq",
                "SubnetName": "demo",
                "NetDetectId": "netd-pnpcflil",
                "NetDetectName": "demo",
                "DetectDestinationIp": [
                    "10.0.0.2",
                    "10.0.0.3"
                ],
                "DetectSourceIp": [
                    "10.0.0.5",
                    "10.0.0.6"
                ],
                "NextHopType": "NORMAL_CVM",
                "NextHopDestination": "10.0.0.4",
                "NextHopName": "",
                "NetDetectDescription": "",
                "CreateTime": "2020-06-08 10:00:00"
            }
        ],
        "TotalCount": 1,
        "RequestId": "6aa316a4-07d2-4355-b87d-40b7f22972b0"
    }
}
```

