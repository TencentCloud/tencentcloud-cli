**Example 1: 查询证书安装任务**



Input: 

```
tccli lighthouse DescribeInstallCertificateTasks --cli-unfold-argument  \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "InstallCertificateTaskSet": [
            {
                "InstanceId": "lhins-aaaabbbb",
                "CertificateId": "yrrzyb53",
                "Domain": "a.b.com",
                "InvocationId": "inv-aaaaeeee",
                "TaskStatus": "PENDING",
                "TaskOutput": "",
                "InstallTime": "2022-09-23T07:41:55Z"
            }
        ],
        "RequestId": "cb31e424-0b5f-4f25-8cfc-76121aed5b58"
    }
}
```

