**Example 1: DescribeCloudInstanceService**

DescribeCloudInstanceService

Input: 

```
tccli emr DescribeCloudInstanceService --cli-unfold-argument  \
    --InstanceId emr-test
```

Output: 
```
{
    "Response": {
        "RequestId": "ecee78a4-f0e7-41a2-8f94-5bce64d82892",
        "ServiceLayerIns": [
            {
                "CloudServices": [
                    {
                        "AddTime": "2023-05-26 11:02:38",
                        "ClusterId": 37563,
                        "DependentClusterId": "",
                        "DisPlay": true,
                        "ExternalService": [
                            "emr-bwcabyig-openldap-slapd-inner"
                        ],
                        "InternalService": [
                            "emr-bwcabyig-openldap-slapd-inner"
                        ],
                        "IsExternal": 0,
                        "PathsInfo": "/usr/libexec/openldap",
                        "ServiceLayer": "middleLayer",
                        "ServiceType": 39,
                        "Soft": "OPENLDAP-2.4.57",
                        "SoftName": "OPENLDAP",
                        "Status": 0,
                        "UserGroup": "root",
                        "UserName": "root"
                    }
                ],
                "ServiceLayer": "middleLayer"
            }
        ],
        "TotalCnt": 1
    }
}
```

