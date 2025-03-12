**Example 1: 拉取prometheus配置**

拉取prometheus配置

Input: 

```
tccli monitor DescribePrometheusConfig --cli-unfold-argument  \
    --InstanceId prom-fdfasasf \
    --ClusterType tke \
    --ClusterId cls-gdgdge
```

Output: 
```
{
    "Response": {
        "Config": "global:\n  scrape_interval: 15s",
        "ServiceMonitors": [
            {
                "Name": "test-sm",
                "Config": "scrape_interval:5s\n",
                "TemplateId": "temp-akdj",
                "Targets": {
                    "Total": 1,
                    "Up": 1,
                    "Down": 1,
                    "Unknown": 1
                }
            }
        ],
        "PodMonitors": [
            {
                "Name": "test-pm",
                "Config": "scrape_interval:5s\n",
                "TemplateId": "temp-akdj",
                "Targets": {
                    "Total": 1,
                    "Up": 1,
                    "Down": 1,
                    "Unknown": 1
                }
            }
        ],
        "RawJobs": [
            {
                "Name": "test-rawjob",
                "Config": "scrape_interval:5s\n",
                "TemplateId": "temp-akdj",
                "Targets": {
                    "Total": 1,
                    "Up": 1,
                    "Down": 1,
                    "Unknown": 1
                }
            }
        ],
        "Probes": [
            {
                "Name": "test-probe",
                "Config": "scrape_interval:5s\n",
                "TemplateId": "temp-akdj",
                "Targets": {
                    "Total": 1,
                    "Up": 1,
                    "Down": 1,
                    "Unknown": 1
                }
            }
        ],
        "ImageNeedUpdate": true,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

