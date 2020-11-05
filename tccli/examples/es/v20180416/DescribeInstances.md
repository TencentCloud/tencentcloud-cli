**Example 1: Querying ES cluster instances**

This example shows you how to query eligible ES cluster instances according to the given criteria and return their details.

Input: 

```
tccli es DescribeInstances --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "InstanceList": [
            {
                "InstanceId": "es-sample",
                "InstanceName": "es-sample",
                "InstanceType": 2,
                "Region": "ap-guangzhou",
                "Zone": "ap-guangzhou-2",
                "AppId": 0,
                "Uin": "xxxxxxxx",
                "VpcUid": "vpc-sample",
                "SubnetUid": "subnet-sample",
                "Status": 1,
                "ChargeType": "PREPAID",
                "ChargePeriod": 1,
                "RenewFlag": "RENEW_FLAG_DEFAULT",
                "NodeType": "ES.S1.SMALL2",
                "NodeNum": 2,
                "CpuNum": 1,
                "MemSize": 2,
                "DiskType": "",
                "DiskSize": 100,
                "EsDomain": "es-sample.tencentelasticsearch.com",
                "EsVip": "0.0.0.0",
                "EsPort": 9200,
                "KibanaUrl": "https://es-sample.kibana.tencentelasticsearch.com:5601",
                "EsVersion": "5.6.4",
                "EsConfig": "{}",
                "EsAcl": {
                    "WhiteIpList": [],
                    "BlackIpList": []
                },
                "CreateTime": "2018-07-27 17:28:04",
                "UpdateTime": "2018-07-30 10:22:29",
                "Deadline": "2018-08-27 17:28:04"
            },
            {
                "InstanceId": "es-sample2",
                "InstanceName": "es-sample2",
                "InstanceType": 2,
                "Region": "ap-guangzhou",
                "Zone": "ap-guangzhou-4",
                "AppId": 0,
                "Uin": "xxxxxx",
                "VpcUid": "vpc-sample",
                "SubnetUid": "subnet-sample",
                "Status": 1,
                "ChargeType": "PREPAID",
                "ChargePeriod": 1,
                "RenewFlag": "RENEW_FLAG_DEFAULT",
                "NodeType": "ES.S1.MEDIUM4",
                "NodeNum": 2,
                "CpuNum": 2,
                "MemSize": 4,
                "DiskType": "",
                "DiskSize": 100,
                "EsDomain": "es-sample.tencentelasticsearch.com",
                "EsVip": "0.0.0.0",
                "EsPort": 9200,
                "KibanaUrl": "https://es-sample.kibana.tencentelasticsearch.com:5601",
                "EsVersion": "5.6.4",
                "EsConfig": "{}",
                "EsAcl": {
                    "WhiteIpList": [],
                    "BlackIpList": []
                },
                "CreateTime": "2018-07-26 17:47:47",
                "UpdateTime": "2018-07-26 18:16:50",
                "Deadline": "2018-08-26 17:47:47"
            }
        ],
        "RequestId": "5d5a201f-0a3d-485f-a82f-3c73ccxxxxxx"
    }
}
```

