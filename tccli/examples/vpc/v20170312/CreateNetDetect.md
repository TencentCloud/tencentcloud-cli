**Example 1: 创建网络探测**

创建网络探测

Input: 

```
tccli vpc CreateNetDetect --cli-unfold-argument  \
    --VpcId vpc-4tw1bxlq \
    --NextHopDestination 10.0.0.4 \
    --NextHopType NORMAL_CVM \
    --NetDetectName demo \
    --DetectDestinationIp 10.0.0.3 10.0.0.2 \
    --SubnetId subnet-6zwa44xm
```

Output: 
```
{
    "Response": {
        "NetDetect": {
            "VpcId": "vpc-4tw1bxlq",
            "VpcName": "demo",
            "SubnetId": "subnet-6zwa44xm",
            "SubnetName": "demo",
            "NetDetectId": "netd-ms7c7gcr",
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
            "CreateTime": "0000-00-00 00:00:00"
        },
        "RequestId": "6aa316a4-07d2-4355-b87d-40b7f22972b0"
    }
}
```

