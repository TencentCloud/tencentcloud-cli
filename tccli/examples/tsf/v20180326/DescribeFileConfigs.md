**Example 1: 查询文件配置项列表**



Input: 

```
tccli tsf DescribeFileConfigs --cli-unfold-argument  \
    --ConfigName sadf \
    --ApplicationId application-6ymrrbag \
    --Offset 0 \
    --Limit 50
```

Output: 
```
{
    "Response": {
        "RequestId": "678168f0-96f6-4d78-838c-7bcd5a305e65",
        "Result": {
            "TotalCount": 1,
            "Content": [
                {
                    "ConfigId": "dcfg-f-zvw5q89v",
                    "ConfigName": "sadf",
                    "ConfigVersion": "1.0",
                    "ConfigVersionDesc": null,
                    "ConfigFileName": "Dockerfile",
                    "ConfigFileCode": "UTF-8",
                    "ConfigFileValue": "FROM centos:7\r\n\r\nRUN echo \"ip_resolve=4\" >> /etc/yum.conf\r\nRUN yum update -y && yum install -y java-1.8.0-openjdk\r\n\r\nCOPY demo-calculate-1.10.0-RELEASE.jar /data/tsf/\r\nCOPY run.sh /data/tsf/\r\n\r\n# GMT+8 for CentOS\r\nRUN /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime\r\nRUN echo \"Asia/Shanghai\" > /etc/timezone\r\n\r\n# run.sh\r\nCMD [\"sh\", \"-c\", \"cd /data/tsf; sh run.sh demo-calculate-1.10.0-RELEASE.jar /data/tsf\"]\r\n",
                    "ConfigFilePath": "/a/",
                    "ConfigPostCmd": null,
                    "CreationTime": "2019-03-28 18:16:40",
                    "LastUpdateTime": null,
                    "ConfigVersionCount": null,
                    "ApplicationId": "application-6ymrrbag",
                    "ApplicationName": "provider",
                    "DeleteFlag": true,
                    "ConfigFileValueLength": 419
                }
            ]
        }
    }
}
```

