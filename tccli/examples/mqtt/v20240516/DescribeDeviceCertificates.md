**Example 1: 示例**

示例

Input: 

```
tccli mqtt DescribeDeviceCertificates --cli-unfold-argument  \
    --InstanceId mqtt-qgzaawn9
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Data": [
            {
                "ClientId": "client-1",
                "DeviceCertificateSn": "0eef68a582b94254296e54ce754f94d707a59913",
                "DeviceCertificateCn": "tx",
                "DeviceCertificate": "-----BEGIN CERTIFICATE-----\n-----END CERTIFICATE-----\n",
                "CaSn": "1b1e3bf3702110125887a3a721a7e66f05522513",
                "OrganizationalUnit": "tx",
                "Format": "PEM",
                "Status": "ACTIVE",
                "CertificateSource": "API",
                "LastActivationTime": 1742983099435,
                "LastInactivationTime": 0,
                "CreatedTime": 1742983115198,
                "UpdateTime": 1742983115198,
                "NotBeforeTime": 1734537600000,
                "NotAfterTime": 1766073600000
            }
        ],
        "RequestId": "378f8c36-a6a1-406c-85ac-f2379386eed6",
        "TotalCount": 0
    }
}
```

