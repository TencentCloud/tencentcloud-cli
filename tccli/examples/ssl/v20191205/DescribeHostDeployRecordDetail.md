**Example 1: 查询证书云资源部署记录详情 - clb**



Input: 

```
tccli ssl DescribeHostDeployRecordDetail --cli-unfold-argument  \
    --DeployRecordId 74889
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "SuccessTotalCount": 1,
        "FailedTotalCount": 0,
        "RunningTotalCount": 0,
        "DeployRecordDetailList": [
            {
                "Id": 182241,
                "CertId": "Fvu**OA",
                "OldCertId": "FxG***jc",
                "Status": 1,
                "ErrorMsg": "",
                "CreateTime": "2024-06-26T11:36:33.000000Z",
                "UpdateTime": "2024-06-26T11:37:40.000000Z",
                "InstanceId": "lb-jaj**fy",
                "InstanceName": "zrhtest2",
                "ListenerId": "lbl-fx***3l2",
                "ListenerName": "zrhtest7",
                "Domains": [
                    "clb.tencent.com"
                ],
                "Protocol": "HTTPS",
                "SniSwitch": 1,
                "Bucket": "",
                "Namespace": "",
                "SecretName": "",
                "EnvId": "",
                "TCBType": "",
                "Region": "",
                "Port": 0,
                "Url": [
                    "/zrh1",
                    "/zrh2"
                ]
            }
        ],
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

**Example 2: 查询证书云资源部署记录详情 - cdn**



Input: 

```
tccli ssl DescribeHostDeployRecordDetail --cli-unfold-argument  \
    --DeployRecordId 264850
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "SuccessTotalCount": 1,
        "FailedTotalCount": 0,
        "RunningTotalCount": 0,
        "DeployRecordDetailList": [
            {
                "Id": 264850,
                "CertId": "Ls1nawoK",
                "OldCertId": "JasJqQ1B",
                "Domains": [
                    "cdn.tencent.com.cn|on"
                ],
                "Status": 1,
                "ErrorMsg": "",
                "CreateTime": "2025-02-11T07:47:55.000000Z",
                "UpdateTime": "2025-02-11T07:48:35.000000Z",
                "InstanceId": "",
                "InstanceName": "",
                "ListenerId": "",
                "ListenerName": "",
                "Protocol": "",
                "SniSwitch": 0,
                "Bucket": "",
                "Namespace": "",
                "SecretName": "",
                "EnvId": "",
                "TCBType": "",
                "Region": "",
                "Port": 0
            }
        ],
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

**Example 3: 查询证书云资源部署记录详情 - ddos**



Input: 

```
tccli ssl DescribeHostDeployRecordDetail --cli-unfold-argument  \
    --DeployRecordId 263399 \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 4,
        "SuccessTotalCount": 4,
        "FailedTotalCount": 0,
        "RunningTotalCount": 0,
        "DeployRecordDetailList": [
            {
                "Id": 263399,
                "CertId": "Lzaz1esU",
                "OldCertId": "jUTl1xsU",
                "Status": 1,
                "ErrorMsg": "",
                "CreateTime": "2025-02-08T01:57:41.000000Z",
                "UpdateTime": "2025-02-08T01:59:09.000000Z",
                "InstanceId": "bgpip-000001a6",
                "InstanceName": "",
                "ListenerId": "",
                "ListenerName": "",
                "Protocol": "https",
                "SniSwitch": 0,
                "Domains": [
                    "*.live.tencent.com"
                ],
                "Bucket": "",
                "Namespace": "",
                "SecretName": "",
                "EnvId": "",
                "TCBType": "",
                "Region": "",
                "Port": "443"
            }
        ],
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

**Example 4: 查询证书云资源部署记录详情 - live**



Input: 

```
tccli ssl DescribeHostDeployRecordDetail --cli-unfold-argument  \
    --DeployRecordId 264682
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "SuccessTotalCount": 1,
        "FailedTotalCount": 0,
        "RunningTotalCount": 0,
        "DeployRecordDetailList": [
            {
                "Id": 264682,
                "CertId": "L12st1jn",
                "OldCertId": "CzcaA1ls",
                "Status": 1,
                "ErrorMsg": "",
                "CreateTime": "2025-02-11T03:30:31.000000Z",
                "UpdateTime": "2025-02-11T03:30:51.000000Z",
                "InstanceId": "",
                "InstanceName": "",
                "ListenerId": "",
                "ListenerName": "",
                "Protocol": "",
                "SniSwitch": 0,
                "Domains": [
                    "live.tencent.com"
                ],
                "Bucket": "",
                "Namespace": "",
                "SecretName": "",
                "EnvId": "",
                "TCBType": "",
                "Region": "",
                "Port": 0
            }
        ],
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

**Example 5: 查询证书云资源部署记录详情 - waf**



Input: 

```
tccli ssl DescribeHostDeployRecordDetail --cli-unfold-argument  \
    --DeployRecordId 264637 \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 3,
        "SuccessTotalCount": 3,
        "FailedTotalCount": 0,
        "RunningTotalCount": 0,
        "DeployRecordDetailList": [
            {
                "Id": 264637,
                "CertId": "Lc1ts2cA",
                "OldCertId": "Lak1z8Cj",
                "Status": 1,
                "Domains": [
                    "waf.tencent.com"
                ],
                "ErrorMsg": "",
                "CreateTime": "2025-02-11T03:19:58.000000Z",
                "UpdateTime": "2025-02-11T03:20:21.000000Z",
                "InstanceId": "",
                "InstanceName": "",
                "ListenerId": "",
                "ListenerName": "",
                "Protocol": "",
                "SniSwitch": 0,
                "Bucket": "",
                "Namespace": "",
                "SecretName": "",
                "EnvId": "",
                "TCBType": "",
                "Region": "",
                "Port": 0
            }
        ],
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

**Example 6: 查询证书云资源部署记录详情 - apigateway**



Input: 

```
tccli ssl DescribeHostDeployRecordDetail --cli-unfold-argument  \
    --DeployRecordId 264731
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "SuccessTotalCount": 1,
        "FailedTotalCount": 0,
        "RunningTotalCount": 0,
        "DeployRecordDetailList": [
            {
                "Id": 264731,
                "CertId": "LRxPsIVq",
                "OldCertId": "Ds1VDi7T",
                "Status": 1,
                "ErrorMsg": "",
                "CreateTime": "2025-02-11T04:35:58.000000Z",
                "UpdateTime": "2025-02-11T04:36:41.000000Z",
                "InstanceId": "service-12as3g2c",
                "InstanceName": "SCF_API_SERVICE",
                "Domains": [
                    "apigw.tencent.com"
                ],
                "ListenerId": "",
                "ListenerName": "",
                "Protocol": "http&https",
                "SniSwitch": 0,
                "Bucket": "",
                "Namespace": "",
                "SecretName": "",
                "EnvId": "",
                "TCBType": "",
                "Region": "",
                "Port": 0
            }
        ],
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

**Example 7: 查询证书云资源部署记录详情 - teo**



Input: 

```
tccli ssl DescribeHostDeployRecordDetail --cli-unfold-argument  \
    --DeployRecordId 264789 \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 21,
        "SuccessTotalCount": 21,
        "FailedTotalCount": 0,
        "RunningTotalCount": 0,
        "DeployRecordDetailList": [
            {
                "Id": 264789,
                "CertId": "Lnsfvtx1n",
                "OldCertId": "Bzs14zdw",
                "Domains": [
                    "teo.tencent.com"
                ],
                "Status": 1,
                "ErrorMsg": "",
                "CreateTime": "2025-02-11T06:50:26.000000Z",
                "UpdateTime": "2025-02-11T06:52:23.000000Z",
                "InstanceId": "",
                "InstanceName": "",
                "ListenerId": "",
                "ListenerName": "",
                "Protocol": "",
                "SniSwitch": 0,
                "Bucket": "",
                "Namespace": "",
                "SecretName": "",
                "EnvId": "",
                "TCBType": "",
                "Region": "",
                "Port": 0
            }
        ],
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

**Example 8: 查询证书云资源部署记录详情 - tke**



Input: 

```
tccli ssl DescribeHostDeployRecordDetail --cli-unfold-argument  \
    --DeployRecordId 264571
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "SuccessTotalCount": 1,
        "FailedTotalCount": 0,
        "RunningTotalCount": 0,
        "DeployRecordDetailList": [
            {
                "Id": 264571,
                "CertId": "LAgw11gu",
                "OldCertId": "k4y1ss3g",
                "Status": 1,
                "ErrorMsg": "",
                "CreateTime": "2025-02-11T02:12:13.000000Z",
                "UpdateTime": "2025-02-11T02:12:16.000000Z",
                "InstanceId": "cls-c1g0sk7p",
                "InstanceName": "prod",
                "Namespace": "prod",
                "SecretName": "tencent-k4y1ss3g",
                "ListenerId": "",
                "ListenerName": "",
                "Protocol": "",
                "SniSwitch": 0,
                "Bucket": "",
                "Domains": [],
                "EnvId": "",
                "TCBType": "",
                "Region": "",
                "Port": 0
            }
        ],
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

**Example 9: 查询证书云资源部署记录详情 - cos**



Input: 

```
tccli ssl DescribeHostDeployRecordDetail --cli-unfold-argument  \
    --DeployRecordId 264845
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "SuccessTotalCount": 1,
        "FailedTotalCount": 0,
        "RunningTotalCount": 0,
        "DeployRecordDetailList": [
            {
                "Id": 264845,
                "CertId": "LA32v1sg",
                "OldCertId": "sffyRsAD",
                "Status": 1,
                "Domains": [
                    "cos.tencent.com"
                ],
                "ErrorMsg": "",
                "CreateTime": "2025-02-11T07:34:27.000000Z",
                "UpdateTime": "2025-02-11T07:34:42.000000Z",
                "InstanceId": "",
                "InstanceName": "",
                "ListenerId": "",
                "ListenerName": "",
                "Protocol": "",
                "SniSwitch": 0,
                "Bucket": "tencent-1251330511",
                "Namespace": "",
                "SecretName": "",
                "EnvId": "",
                "TCBType": "",
                "Region": "",
                "Port": 0
            }
        ],
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

**Example 10: 查询证书云资源部署记录详情 - lighthouse**



Input: 

```
tccli ssl DescribeHostDeployRecordDetail --cli-unfold-argument  \
    --DeployRecordId 264842 \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "SuccessTotalCount": 2,
        "FailedTotalCount": 0,
        "RunningTotalCount": 0,
        "DeployRecordDetailList": [
            {
                "Id": 264842,
                "CertId": "LA3daHbh",
                "OldCertId": "",
                "Status": 1,
                "Domains": [
                    "lh.tencent.com"
                ],
                "ErrorMsg": "",
                "CreateTime": "2025-02-11T07:26:47.000000Z",
                "UpdateTime": "2025-02-11T07:27:45.000000Z",
                "InstanceId": "lhins-122iisds",
                "InstanceName": "",
                "ListenerId": "",
                "ListenerName": "",
                "Protocol": "",
                "Namespace": "",
                "SecretName": "",
                "Port": 0,
                "SniSwitch": 0,
                "EnvId": "",
                "TCBType": "",
                "Region": "",
                "Bucket": ""
            }
        ],
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

**Example 11: 查询证书云资源部署记录详情 - vod**



Input: 

```
tccli ssl DescribeHostDeployRecordDetail --cli-unfold-argument  \
    --DeployRecordId 264268
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "SuccessTotalCount": 1,
        "FailedTotalCount": 0,
        "RunningTotalCount": 0,
        "DeployRecordDetailList": [
            {
                "Id": 264268,
                "CertId": "LAGVhA1g",
                "OldCertId": "C1scyc27",
                "Status": 1,
                "Domains": [
                    "vod.tencent.com"
                ],
                "ErrorMsg": "",
                "CreateTime": "2025-02-10T08:29:15.000000Z",
                "UpdateTime": "2025-02-10T08:29:35.000000Z",
                "InstanceId": "",
                "InstanceName": "",
                "ListenerId": "",
                "ListenerName": "",
                "Protocol": "",
                "Namespace": "",
                "SecretName": "",
                "Port": 0,
                "SniSwitch": 0,
                "EnvId": "",
                "TCBType": "",
                "Region": "",
                "Bucket": ""
            }
        ],
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

**Example 12: 查询证书云资源部署记录详情 - tcb**



Input: 

```
tccli ssl DescribeHostDeployRecordDetail --cli-unfold-argument  \
    --DeployRecordId 264553 \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "SuccessTotalCount": 2,
        "FailedTotalCount": 0,
        "RunningTotalCount": 0,
        "DeployRecordDetailList": [
            {
                "Id": 264553,
                "CertId": "LAeV7s2s",
                "OldCertId": "JaRvVaT2",
                "Status": 1,
                "Domains": [
                    "tencent.com"
                ],
                "ErrorMsg": "",
                "CreateTime": "2025-02-11T01:32:54.000000Z",
                "UpdateTime": "2025-02-11T01:33:44.000000Z",
                "InstanceId": "",
                "InstanceName": "",
                "ListenerId": "",
                "ListenerName": "",
                "Protocol": "",
                "Namespace": "",
                "SecretName": "",
                "Port": 0,
                "SniSwitch": 0,
                "EnvId": "cloud1-2vjs6dvjbabavf5f",
                "TCBType": "AccessService",
                "Region": "ap-shanghai",
                "Bucket": ""
            }
        ],
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

**Example 13: 查询证书云资源部署记录详情 - tse**



Input: 

```
tccli ssl DescribeHostDeployRecordDetail --cli-unfold-argument  \
    --DeployRecordId 264600
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "SuccessTotalCount": 1,
        "FailedTotalCount": 0,
        "RunningTotalCount": 0,
        "DeployRecordDetailList": [
            {
                "Id": 264600,
                "CertId": "Arj3s7PT",
                "OldCertId": "fhashp31",
                "Status": 1,
                "ErrorMsg": "",
                "CreateTime": "2025-02-11T02:35:55.000000Z",
                "UpdateTime": "2025-02-11T02:36:33.000000Z",
                "InstanceId": "gateway-aavb1av3",
                "InstanceName": "tencent",
                "Namespace": "",
                "SecretName": "",
                "ListenerId": "51426ae8-3325-4ac8-caab-a1fe5d5s012a",
                "ListenerName": "tencent",
                "Protocol": "",
                "SniSwitch": 0,
                "Bucket": "",
                "Domains": [
                    "tse.tencent.com"
                ],
                "EnvId": "",
                "TCBType": "",
                "Region": "",
                "Port": 0
            }
        ],
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

