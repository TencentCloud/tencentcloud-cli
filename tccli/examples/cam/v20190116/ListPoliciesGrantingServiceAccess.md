**Example 1: 所有已授权服务**



Input: 

```
tccli cam ListPoliciesGrantingServiceAccess --cli-unfold-argument  \
    --TargetUin 100000001
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Service": {
                    "ServiceType": "cvm",
                    "ServiceName": "云服务器"
                },
                "Action": [],
                "Policy": [
                    {
                        "PolicyId": "73019980",
                        "PolicyName": "policygen-20210xxxxxxx",
                        "PolicyDescription": "-",
                        "PolicyType": "Custom"
                    }
                ]
            }
        ],
        "RequestId": "6de4c96b-60be-4422-8fe8-5ac09707a116"
    }
}
```

**Example 2: 查看已授权服务中所有已授权接口**



Input: 

```
tccli cam ListPoliciesGrantingServiceAccess --cli-unfold-argument  \
    --TargetUin 100000001 \
    --ServiceType cvm
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Service": {
                    "ServiceType": "cvm",
                    "ServiceName": "云服务器"
                },
                "Action": [
                    {
                        "Name": "AddInstanceInDeployGroup",
                        "Description": "新增实例部署组"
                    }
                ],
                "Policy": [
                    {
                        "PolicyId": "73019980",
                        "PolicyName": "policygen-20210xxxxxxx",
                        "PolicyDescription": "-",
                        "PolicyType": "Custom"
                    }
                ]
            }
        ],
        "RequestId": "6de4c96b-60be-4422-8fe8-5ac09707a116"
    }
}
```

